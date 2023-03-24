from multiprocessing import Process, Queue
# from threading import Thread
# from queue import Queue
from pathlib import Path
from tkinter.filedialog import asksaveasfilename
from typing import List, Union

from fitz import Document
from constants import FILE_TYPES_IMAGE, FILE_TYPES_PDF

from app.Progress import Progress
from ui.UiImages2PDF import UiImages2PDF
from utils.DndDrop import DndDrop
from utils.util import (
    check_dir, check_file_exist, split_drop_data,
    treeview_add_files, treeview_drop_files,
    treeview_get_file_list, treeview_get_first_file,
    treeview_move_item, treeview_remove_items,
    show_tooltip
)


class Images2PDF(UiImages2PDF, DndDrop):
    def __init__(self, master=None, **kw):
        super(Images2PDF, self).__init__(master, **kw)
        show_tooltip(self.TreeViewImageList)

        self.TreeViewImageList.configure(show='headings')
        self._image_count = 0
        self._pdf_file: Union[str, Path] = ''

        self.TreeViewImageList.configure(yscrollcommand=self.ScrollbarImagesList.set)
        self.ScrollbarImagesList.configure(command=self.TreeViewImageList.yview)

        self.drop()

    def drop_file(self, event):
        file_list = split_drop_data(event.data)
        treeview_drop_files(self.TreeViewImageList, file_list, FILE_TYPES_IMAGE)
        self._set_app_info()
        self._toggle_buttons()

    def add_images(self):
        # treeview_add_files(self.TreeViewImageList, title=_('Select images files'), filetypes=FILE_TYPES_IMAGE)
        treeview_add_files(self.TreeViewImageList, title='Select images files', filetypes=FILE_TYPES_IMAGE)
        self._set_app_info()
        self._toggle_buttons()

    def remove_images(self):
        treeview_remove_items(self.TreeViewImageList)
        self._set_app_info()
        self._toggle_buttons()

    def remove_all(self):
        treeview_remove_items(self.TreeViewImageList, remove_all=True)
        self._set_app_info()
        self._toggle_buttons()

    def move_top(self):
        treeview_move_item(self.TreeViewImageList, 'top')

    def move_up(self):
        treeview_move_item(self.TreeViewImageList, 'up')

    def move_down(self):
        treeview_move_item(self.TreeViewImageList, 'down')

    def move_bottom(self):
        treeview_move_item(self.TreeViewImageList, 'bottom')

    def set_pdf_file(self):
        if self._pdf_file:
            initial_file = self._pdf_file.name
        else:
            initial_file = treeview_get_first_file(self.TreeViewImageList)
            if initial_file:
                initial_file = initial_file.with_suffix('.pdf')
                initial_file = initial_file.name
        pdf_file = asksaveasfilename(
                filetypes=FILE_TYPES_PDF,
                defaultextension='.pdf',
                # title=_('Select PDF file'),
                title='Select PDF file',
                initialfile=initial_file
                )
        if pdf_file:
            self._pdf_file = Path(pdf_file)
            self.pdf_file.set(self._pdf_file)

        self._toggle_buttons()

    def process(self):
        image_list = treeview_get_file_list(self.TreeViewImageList)
        for image_file in image_list:
            if not check_file_exist(image_file):
                return None
        check_dir(self._pdf_file.parent)

        queue = Queue()
        sub_process = Process(
                target=images2pdf,
                args=(queue, image_list, self._pdf_file)
                )
        sub_process_list = [sub_process]
        sub_process.start()
        progress = Progress(process_list=sub_process_list, queue=queue, maximum=len(image_list))
        self.wait_window(progress)

    def _set_app_info(self):
        self._image_count = len(self.TreeViewImageList.get_children())
        if self._image_count:
            # info = _('Total Images: {}').format(self._image_count)
            info = 'Total Images: {}'.format(self._image_count)
        else:
            info = ''
        self.process_info.set('')
        self.app_info.set(info)

    def _toggle_buttons(self):
        if self._image_count > 0 and self._pdf_file:
            self.ButtonProcess.configure(state='normal')
        else:
            self.ButtonProcess.configure(state='disabled')


def images2pdf(queue: Queue, image_list: List[Union[str, Path]], pdf_file: Union[str, Path]):
    with Document() as pdf:
        for image_no, image_file in enumerate(image_list, start=1):
            with Document(image_file) as image_doc:
                pdf_bytes = image_doc.convert_to_pdf()
                with Document('images.pdf', stream=pdf_bytes) as image_pdf:
                    pdf.insert_pdf(image_pdf)
            queue.put(image_no)
        pdf.save(pdf_file)
