from math import ceil
from os import close, unlink
from os.path import getsize
from io import BytesIO
from multiprocessing import Process, Queue
# from threading import Thread
# from queue import Queue
from pathlib import Path
from tempfile import gettempdir, mkstemp
from tkinter.filedialog import asksaveasfilename
from typing import Iterable, Union

from fitz import Document
from PIL import Image

from constants import FILE_TYPES_PDF, PHYSICAL_CPU_COUNT

from app.Progress import Progress

from ui.UiCompressPDF import UiCompressPDF
from utils.util import (
    check_dir, check_file_exist, get_pdf_info,
    int2byte_unit, pdf_info, split_drop_data,
    show_tooltip
)
from utils.DndDrop import DndDrop

TEMP_DIR = Path(gettempdir())


class CompressPDF(UiCompressPDF, DndDrop):
    def __init__(self, master=None, **kw):
        super(CompressPDF, self).__init__(master, **kw)
        show_tooltip(self.EntryPDFFile)

        self._pdf_file: Union[str, Path] = ''
        self._page_count = 0
        self._pdf_file_size = 0
        self._compressed_pdf_file: Union[str, Path] = ''
        self._compressed_pdf_file_size = 0
        self._image_quality = 80
        self._image_max_dpi = 144
        self.image_quality.set(self._image_quality)
        self.image_max_dpi.set(self._image_max_dpi)

        self.drop()

    def drop_file(self, event):
        file_list = split_drop_data(event.data)
        for file in file_list:
            if file.suffix.lower() in FILE_TYPES_PDF[0][1]:
                self._pdf_file, self._page_count, _other = pdf_info(file)
                break
        self._set_options()

    def get_pdf_file(self):
        pdfinfo = get_pdf_info()
        if pdfinfo:
            self._pdf_file, self._page_count, _other = pdfinfo
            self._set_options()

    def _set_options(self):
        if self._page_count > 0:
            self.pdf_file.set(self._pdf_file)
            self._pdf_file_size = getsize(self._pdf_file)
            pdfInfo = 'Total Pages: {}, Size: {}. '.format(self._page_count, int2byte_unit(self._pdf_file_size))
            self.pdf_info.set(pdfInfo)
            self._compressed_pdf_file = self._pdf_file.with_suffix('.Compressed.pdf')
            self.compressed_pdf_file.set(self._compressed_pdf_file)
        self._toggle_buttons()

    def set_compressed_pdf_file(self):
        if self._compressed_pdf_file:
            initial_file = self._compressed_pdf_file.name
        else:
            initial_file = ''
        rotated_pdf_file = asksaveasfilename(
            filetypes=FILE_TYPES_PDF,
            defaultextension='.pdf',
            title='Select compressed PDF file',
            initialfile=initial_file
        )
        if rotated_pdf_file:
            self._compressed_pdf_file = Path(rotated_pdf_file)
            self.compressed_pdf_file.set(self._compressed_pdf_file)

        self._toggle_buttons()

    def valid_image_quality(self, d, P, V):
        if d == '0' \
                or d == '1' and P == '0' \
                or d == '1' and not P.startswith('0') and P.isdigit() and 0 <= int(P) <= 100 \
                or V == 'focusout' and P.isdigit() and 0 <= int(P) <= 100:
            if self.EntryImageQuality.grab_status():
                self.EntryImageQuality.grab_release()
            return True

        self.EntryImageQuality.grab_set()
        self.EntryImageQuality.focus()
        return False

    def set_image_quality(self, scale_value):
        value = int(round(float(scale_value) * 2, -1)) // 2  # Scale step: 5
        self._image_quality = value
        self.image_quality.set(self._image_quality)

    def valid_image_dpi(self, d, P, V):
        if d == '0' \
                or d == '1' and not P.startswith('0') and P.isdigit() and 0 < int(P) \
                or V == 'focusout' and P.isdigit() and 0 < int(P):
            if self.ComboboxDPI.grab_status():
                self.ComboboxDPI.grab_release()
            return True

        self.ComboboxDPI.grab_set()
        self.ComboboxDPI.focus()
        return False

    def process(self):
        if not check_file_exist(self._pdf_file):
            return None
        check_dir(self._compressed_pdf_file.parent)

        # split pdf range
        page_range_list = []
        process_count = PHYSICAL_CPU_COUNT
        pdf_page_range = list(range(self._page_count))
        while process_count > 0:
            chunk_size = ceil(len(pdf_page_range) / process_count)
            page_range_list.append(pdf_page_range[:chunk_size])
            pdf_page_range = pdf_page_range[chunk_size:]
            process_count -= 1
        page_range_list = [page_range for page_range in page_range_list if len(page_range)]

        queue = Queue()
        sub_process_list = []
        for process_id, page_range in enumerate(page_range_list):
            sub_process = Process(
                target=compress_pdf,
                args=(
                    queue, self._pdf_file, self._compressed_pdf_file, self._image_quality,
                    self._image_max_dpi, page_range, process_id
                )
            )
            sub_process_list.append(sub_process)
        for sub_process in sub_process_list:
            sub_process.start()
        progress = Progress(process_list=sub_process_list, queue=queue, maximum=self._page_count, auto_destroy=True)
        self.wait_window(progress)  # wait all sub process finished

        if progress.status:
            # merge sub_compressed_pdf
            sub_process = Process(
                target=merge_compressed_pdf,
                args=(queue, self._compressed_pdf_file, page_range_list)
            )
            sub_process_list = [sub_process]
            sub_process.start()
            progress = Progress(process_list=sub_process_list, queue=queue, maximum=len(page_range_list))
            self.wait_window(progress)

            self._compressed_pdf_file_size = getsize(self._compressed_pdf_file)
            compressed_ratio = int(self._compressed_pdf_file_size / self._pdf_file_size * 100)
            # process_info = _('Compressed Size: {}, Compress Ratio: {}%').format(
            process_info = 'Compressed Size: {}, Compress Ratio: {}%'.format(
                int2byte_unit(self._compressed_pdf_file_size), compressed_ratio
            )
            self.process_info.set(process_info)

        for file_no in range(len(page_range_list)):
            sub_compressed_pdf_file = self._compressed_pdf_file.parent / f'{file_no}-{self._compressed_pdf_file.name}'
            try:
                unlink(sub_compressed_pdf_file)
            except FileNotFoundError:
                pass

    def _toggle_buttons(self):
        if self._pdf_file and self._compressed_pdf_file:
            self.ButtonProcess['state'] = 'normal'
        else:
            self.ButtonProcess['state'] = 'disabled'


