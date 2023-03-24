from platform import version as pversion
from platform import system as psystem

from multiprocessing import freeze_support
from collections import namedtuple
from ttkbootstrap import Window
from ttkbootstrap import (
    Frame, BOTH, TOP, X, Button, StringVar,
    PhotoImage, Menu, Style, VERTICAL, Separator
)
from ttkbootstrap.tooltip import ToolTip
from tkinterdnd2 import TkinterDnD
from constants import APP_ICON, TOOLBAR_BUTTON

from app.About import About
from app.MergePDF import MergePDF
from app.SplitPDF import SplitPDF
from app.RotatePDF import RotatePDF
from app.CompressPDF import CompressPDF
from app.ExtractImages import ExtractImages
from app.ExtractText import ExtractText
from app.PDF2Images import PDF2Images
from app.Images2PDF import Images2PDF
from app.PDF2Excel import PDF2Excel
from app.PDF2Docx import PDF2Docx
from utils.util import TMessagebox


operate = namedtuple('operate', ('widget', 'widget_id'))


class PDFMore(Window, TkinterDnD.Tk):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.img_pdf2excel = None
        self.img_extracttext = None
        self.img_extractimage = None
        self.img_image2pdf = None
        self.img_rotate = None
        self.img_pdf2docx = None
        self.img_pdf2image = None
        self.img_compress = None
        self.img_split = None
        self.pdf2xlsxbtn = None
        self.pdf2docxbtn = None
        self.image2pdf = None
        self.pdf2imagebtn = None
        self.extracttextbtn = None
        self.extractimagebtn = None
        self.compresspdfbtn = None
        self.rotatepdfbtn = None
        self.splitpdfbtn = None
        self.mergepdfbtn = None
        self.ThemeMenu = None
        self.PDFAndImageMenu = None
        self.SystemMenu = None
        self.img_merge = None
        self.theme = None
        self.statusBar = None
        self.PDFAndExcelMenu = None
        self.PDFConvertMenu = None
        self.PDFExtractMenu = None
        self.PDFEditMenu = None
        self.MenuBar = None
        self._current_operate = None
        self.FrameStatus = None
        self.FrameBody = None
        self.FrameToolbar = None
        self._operates = None
        self.bootstyle = {'bootstyle': 'light'}
        self._center()
        # self.protocol('WM_DELETE_WINDOW', self.destroy_window)
        self.iconphoto(False, PhotoImage(file=APP_ICON))
        # self._binding()
        self.create_base_frames()
        self.create_menus()
        self.create_toolbar()
        self.create_operates()

    def create_base_frames(self):
        # resize row 1 and column 0 with window
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        # set minimum height for row 0 and 2
        self.rowconfigure(0, minsize=40)
        self.rowconfigure(2, minsize=30)
        # Toolbar
        self.FrameToolbar = Frame(self, height=40, padding=1, **self.bootstyle)
        self.FrameToolbar.grid(row=0, sticky='ew')

        # Middle
        self.FrameBody = Frame(self, **self.bootstyle)
        self.FrameBody.grid(row=1, sticky='ewsn')

        # Status bar
        self.FrameStatus = Frame(self, height=30, relief='sunken', **self.bootstyle)
        self.FrameStatus.grid(row=2, sticky='ew')

    def create_operates(self):
        self._operates = {
            'MergePDF': operate(MergePDF(master=self.FrameBody), 'Merge PDF'),
            'SplitPDF': operate(SplitPDF(master=self.FrameBody), 'Split PDF'),
            'RotatePDF': operate(RotatePDF(master=self.FrameBody), 'Rotate PDF'),
            'CompressPDF': operate(CompressPDF(master=self.FrameBody), 'Compress PDF'),
            'ExtractImages': operate(ExtractImages(master=self.FrameBody), 'Extract Images'),
            'ExtractText': operate(ExtractText(master=self.FrameBody), 'Extract Text'),
            'PDF2Images': operate(PDF2Images(master=self.FrameBody), 'PDF To Images'),
            'Images2PDF': operate(Images2PDF(master=self.FrameBody), 'Images To PDF'),
            'PDF2Excel': operate(PDF2Excel(master=self.FrameBody), 'PDF To Excel'),
            'PDF2Docx': operate(PDF2Docx(master=self.FrameBody), 'PDF To Docx'),
        }
        self._current_operate = 'MergePDF'
        current_operate = self._operates.get(self._current_operate)
        current_operate.widget.pack(side=TOP, expand=True, fill=BOTH)
        self.updateTitle()

    def create_menus(self):
        self.MenuBar = Menu(self)
        self.config(menu=self.MenuBar)
        # PDF Edit Menu
        self.PDFEditMenu = Menu(self.MenuBar, tearoff=0)
        # add command
        def _w_cmd(wid='MergePDF'): self.set_operate(wid)
        self.PDFEditMenu.add_command(label='Merge PDF', command=_w_cmd)
        def _w_cmd(wid='SplitPDF'): self.set_operate(wid)
        self.PDFEditMenu.add_command(label='Split PDF', command=_w_cmd)
        def _w_cmd(wid='RotatePDF'): self.set_operate(wid)
        self.PDFEditMenu.add_command(label='Rotate PDF', command=_w_cmd)
        def _w_cmd(wid='CompressPDF'): self.set_operate(wid)
        self.PDFEditMenu.add_command(label='Compress PDF', command=_w_cmd)
        self.MenuBar.add_cascade(label='PDF Edit', menu=self.PDFEditMenu)

        # PDF Extract Menu
        self.PDFExtractMenu = Menu(self.MenuBar, tearoff=0)
        def _w_cmd(wid='ExtractImages'): self.set_operate(wid)
        self.PDFExtractMenu.add_command(label='Extract Image', command=_w_cmd)
        def _w_cmd(wid='ExtractText'): self.set_operate(wid)
        self.PDFExtractMenu.add_command(label='Extract Text', command=_w_cmd)
        self.MenuBar.add_cascade(label='PDF Extract', menu=self.PDFExtractMenu)

        # PDF Convert Menu
        self.PDFConvertMenu = Menu(self.MenuBar, tearoff=0)
        # PDF to Excel
        self.PDFAndExcelMenu = Menu(self.PDFConvertMenu, tearoff=0)
        def _w_cmd(wid='PDF2Excel'): self.set_operate(wid)
        self.PDFAndExcelMenu.add_command(label='PDF To Excel', command=_w_cmd)
        # PDF to Docx
        def _w_cmd(wid='PDF2Docx'): self.set_operate(wid)
        self.PDFAndExcelMenu.add_command(label='PDF To Docx', command=_w_cmd)
        self.PDFConvertMenu.add_cascade(label='PDF & Office', menu=self.PDFAndExcelMenu)
        # PDF & Image
        self.PDFAndImageMenu = Menu(self.PDFConvertMenu, tearoff=0)
        def _w_cmd(wid='PDF2Images'): self.set_operate(wid)
        self.PDFAndImageMenu.add_command(label='PDF To Image', command=_w_cmd)
        def _w_cmd(wid='Images2PDF'): self.set_operate(wid)
        self.PDFAndImageMenu.add_command(label='Image To PDF', command=_w_cmd)
        self.PDFConvertMenu.add_cascade(label='PDF & Image', menu=self.PDFAndImageMenu)
        self.MenuBar.add_cascade(label='PDF Converter', menu=self.PDFConvertMenu)

        self.SystemMenu = Menu(self.MenuBar, tearoff=0)
        self.ThemeMenu = Menu(self.SystemMenu, tearoff=0)
        self.setTheme()
        self.SystemMenu.add_cascade(label='Theme', menu=self.ThemeMenu)

        self.SystemMenu.add_command(label='About', command=self.about)
        # self.SystemMenu.add_separator()
        # self.SystemMenu.add_command(label='Exit', command=self.destroy_window, accelerator=self.COMMAND[0][-1])
        self.MenuBar.add_cascade(label='System', menu=self.SystemMenu)

    def create_toolbar(self):
        self.statusBar = Frame(self.FrameToolbar, **self.bootstyle)
        self.statusBar.configure(height=40, width=500)

        self.mergepdfbtn = Button(self.statusBar, **self.bootstyle)
        self.mergepdfbtn.pack(padx=2, side="left")
        ToolTip(self.mergepdfbtn, 'Merge PDF')
        def _wcmd(wid="MergePDF"): self.set_operate(wid)
        self.mergepdfbtn.configure(command=_wcmd)
        separator1 = Separator(self.statusBar)
        separator1.configure(orient=VERTICAL)

        self.splitpdfbtn = Button(self.statusBar, **self.bootstyle)
        self.splitpdfbtn.pack(padx=2, side="left")
        ToolTip(self.splitpdfbtn, 'Split PDF')
        def _wcmd(wid="SplitPDF"): self.set_operate(wid)
        self.splitpdfbtn.configure(command=_wcmd)
        separator2 = Separator(self.statusBar)
        separator2.configure(orient=VERTICAL)

        self.rotatepdfbtn = Button(self.statusBar, **self.bootstyle)
        self.rotatepdfbtn.pack(padx=2, side="left")
        ToolTip(self.rotatepdfbtn, 'Rotate PDF')
        def _wcmd(wid="RotatePDF"): self.set_operate(wid)
        self.rotatepdfbtn.configure(command=_wcmd)
        separator3 = Separator(self.statusBar)
        separator3.configure(orient=VERTICAL)

        self.compresspdfbtn = Button(self.statusBar, **self.bootstyle)
        self.compresspdfbtn.pack(padx=2, side="left")
        ToolTip(self.compresspdfbtn, 'Compress PDF')
        def _wcmd(wid="CompressPDF"): self.set_operate(wid)
        self.compresspdfbtn.configure(command=_wcmd)
        separator4 = Separator(self.statusBar, **self.bootstyle)
        separator4.configure(orient=VERTICAL)

        self.extractimagebtn = Button(self.statusBar, **self.bootstyle)
        self.extractimagebtn.pack(padx=2, side="left")
        ToolTip(self.extractimagebtn, 'Extract images from PDF file')
        def _wcmd(wid="ExtractImages"): self.set_operate(wid)
        self.extractimagebtn.configure(command=_wcmd)
        separator5 = Separator(self.statusBar)
        separator5.configure(orient=VERTICAL)

        self.extracttextbtn = Button(self.statusBar, **self.bootstyle)
        self.extracttextbtn.pack(padx=2, side="left")
        ToolTip(self.extracttextbtn, 'Extract text from PDF file')
        def _wcmd(wid="ExtractText"): self.set_operate(wid)
        self.extracttextbtn.configure(command=_wcmd)
        separator6 = Separator(self.statusBar)
        separator6.configure(orient=VERTICAL)

        self.pdf2imagebtn = Button(self.statusBar, **self.bootstyle)
        self.pdf2imagebtn.pack(padx=2, side="left")
        ToolTip(self.pdf2imagebtn, 'Convert PDF file to images')
        def _wcmd(wid="PDF2Images"): self.set_operate(wid)
        self.pdf2imagebtn.configure(command=_wcmd)
        separator7 = Separator(self.statusBar)
        separator7.configure(orient=VERTICAL)

        self.image2pdf = Button(self.statusBar, **self.bootstyle)
        self.image2pdf.pack(padx=2, side="left")
        ToolTip(self.image2pdf, 'Convert images to PDF file')
        def _wcmd(wid="Images2PDF"): self.set_operate(wid)
        self.image2pdf.configure(command=_wcmd)
        separator9 = Separator(self.statusBar)
        separator9.configure(orient=VERTICAL)

        self.pdf2xlsxbtn = Button(self.statusBar, **self.bootstyle)
        self.pdf2xlsxbtn.pack(padx=2, side="left")
        ToolTip(self.pdf2xlsxbtn, 'Convert PDF file to excel file')
        def _wcmd(wid="PDF2Excel"): self.set_operate(wid)
        self.pdf2xlsxbtn.configure(command=_wcmd)
        separator8 = Separator(self.statusBar)
        separator8.configure(orient=VERTICAL)

        self.pdf2docxbtn = Button(self.statusBar, **self.bootstyle)
        self.pdf2docxbtn.pack(padx=2, side="left")
        ToolTip(self.pdf2docxbtn, 'Convert PDF file to docx file')
        def _wcmd(wid="PDF2Docx"): self.set_operate(wid)
        self.pdf2docxbtn.configure(command=_wcmd)

        self.statusBar.pack(side=TOP, fill=X, expand=True)
        self.setToolbarImage()

    def setToolbarImage(self):
        self.img_merge = PhotoImage(file=TOOLBAR_BUTTON[0])
        self.mergepdfbtn.configure(image=self.img_merge)

        self.img_split = PhotoImage(file=TOOLBAR_BUTTON[1])
        self.splitpdfbtn.configure(image=self.img_split)

        self.img_rotate = PhotoImage(file=TOOLBAR_BUTTON[2])
        self.rotatepdfbtn.configure(image=self.img_rotate)

        self.img_compress = PhotoImage(file=TOOLBAR_BUTTON[3])
        self.compresspdfbtn.configure(image=self.img_compress)

        self.img_extractimage = PhotoImage(file=TOOLBAR_BUTTON[4])
        self.extractimagebtn.configure(image=self.img_extractimage)

        self.img_extracttext = PhotoImage(file=TOOLBAR_BUTTON[5])
        self.extracttextbtn.configure(image=self.img_extracttext)

        self.img_pdf2image = PhotoImage(file=TOOLBAR_BUTTON[6])
        self.pdf2imagebtn.configure(image=self.img_pdf2image)

        self.img_image2pdf = PhotoImage(file=TOOLBAR_BUTTON[7])
        self.image2pdf.configure(image=self.img_image2pdf)

        self.img_pdf2excel = PhotoImage(file=TOOLBAR_BUTTON[8])
        self.pdf2xlsxbtn.configure(image=self.img_pdf2excel)

        self.img_pdf2docx = PhotoImage(file=TOOLBAR_BUTTON[9])
        self.pdf2docxbtn.configure(image=self.img_pdf2docx)

    def set_operate(self, widget_id):
        old_operate = self._operates.get(self._current_operate)
        old_operate.widget.pack_forget()

        self._current_operate = widget_id
        current_operate = self._operates.get(self._current_operate)
        current_operate.widget.pack(side=TOP, expand=True, fill=BOTH)
        self.updateTitle()

    def setTheme(self):
        self.getTheme()
        for theme in self._style.theme_names():
            self.ThemeMenu.add_radiobutton(label=theme, command=self._set_theme, value=theme, variable=self.theme)

    def _set_theme(self):
        self._style.theme_use(self.theme.get())

    def getTheme(self):
        self._style = Style(self.master)
        self.theme = StringVar(value=self._style.theme_use())

    def about(self):
        about_frame = About(None)
        self.wait_window(about_frame)

    def _center(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        width = screen_width * 2 // 3
        height = screen_height * 3 // 4
        screen_height = screen_height * 4 // 4
        left = (screen_width - width) // 2
        top = (screen_height - height) // 2
        self.wm_minsize(width, height)
        self.wm_resizable(True, True)
        self.wm_geometry(f'+{left}+{top}')

    # def _binding(self):
    #     self.bind('<{}>'.format(self.COMMAND[0][0]), self.destroy_window)

    def updateTitle(self, _title=''):
        current_operate = self._current_operate
        op = self._operates.get(current_operate)
        if not _title:
            _title = f'PDFMore-{op.widget_id}'
        self.title(_title)

    def destroy_window(self, _=None):
        """"""
        query = TMessagebox.okcancel('Are you sure to close window?', 'Exit')
        if query and query.lower() in ['确定', 'ok', 'yes']:
            self.destroy()

    def run(self):
        self.mainloop()
        

if __name__ == '__main__':
    freeze_support()

    if psystem() == 'Windows' and int(pversion().split('.')[0]) >= 10:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)

    app = PDFMore()
    app.run()
