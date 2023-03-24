from __future__ import annotations

from re import compile
from os import mkdir
from os.path import exists
from pathlib import Path
from tkinter.filedialog import askopenfilename, askopenfilenames
from ttkbootstrap import Treeview
from ttkbootstrap.dialogs import Messagebox, MessageDialog
from ttkbootstrap.tooltip import ToolTip

from fitz import Document
from ttkbootstrap.icons import Icon

from constants import BYTE_UNIT, FILE_TYPES_PDF


class TMessagebox(Messagebox):
    @staticmethod
    def show_error(message, title=" ", parent=None, alert=True, **kwargs):
        if kwargs.get('localize', None):
            localize = kwargs.get('localize')
        else:
            localize = False
        dialog = MessageDialog(
            message=message,
            title=title,
            parent=parent,
            buttons=["OK:primary"],
            icon=Icon.error,
            alert=alert,
            localize=localize,
            **kwargs,
        )
        if "position" in kwargs:
            position = kwargs.pop("position")
        else:
            position = None
        dialog.show(position)

    @staticmethod
    def okcancel(message, title=" ", alert=False, parent=None, **kwargs):
        localize = kwargs.get('localize') if kwargs.get('localize', None) else False
        dialog = MessageDialog(
            title=title,
            message=message,
            parent=parent,
            alert=alert,
            localize=localize,
            **kwargs,
        )
        position = kwargs.pop("position") if "position" in kwargs else None
        dialog.show(position)
        return dialog.result


def int2byte_unit(value: int):
    index = 0
    while value > 1024 and index < 8:
        value /= 1024
        index += 1
    return f'{round(value)}{BYTE_UNIT[index]}B'


def show_tooltip(widget, message=''):
    ToolTip(widget, text=message or 'You can drag files here')


def pdf_info(pdf_file):
    # page_count = 0
    with Document(pdf_file) as pdf:
        page_count = pdf.page_count
    pdf_file = Path(pdf_file)
    return pdf_file, page_count, len(str(page_count))


def get_pdf_info(title='Select PDF file', filetypes=FILE_TYPES_PDF):
    if pdf_file := askopenfilename(title=title, filetypes=filetypes):
        return pdf_info(pdf_file)


def check_file_exist(file_path: Path):
    if not file_path.exists():
        TMessagebox.show_error(title='File not exist.', message=f'{file_path}\nFile not exist, please check.')

        return False
    return True


def check_dir(dir_path: Path | str):
    if isinstance(dir_path, Path):
        if not dir_path.exists():
            dir_path.mkdir()
    elif not exists(dir_path):
        mkdir(dir_path)


def treeview_add_files(treeview: Treeview, title, filetypes):
    file_list = askopenfilenames(title=title, filetypes=filetypes)
    for file in file_list:
        file_path = Path(file)
        treeview.insert('', 'end', text=str(file_path), values=(file_path.parent, file_path.name))


def get_filelist(title, filetypes):
    return askopenfilenames(title=title, filetypes=filetypes)


def treeview_move_item(treeview: Treeview, position: str):
    item_list = treeview.get_children()
    item_count = len(item_list)
    selected_list = treeview.selection()
    selected_count = len(selected_list)
    if item_count == 1 or selected_count != 1:
        return None
    selected_item = selected_list[0]
    index = item_list.index(selected_item)
    if position == 'top':
        new_index = 0
    elif position == 'bottom':
        new_index = 'end'
    elif position == 'up':
        new_index = index - 1
    elif position == 'down':
        new_index = index + 1
    else:
        return None
    treeview.move(selected_item, '', new_index)


def treeview_remove_items(treeview, remove_all=False):
    item_list = treeview.get_children() if remove_all else treeview.selection()
    treeview.delete(*item_list)


def treeview_get_file_list(treeview: Treeview, is_winPath=True):
    file_list = []
    for item in treeview.get_children():
        file_path = treeview.item(item, 'text')
        if is_winPath:
            file_list.append(Path(file_path))
        else:
            file_list.append(file_path)
    return file_list


def treeview_get_first_file(treeview: Treeview):
    # sourcery skip: assign-if-exp, use-named-expression
    file_list = treeview_get_file_list(treeview)
    if file_list:
        return file_list[0]
    else:
        return ''


def split_drop_data(data):
    file_list = []
    pattern = compile(r'\{([^\{\}]+)\}|(\S+)')
    for match in pattern.findall(data):
        file_name = match[0] or match[1]
        file_name = Path(file_name)
        if file_name.is_file():
            file_list.append(file_name)
    return file_list


def treeview_drop_files(treeview, file_list, file_type):
    for file in file_list:
        if file.suffix.lower() in file_type[0][1]:
            treeview.insert(
                '', 'end', text=file, values=(file.parent, file.name)
            )


def formatrow(rowdata):
    for index, item in enumerate(rowdata):
        if '\n' in item:
            rowdata[index] = item.replace('\n', '')
    return rowdata