def compress_pdf(
    queue: Queue, pdf_file: Union[str, Path], compressed_pdf_file: Union[str, Path],
    image_quality: int, max_dpi: int, page_range: Iterable, process_id: int
):
    sub_compressed_pdf_file = TEMP_DIR / f'{process_id}-{compressed_pdf_file.name}'
    with Document(pdf_file) as pdf:
        for page_no in page_range:
            reduced_images_list = _get_reduced_images_list(pdf, page_no, image_quality, max_dpi)
            _remove_images(pdf, page_no)
            page = pdf[page_no]
            for rect, reduced_image in reduced_images_list:
                page.insert_image(rect, filename=reduced_image)
                unlink(reduced_image)
            page.clean_contents()
            queue.put(page_no)

        pdf.save(sub_compressed_pdf_file, deflate=True)


def _remove_images(pdf, page_no):
    page = pdf[page_no]
    page.clean_contents()
    page_xref = page.get_contents()[0]
    contents = page.read_contents()
    for image_info in page.get_images():
        replace_bytes = bytes(f'/{image_info[7]} Do', encoding='utf-8')
        contents = contents.replace(replace_bytes, b'')
    pdf.update_stream(page_xref, contents)
    page.clean_contents()


def _get_reduced_images_list(pdf, page_no, image_quality, image_max_dpi):
    page = pdf[page_no]
    reduced_image_list = []
    for image_info in page.get_images():
        # xref, s_mask, width, height, bpc, colorspace, alt.colorspace, name, filter
        xref = image_info[0]
        width, height = image_info[2:4]
        name = image_info[7]
        rect = page.get_image_bbox(name)
        size, dpi = _calculate_size(size=(width, height), rect=rect, max_dpi=image_max_dpi)
        image_data = pdf.extract_image(xref)
        temp_image = _reduce_image(BytesIO(image_data.get('image')), size=size, quality=image_quality, dpi=dpi)
        reduced_image_list.append((rect, temp_image))
    return reduced_image_list


def _reduce_image(image_file, size, quality, dpi):
    image = Image.open(image_file)
    try:
        resized_image = image.resize(size)
    except OSError:
        resized_image = image.resize(size)

    fd, temp_file = mkstemp(prefix='pdf_express_tmp', suffix='.jpg')
    resized_image.save(temp_file, format='jpeg', quality=quality, dpi=(dpi, dpi))
    close(fd)
    resized_image.close()
    image.close()
    return temp_file


def _calculate_size(size, rect, max_dpi):
    width, height = size
    rect_width, rect_height = rect.br - rect.tl
    x_dpi = width / rect_width * 72
    y_dpi = height / rect_height * 72
    dpi = min(x_dpi, y_dpi)
    if dpi > max_dpi:
        dpi = max_dpi
    width = int(dpi * rect_width / 72)
    height = int(dpi * rect_height / 72)
    return (width, height), int(dpi)


def merge_compressed_pdf(
        queue: Queue, compressed_pdf_file: Union[str, Path], page_range_list: Union[list, tuple, range]
):
    with Document() as pdf:
        for file_no, page_range in enumerate(page_range_list):
            sub_compressed_pdf_file = TEMP_DIR / f'{file_no}-{compressed_pdf_file.name}'
            with Document(sub_compressed_pdf_file) as sub_compressed_pdf:
                pdf.insert_pdf(sub_compressed_pdf, from_page=page_range[0], to_page=page_range[-1])
            queue.put(file_no)
        pdf.save(compressed_pdf_file, deflate=True)
