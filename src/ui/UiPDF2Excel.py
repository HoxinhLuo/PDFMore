from ttkbootstrap import (
    Frame, Button, Treeview, Labelframe, Scrollbar,
    Separator, Entry, StringVar, Checkbutton, BooleanVar
)


class UiPDF2Excel(Frame):
    def __init__(self, master=None, **kwargs):
        super(UiPDF2Excel, self).__init__(master, **kwargs)
        self.FramePDFList = Labelframe(self)
        self.FramePDFList.configure(text="PDF List")
        self.TreeViewPDFList = Treeview(self.FramePDFList)
        self.TreeViewPDFList.configure(selectmode="extended", show="headings")
        self.TreeviewPDFList_cols = ["ColumnDirName", "ColumnFileName"]
        self.TreeviewPDFList_dcols = ["ColumnDirName", "ColumnFileName"]
        self.TreeViewPDFList.configure(
            columns=self.TreeviewPDFList_cols, displaycolumns=self.TreeviewPDFList_dcols
        )
        self.TreeViewPDFList.column(
            "ColumnDirName", anchor='center', stretch=True, width=200, minwidth=20
        )
        self.TreeViewPDFList.column(
            "ColumnFileName", anchor='center', stretch=True, width=300, minwidth=20
        )
        self.TreeViewPDFList.heading("ColumnDirName", anchor="center", text="Folder")
        self.TreeViewPDFList.heading(
            "ColumnFileName", anchor="center", text="File Name"
        )
        self.TreeViewPDFList.pack(
            expand=True, fill="both", padx=4, pady=4, side="left"
        )
        self.ScrollbarPDFList = Scrollbar(self.FramePDFList)
        self.ScrollbarPDFList.configure(orient="vertical")
        self.ScrollbarPDFList.pack(fill="y", pady=4, side="left")
        self.PDFListButtonFrame = Frame(self.FramePDFList)
        self.PDFListButtonFrame.configure(height=200)
        self.ButtonAddPDF = Button(self.PDFListButtonFrame)
        self.ButtonAddPDF.configure(text="Add PDF")
        self.ButtonAddPDF.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonAddPDF.configure(command=self.add_pdf)
        self.ButtonRemovePDF = Button(self.PDFListButtonFrame)
        self.ButtonRemovePDF.configure(text="Remove PDF")
        self.ButtonRemovePDF.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonRemovePDF.configure(command=self.remove_pdf)
        self.ButtonRemoveAll = Button(self.PDFListButtonFrame)
        self.ButtonRemoveAll.configure(text="Remove All")
        self.ButtonRemoveAll.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonRemoveAll.configure(command=self.remove_all)
        self.Separator = Separator(self.PDFListButtonFrame)
        self.Separator.configure(orient="horizontal")
        self.Separator.pack(fill="x", padx=4, pady=8, side="top")
        # self.ButtonMoveTop = Button(self.FramePDFList)
        # self.ButtonMoveTop.configure(text="Move to First")
        # self.ButtonMoveTop.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        # self.ButtonMoveTop.configure(command=self.move_top)
        self.ButtonMoveUp = Button(self.PDFListButtonFrame)
        self.ButtonMoveUp.configure(text="Move Up")
        self.ButtonMoveUp.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonMoveUp.configure(command=self.move_up)
        self.ButtonMoveDown = Button(self.PDFListButtonFrame)
        self.ButtonMoveDown.configure(text="Move Down")
        self.ButtonMoveDown.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        self.ButtonMoveDown.configure(command=self.move_down)
        # self.ButtonMoveBottom = Button(self.FramePDFList)
        # self.ButtonMoveBottom.configure(text="Move to Last")
        # self.ButtonMoveBottom.pack(fill="x", ipadx=2, padx=4, pady=4, side="top")
        # self.ButtonMoveBottom.configure(command=self.move_bottom)
        self.PDFListButtonFrame.pack(
            expand="false", fill="y", padx=6, side="right"
        )
        self.FramePDFList.pack(expand=True, fill="both", padx=4, pady=4, side="top")

        self.FramePDFFile = Labelframe(self)
        self.FramePDFFile.configure(height=200, text="Converted Excel Folder", width=200)
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.excel_dir = StringVar()
        self.EntryPDFFile.configure(state="readonly", textvariable=self.excel_dir)
        self.EntryPDFFile.pack(expand=True, fill="x", padx=4, pady=4, side="left")
        self.ButtonPDFFile = Button(self.FramePDFFile, width=10)
        self.ButtonPDFFile.configure(text="Browser", state='disabled')
        self.ButtonPDFFile.pack(ipadx=2, padx=8, pady=4, side="left")
        self.ButtonPDFFile.configure(command=self.get_excel_folder)
        self.FramePDFFile.pack(fill="x", padx=4, pady=4, side="top", ipady=8)

        self.CheckbuttonSourceFileFolder = Checkbutton(self.FramePDFFile)
        self.use_source_folder = BooleanVar(value=True)
        self.CheckbuttonSourceFileFolder.configure(
            text="Source Folder", 
            variable=self.use_source_folder,
            # state='disabled'
        )
        self.CheckbuttonSourceFileFolder.pack(ipadx=2, padx=4, pady=2, side="right")
        self.CheckbuttonSourceFileFolder.configure(command=self.set_source_folder)

        self.LabelframeExcelOption = Labelframe(self)
        self.LabelframeExcelOption.configure(
            height=100, text="Convert Option", width=200
        )
        self.CheckbuttonAllPagesToOneSheet = Checkbutton(self.LabelframeExcelOption)
        self.all_pages_to_one_sheet = BooleanVar()
        self.CheckbuttonAllPagesToOneSheet.configure(
            text="All page's table to one sheet", variable=self.all_pages_to_one_sheet
        )
        self.CheckbuttonAllPagesToOneSheet.pack(padx=4, side="left")
        self.CheckbuttonAllPagesToOneSheet.configure(
            command=self.check_all_pages_to_one_sheet
        )
        self.CheckbuttonAllTablesPerageToOneSheet = Checkbutton(self.LabelframeExcelOption)
        self.all_tables_per_page_to_one_sheet = BooleanVar()
        self.CheckbuttonAllTablesPerageToOneSheet.configure(
            text="All tables of per page to one sheet",
            variable=self.all_tables_per_page_to_one_sheet,
        )
        self.CheckbuttonAllTablesPerageToOneSheet.pack(padx=4, side="left")
        self.CheckbuttonAllTablesPerageToOneSheet.configure(
            command=self.check_all_tables_per_page_to_one_sheet
        )
        self.LabelframeExcelOption.pack(fill="x", padx=4, pady=4, side="top", ipady=8)

        self.FrameProcess = Labelframe(self)
        self.FrameProcess.configure(height=200, text="PDF To Excel", width=200)
        self.TreeviewPDFInfoList = Treeview(self.FrameProcess)
        self.TreeviewPDFInfoList.configure(
            height=5, selectmode="extended", show="headings"
        )
        self.TreeviewPDFInfoList_cols = [
            "ColumnPDFFile",
            "ColumnPDFPages",
            "ColumnTableNum",
        ]
        self.TreeviewPDFInfoList_dcols = [
            "ColumnPDFFile",
            "ColumnPDFPages",
            "ColumnTableNum",
        ]
        self.TreeviewPDFInfoList.configure(
            columns=self.TreeviewPDFInfoList_cols,
            displaycolumns=self.TreeviewPDFInfoList_dcols,
        )
        self.TreeviewPDFInfoList.column(
            "ColumnPDFFile", anchor="center", stretch=True, width=300, minwidth=20
        )
        self.TreeviewPDFInfoList.column(
            "ColumnPDFPages", anchor="center", stretch=True, width=100, minwidth=20
        )
        self.TreeviewPDFInfoList.column(
            "ColumnTableNum", anchor="center", stretch=True, width=100, minwidth=20
        )
        self.TreeviewPDFInfoList.heading(
            "ColumnPDFFile", anchor="center", text="PDF File"
        )
        self.TreeviewPDFInfoList.heading(
            "ColumnPDFPages", anchor="center", text="PDF Pages"
        )
        self.TreeviewPDFInfoList.heading(
            "ColumnTableNum", anchor="center", text="Table Num"
        )
        self.TreeviewPDFInfoList.pack(fill="x", padx=4, pady=4, side="left", expand=True)
        self.PDFInfoScrollbar = Scrollbar(self.FrameProcess)
        self.PDFInfoScrollbar.configure(orient="vertical")
        self.PDFInfoScrollbar.pack(fill="y", pady=4, side="left")

        self.FrameOperate = Labelframe(self.FrameProcess)
        self.FrameOperate.configure(height=200, text="Operate", width=200)
        self.ButtonReadPDFInfo = Button(self.FrameOperate)
        self.ButtonReadPDFInfo.configure(state="disabled", text="Analyze PDF", width=11)
        self.ButtonReadPDFInfo.pack(ipadx=2, padx=10, pady=4, side="top")
        self.ButtonReadPDFInfo.configure(command=self.get_pdf_info)
        self.ButtonProcess = Button(self.FrameOperate)
        self.ButtonProcess.configure(state="disabled", text="Convert", width=11)
        self.ButtonProcess.pack(ipadx=2, padx=10, pady=4, side="bottom")
        self.ButtonProcess.configure(command=self.process)
        self.FrameOperate.pack(fill="y", padx=5, side="right")
        self.FrameProcess.pack(fill="x", padx=4, pady=4, side="top")

    def add_pdf(self):
        pass

    def remove_pdf(self):
        pass

    def remove_all(self):
        pass

    # def move_top(self):
    #     pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    # def move_bottom(self):
    #     pass

    def get_excel_folder(self):
        pass

    def process(self):
        pass

    def get_pdf_info(self):
        pass

    def set_source_folder(self):
        pass

    def check_all_pages_to_one_sheet(self):
        pass

    def check_all_tables_per_page_to_one_sheet(self):
        pass
