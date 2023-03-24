from __future__ import annotations

from os.path import join, split
from pathlib import Path

from pdfplumber import open as _open
from typing import List
from multiprocessing import Process, Queue
from tkinter.filedialog import askdirectory
from ui.UiPDF2Docx import UiPDF2Docx
from constants import FILE_TYPES_PDF
from pdf2docx import Converter
from app.Progress import Progress

from utils.DndDrop import DndDrop
from utils.util import (
    check_dir, check_file_exist, split_drop_data,
    treeview_add_files, treeview_drop_files,
    treeview_get_file_list, treeview_move_item,
    treeview_remove_items,  show_tooltip,
    TMessagebox, treeview_get_first_file,
    pdf_info, get_filelist
)


class PDF2Docx(UiPDF2Docx, DndDrop):
    def __init__(self, master=None, **kw):
        super(PDF2Docx, self).__init__(master, **kw)
        show_tooltip(self.TreeViewPDFList)

        self.TreeViewPDFList.configure(show='headings')
        self._pdf_count: int = 0
        self._pdf_info_list: List = []
        self._docx_dir: str | Path = ''
        # self.app_info = StringVar()
        self._use_sfld = self.use_source_folder.get()
        self.TreeViewPDFList.configure(yscrollcommand=self.ScrollbarPDFList.set)
        self.ScrollbarPDFList.configure(command=self.TreeViewPDFList.yview)
        self.drop()

    def drop_file(self, event):
        file_list = split_drop_data(event.data)
        self.treeview_drop_files(
            self.TreeViewPDFList, 
            file_list, 
            FILE_TYPES_PDF
        )
        self._toggle_button()

    def set_treeview(self, treeview, file):
        self._pdf_file, self._page_count, self._page_no_width = pdf_info(file)
        treeview.insert('', 'end', text=file, values=(file.parent / file.name, self._page_count))

    def treeview_drop_files(self, treeview, file_list, file_type):
        for file in file_list:
            if file.suffix.lower() in file_type[0][1]:
                self.set_treeview(treeview, file)
    
    def treeview_add_files(self, treeview, title, filetypes):
        file_list = get_filelist(title, filetypes)
        for file in file_list:
            file = Path(file)
            self.set_treeview(treeview, file)

    def add_pdf(self):
        self.treeview_add_files(
            self.TreeViewPDFList, 
            title='Select PDF files', 
            filetypes=FILE_TYPES_PDF
        )
        self._toggle_button()

    def remove_pdf(self):
        treeview_remove_items(self.TreeViewPDFList)
        self._toggle_button()

    def remove_all(self):
        treeview_remove_items(self.TreeViewPDFList, remove_all=True)
        self._toggle_button()

    # def move_top(self):
    #     treeview_move_item(self.TreeViewPDFList, 'top')

    # def move_bottom(self):
    #     treeview_move_item(self.TreeViewPDFList, 'bottom')

    def move_up(self):
        treeview_move_item(self.TreeViewPDFList, 'up')

    def move_down(self):
        treeview_move_item(self.TreeViewPDFList, 'down')

    def set_source_folder(self):
        self._use_sfld = self.use_source_folder.get()
        if self._use_sfld:
            self.ButtonPDFFile.configure(state='disabled')
            if self._pdf_count > 0:
                self._docx_dir = Path(treeview_get_first_file(self.TreeViewPDFList)).parent
            else:
                self._docx_dir = ''
            self._set_docx_folder()
        else:
            self.ButtonPDFFile.configure(state='normal')

    def get_docx_folder(self):
        # pass
        self._docx_dir = askdirectory(title='Select Docx folder')
        if self._docx_dir:
            self._docx_dir = Path(self._docx_dir)
        self._set_docx_folder()
        self._toggle_button()

    def _toggle_button(self):
        self._pdf_count = len(self.TreeViewPDFList.get_children())
        self.set_source_folder()
        if self._pdf_count > 0: #  and self._docx_dir:
            # self.ButtonPDFFile.configure(state='normal')
            self.CheckbuttonSourceFileFolder.configure(state='normal')
            self.ButtonProcess.configure(state='normal')
        else:
            # self.ButtonPDFFile.configure(state='disabled')
            self.CheckbuttonSourceFileFolder.configure(state='disabled')
            self.ButtonProcess.configure(state='disabled')

    def _set_docx_folder(self):
        self.docx_dir.set(self._docx_dir)


    def process(self):
        self.ButtonProcess.configure(state='disabled')
        # noinspection PyBroadException
        try:
            pdf_list = treeview_get_file_list(self.TreeViewPDFList)
            for pdf_file in pdf_list:
                if not check_file_exist(pdf_file):
                    return None
            check_dir(self._docx_dir.parent)
        
            queue = Queue()
            sub_process = Process(target=process_pdf2docx, args=(queue, pdf_list, self._docx_dir))
            sub_process_list = [sub_process]
            sub_process.start()
            progress = Progress(process_list=sub_process_list, queue=queue, maximum=self._pdf_count)
            self.wait_window(progress)
        except Exception as e:
            print(e)
            TMessagebox.show_error("File convert failed", "PDF Convert")
        finally:
            self.ButtonProcess.configure(state='normal')


def process_pdf2docx(task_queue: Queue,  pdf_list: List[str | Path], docx_dir: Path):
    # from pdf2docx import Converter
    for pdf_no, pdf_file in enumerate(pdf_list, start=1):
        sp = split(str(pdf_file))
        docx_file = sp[-1].replace('pdf', 'docx')
        docx_file = join(docx_dir, docx_file)
        # convert pdf to docx
        # noinspection PyBroadException
        try:
            cv = Converter(pdf_file)
            cv.convert(docx_file, multi_processing=False)      # all pages by default
            cv.close()
            task_queue.put(pdf_no)
        except Exception as e:
            print(e)
            TMessagebox.show_error(e, "PDF Convert")