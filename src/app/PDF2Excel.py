from __future__ import annotations

from os.path import join, split
from pathlib import Path

from pdfplumber import open as _open
from typing import List
from multiprocessing import Process, Queue
from tkinter.filedialog import askdirectory
from ui.UiPDF2Excel import UiPDF2Excel
from constants import FILE_TYPES_PDF
from app.Progress import Progress

from utils.DndDrop import DndDrop
from utils.excel import addExcel, writeExcel
from utils.util import (
    check_dir, check_file_exist, split_drop_data,
    treeview_add_files, treeview_drop_files,
    treeview_get_file_list, treeview_move_item,
    treeview_remove_items,  show_tooltip,
    TMessagebox, treeview_get_first_file
)


class PDF2Excel(UiPDF2Excel, DndDrop):
    def __init__(self, master=None, **kw):
        super(PDF2Excel, self).__init__(master, **kw)
        show_tooltip(self.TreeViewPDFList)

        self.TreeViewPDFList.configure(show='headings')
        self._pdf_count: int = 0
        self._pdf_info_list: List = []
        self._excel_dir: str | Path = ''
        self._use_source_folder = self.use_source_folder.get()
        self._all_pages_to_one_sheet = self.all_pages_to_one_sheet.get()
        self._all_tables_per_page_to_one_sheet = self.all_tables_per_page_to_one_sheet.get()
        self.TreeViewPDFList.configure(yscrollcommand=self.ScrollbarPDFList.set)
        self.ScrollbarPDFList.configure(command=self.TreeViewPDFList.yview)
        self.drop()

    def drop_file(self, event):
        file_list = split_drop_data(event.data)
        treeview_drop_files(self.TreeViewPDFList, file_list, FILE_TYPES_PDF)
        self._toggle_pdfinfo_button()

    def add_pdf(self):
        treeview_add_files(self.TreeViewPDFList, title='Select PDF files', filetypes=FILE_TYPES_PDF)
        self._toggle_pdfinfo_button()

    def remove_pdf(self):
        treeview_remove_items(self.TreeViewPDFList)
        self._toggle_pdfinfo_button()

    def remove_all(self):
        treeview_remove_items(self.TreeViewPDFList, remove_all=True)
        self._toggle_pdfinfo_button()

    # def move_top(self):
    #     treeview_move_item(self.TreeViewPDFList, 'top')

    # def move_bottom(self):
    #     treeview_move_item(self.TreeViewPDFList, 'bottom')

    def move_up(self):
        treeview_move_item(self.TreeViewPDFList, 'up')

    def move_down(self):
        treeview_move_item(self.TreeViewPDFList, 'down')

    def set_source_folder(self):
        self._use_source_folder = self.use_source_folder.get()
        if self._use_source_folder:
            self.ButtonPDFFile.configure(state='disabled')
            if self._pdf_count > 0:
                self._excel_dir = Path(treeview_get_first_file(self.TreeViewPDFList)).parent
            else:
                self._excel_dir = ''
            self._set_excel_folder()
        else:
            self.ButtonPDFFile.configure(state='normal')

    def check_all_pages_to_one_sheet(self):
        self._toggle_output_select_option()
        if self._all_tables_per_page_to_one_sheet and self._all_pages_to_one_sheet:
            TMessagebox.show_error(
                "Can't select \"All page's table to one sheet\" option!\n"
                "Because option \"All tables of per page to one sheet\" is selected.",
                "Select Error"
            )
            self.all_pages_to_one_sheet.set(False)
            self._toggle_output_select_option()

    def check_all_tables_per_page_to_one_sheet(self):
        self._toggle_output_select_option()
        if self._all_tables_per_page_to_one_sheet and self._all_pages_to_one_sheet:
            TMessagebox.show_error(
                "Can't select \"All tables of per page to one sheet\" option!\n"
                "Because option \"All page's table to one sheet\" is selected.",
                "Select Error"
            )
            self.all_tables_per_page_to_one_sheet.set(False)
            self._toggle_output_select_option()

    def get_pdf_info(self):
        pdf_list = treeview_get_file_list(self.TreeViewPDFList)
        for pdf_file in pdf_list:
            if not check_file_exist(pdf_file):
                return None
        check_dir(self._excel_dir)

        task_queue = Queue()

        sub_process = Process(
            target=process_getpdf_info,
            args=(task_queue, pdf_list, )
        )
        sub_process_list = [sub_process]
        sub_process.start()
        progress = Progress(process_list=sub_process_list, queue=task_queue, maximum=len(pdf_list))
        self.wait_window(progress)
        data = progress.data
        # noinspection PyBroadException
        try:
            for item in data:
                _path = item[0]
                if _path not in self._pdf_info_list:
                    self._pdf_info_list.append(item)
            self._set_pdf_info()
        except Exception as _:
            TMessagebox.show_error("File parse failed.", "Parse Failure")

    def get_excel_folder(self):
        self._excel_dir = askdirectory(title='Select excel folder')
        if self._excel_dir:
            self._excel_dir = Path(self._excel_dir)
        self._set_excel_folder()
        self._toggle_pdfinfo_button()

    def process(self):
        self.ButtonProcess.configure(state='disabled')
        self.ButtonReadPDFInfo.configure(state='disabled')
        # noinspection PyBroadException
        try:
            if self._all_pages_to_one_sheet:
                """所有的表格都转换为一个表格"""
                # 循环每一个PDF文件，每个PDF文件包含一个或多页PDF
                for _all_index, pdf_item in enumerate(self._pdf_info_list):
                    table_size = pdf_item[len(pdf_item) - 1]
                    if table_size:
                        _table_list = []
                        # 循环每一页PDF文件，每页PDF文件是包含多个表格，每个表格是一个2维list，每一页PDF是一个3维list
                        for _table_index, p_tables in enumerate(pdf_item[2]):
                            # 循环每一页PDF所有表格
                            for _table in p_tables:
                                _table_list.extend(_table)
                        # _file = join(self._excel_dir, split(str(pdf_item[0]))[-1].replace('.pdf', '.xlsx'))
                        _file = self.get_savename(pdf_item)
                        # writer = ExcelWriter(_file)
                        # df = DataFrame(_table_list)
                        # df.to_excel(
                        #     writer, sheet_name='Sheet1',
                        #     index=False, header=False
                        # )
                        # writer.save()
                        writeExcel(_file, _table_list, 'Sheet')
            elif self._all_tables_per_page_to_one_sheet:
                # 循环每一个PDF文件，每个PDF文件包含一个或多页PDF
                for _all_index, pp_table in enumerate(self._pdf_info_list):
                    _table_list = []
                    # 循环每一页PDF文件，每页PDF文件是包含多个表格，每个表格是一个2维list，每一页PDF是一个3维list
                    _table_size = pp_table[-1]
                    if _table_size:
                        for _table_index, p_tables in enumerate(pp_table[2]):
                            _table_tmp = []
                            # 循环每一页PDF的表格
                            for _table in p_tables:
                                _table_tmp.extend(_table)
                            _table_list.append(_table_tmp)
                        # _file = join(self._excel_dir, split(str(pp_table[0]))[-1].replace('.pdf', '.xlsx'))
                        _file = self.get_savename(pp_table)
                        # writer = ExcelWriter(_file)
                        for _index, _table in enumerate(_table_list, start=1):
                            # df = DataFrame(_table)
                            sheet = f'Sheet{_index}'
                            if _index == 1:
                                writeExcel(_file, _table, sheet=sheet)
                            else:
                                addExcel(_file, _table, sheet=sheet)
                            # df.to_excel(
                            #     writer, sheet_name='Sheet{}'.format(_index),
                            #     index=False, header=False
                            # )
                        # writer.save()
            else:
                for item in self._pdf_info_list:
                    table_size = item[len(item) - 1]
                    if table_size:
                        # _file = join(self._excel_dir, split(str(item[0]))[-1].replace('.pdf', '.xlsx'))
                        _file = self.get_savename(item)
                        # writer = ExcelWriter(_file)
                        table_list_combined = item[2]
                        for table_index, table_list in enumerate(table_list_combined, start=1):
                            for sheet_index, table in enumerate(table_list, start=1):
                                for index, line in enumerate(table):
                                    table[index] = line
                                sheet = f'Sheet{table_index}{sheet_index}'
                                # print(table_index, sheet_index, sheet, table)
                                if table_index == 1 and sheet_index == 1:
                                    writeExcel(_file, table, sheet=sheet)
                                else:
                                    addExcel(_file, table, sheet=sheet)
                                # df = DataFrame(table)
                                # df.to_excel(
                                #     writer, sheet_name=f'Sheet{table_index + 1}{sheet_index + 1}',
                                #     index=False, header=False
                                # )
                        # writer.save()
            TMessagebox.show_info('File converted', 'PDF Convert')
        except Exception as e:
            print(e)
            TMessagebox.show_error("File convert failed", "PDF Convert")
        finally:
            self.ButtonProcess.configure(state='normal')
            self.ButtonReadPDFInfo.configure(state='normal')

    def _set_pdf_info(self):
        _check_table_page_number = 0
        treeview_remove_items(self.TreeviewPDFInfoList, remove_all=True)
        # noinspection PyBroadException
        try:
            # Fist loop, ergodic each pdf file
            for _each_pdf_file_pages_index, item in enumerate(self._pdf_info_list):
                "An item means all tables in the pdf file."
                _pdf_filename = item[0]
                _pdf_pages = item[1]
                _tables = item[2]
                table_num, _check_tables = check_table(_tables)
                _check_table_page_number += table_num
                self._pdf_info_list[_each_pdf_file_pages_index].append(table_num)
                self.TreeviewPDFInfoList.insert(
                    '', 'end', text=str(_pdf_filename),
                    values=(_pdf_filename, _pdf_pages, table_num)
                )
                self._pdf_info_list[_each_pdf_file_pages_index] = [_pdf_filename, _pdf_pages, _check_tables, table_num]

            if _check_table_page_number:
                self.ButtonProcess.configure(state='normal')
            else:
                self.ButtonProcess.configure(state='disabled')
        except Exception as e:
            print(2, e)

    def _toggle_output_select_option(self):
        self._all_pages_to_one_sheet = self.all_pages_to_one_sheet.get()
        self._all_tables_per_page_to_one_sheet = self.all_tables_per_page_to_one_sheet.get()

    def _toggle_pdfinfo_button(self):
        self._pdf_count = len(self.TreeViewPDFList.get_children())
        self.set_source_folder()
        if self._pdf_count > 0: #  and self._excel_dir:
            self.ButtonReadPDFInfo.configure(state='normal')
        else:
            self.ButtonReadPDFInfo.configure(state='disabled')

        if self._pdf_info_list:
            _pdf_list = treeview_get_file_list(self.TreeViewPDFList)
            if not _pdf_list:
                self._pdf_info_list.clear()
            else:
                _cache_files = [item[0] for item in self._pdf_info_list]
                _index_list = []
                for _index, _cf in enumerate(_cache_files):
                    if _cf not in _pdf_list:
                        _index_list.append(_index)
                for _index in _index_list:
                    self._pdf_info_list.remove(self._pdf_info_list[_index])
            self._set_pdf_info()

    def _set_excel_folder(self):
        self.excel_dir.set(self._excel_dir)

    def get_savename(self, item):
        return join(self._excel_dir, split(str(item[0]))[-1].replace('.pdf', '.xlsx'))


