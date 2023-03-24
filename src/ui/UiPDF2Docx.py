from ttkbootstrap import (
    Frame, Labelframe, Treeview, Button,
    Scrollbar, StringVar, Label, Separator, 
    Entry, Checkbutton, BooleanVar
)


class UiPDF2Docx(Frame):
    def __init__(self, master=None, **kw):
        super(UiPDF2Docx, self).__init__(master, **kw)
        self.FramePDFList = Labelframe(self)
        self.FramePDFList.configure(text='PDF List')
        self.TreeViewPDFList = Treeview(self.FramePDFList)
        self.TreeViewPDFList.configure(
            height=5, selectmode="extended", show="headings")
        self.TreeViewPDFList_cols = ['file_name', 'pdf_page']
        self.TreeViewPDFList_dcols = ['file_name', 'pdf_page']
        self.TreeViewPDFList.configure(
            columns=self.TreeViewPDFList_cols,
            displaycolumns=self.TreeViewPDFList_dcols)
        self.TreeViewPDFList.column(
            "file_name",
            anchor="w",
            stretch="true",
            width=400,
            minwidth=20)
        self.TreeViewPDFList.column(
            "pdf_page",
            anchor="center",
            stretch="true",
            width=150,
            minwidth=20)
        self.TreeViewPDFList.heading(
            "file_name", anchor="center", text='File Name')
        self.TreeViewPDFList.heading(
            "pdf_page", anchor="center", text='PDF Pages')
        self.TreeViewPDFList.pack(
            expand="true",
            fill="both",
            padx=4,
            pady=4,
            side="left")
        self.ScrollbarPDFList = Scrollbar(self.FramePDFList)
        self.ScrollbarPDFList.configure(orient="vertical")
        self.ScrollbarPDFList.pack(fill="y", pady=4, side="left")
        self.PDFListButtonFrame = Frame(self.FramePDFList)
        self.PDFListButtonFrame.configure()
        self.ButtonAddPDF = Button(self.PDFListButtonFrame)
        self.ButtonAddPDF.configure(text='Add PDF')
        self.ButtonAddPDF.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonAddPDF.configure(command=self.add_pdf)
        self.ButtonRemovePDF = Button(self.PDFListButtonFrame)
        self.ButtonRemovePDF.configure(text='Remove PDF')
        self.ButtonRemovePDF.pack(
            fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonRemovePDF.configure(command=self.remove_pdf)
        self.ButtonRemoveAll = Button(self.PDFListButtonFrame)
        self.ButtonRemoveAll.configure(text='Remove All')
        self.ButtonRemoveAll.pack(
            fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonRemoveAll.configure(command=self.remove_all)
        self.Separator = Separator(self.PDFListButtonFrame)
        self.Separator.configure(orient="horizontal")
        self.Separator.pack(fill="x", padx=4, pady=8, side="top")
        self.ButtonMoveUp = Button(self.PDFListButtonFrame)
        self.ButtonMoveUp.configure(text='Move Up')
        self.ButtonMoveUp.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonMoveUp.configure(command=self.move_up)
        self.ButtonMoveDown = Button(self.PDFListButtonFrame)
        self.ButtonMoveDown.configure(text='Move Down')
        self.ButtonMoveDown.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonMoveDown.configure(command=self.move_down)
        self.PDFListButtonFrame.pack(
            expand="false", fill="y", padx=6, side="right")
        self.FramePDFList.pack(
            expand="true",
            fill="both",
            padx=4,
            pady=4,
            side="top")
        self.FramePDFFile = Labelframe(self)
        self.FramePDFFile.configure(text='Converted Docx Folder')
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.docx_dir = StringVar()
        self.EntryPDFFile.configure(
            state="readonly",
            textvariable=self.docx_dir)
        self.EntryPDFFile.pack(
            expand="true",
            fill="x",
            padx=4,
            pady=4,
            side="left")
        self.ButtonPDFFile = Button(self.FramePDFFile)
        self.ButtonPDFFile.configure(text='Browser', state='disabled')
        self.ButtonPDFFile.pack(ipadx=2, padx=4, pady=4, side="left")
        self.ButtonPDFFile.configure(command=self.get_docx_folder)
        self.CheckbuttonSourceFileFolder = Checkbutton(self.FramePDFFile)
        self.use_source_folder = BooleanVar(value=True)
        self.CheckbuttonSourceFileFolder.configure(
            text='Source Folder', variable=self.use_source_folder)
        self.CheckbuttonSourceFileFolder.pack(
            ipadx=2, padx=4, pady=2, side="right")
        self.CheckbuttonSourceFileFolder.configure(
            command=self.set_source_folder)
        self.FramePDFFile.pack(fill="x", padx=4, pady=4, side="top")
        self.FrameConvert = Labelframe(self)
        self.FrameConvert.configure(text='PDF To Docx')
        self.ButtonProcess = Button(self.FrameConvert)
        self.ButtonProcess.configure(
            state="disabled", text='Convert', width=11)
        self.ButtonProcess.pack(anchor="center", padx=4, pady=4, side="right")
        self.ButtonProcess.configure(command=self.process)
        self.FrameConvert.pack(
            expand="false",
            fill="x",
            padx=4,
            pady=4,
            side="top")
        # self.configure(height=200, width=300)

    def add_pdf(self):
        pass

    def remove_pdf(self):
        pass

    def remove_all(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def get_docx_folder(self):
        pass

    def set_source_folder(self):
        pass

    def process(self):
        pass