def check_table(table_list_combined: List):
    """
    Checked how many available tables in each pdf files.
    The structure of the @table_list_combined should be:
    page_table likes:
    [
        [
            [
                [elem, elem, ...], [elem, elem, ...],
                [elem, elem, ...], [elem, elem, ...]
            ],
            [
                [elem, elem, ...], [elem, elem, ...],
                [elem, elem, ...], [elem, elem, ...]
            ],
            ...
        ],
        [
            [
                [elem, elem, ...], [elem, elem, ...],
                [elem, elem, ...], [elem, elem, ...]
            ],
            [
                [elem, elem, ...], [elem, elem, ...],
                [elem, elem, ...], [elem, elem, ...]
            ],
            ...
        ],
        ...
    ]
    which is a four dimension list
    :param table_list_combined: all pages' tables
    :return: checked tables
    """
    table_size = 0
    _checked_table = []

    # Fist loop, ergodic each page of the pdf file
    for table_list_index, table_list in enumerate(table_list_combined):
        _each_page_tables = []
        if table_list:
            """
            A table_list should be:
            [
                [
                    [elem, elem, ...], [elem, elem, ...],
                    [elem, elem, ...], [elem, elem, ...]
                ],
                [
                    [elem, elem, ...], [elem, elem, ...],
                    [elem, elem, ...], [elem, elem, ...]
                ],
                ...
            ],
            """
            # Second loop, ergodic each page,
            # each page has one or more table
            for table in table_list:
                _is_table_empty = True
                if table:
                    """
                    A table should be:
                    [
                        [elem, elem, ...], [elem, elem, ...],
                        [elem, elem, ...], [elem, elem, ...]
                    ],
                    """
                    # loop each line in the table
                    # formatted None value and empty and special char
                    # of each item in each line
                    # then replace it with a user readable char
                    # finally check each table if is an available table.
                    for table_index, _line in enumerate(table):
                        _not_empty_line, _line = check_table_line(_line)
                        # print(_emptyed, _line)
                        if _is_table_empty and _not_empty_line:
                            _is_table_empty = False
                        table[table_index] = _line

                    if not _is_table_empty:
                        _each_page_tables.append(table)
                        table_size += 1
            if _each_page_tables:
                _checked_table.append(_each_page_tables)
    return table_size, _checked_table


def check_table_line(line: List[str]):
    try:
        if not line:
            # print(f'None value: {line}')
            return 0, None
        for index, item in enumerate(line):
            if not item:
                line[index] = ''
            if item and '\n' in item:
                item = item.replace('\n', '')
                line[index] = item
        return any(line), line
    except Exception as e:
        print('Failed to check line: ', e)
        return False, None


def process_getpdf_info(task_queue: Queue,  pdf_list: List[str]):
    for _, pdf_file in enumerate(pdf_list, start=1):
        _tmp_pdf_info_item = [pdf_file, ]
        with _open(pdf_file) as pdf:
            _pages = pdf.pages
            _tmp_pdf_info_item.append(len(_pages))
            _per_table = []
            for i, page in enumerate(_pages):
                _tables = page.extract_tables()
                _per_table.append(_tables)
            _tmp_pdf_info_item.append(_per_table)

            pdf.close()
        task_queue.put(_tmp_pdf_info_item)
