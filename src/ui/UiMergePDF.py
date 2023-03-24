from ttkbootstrap import (
    Frame, Labelframe, Treeview, Button,
    Scrollbar, StringVar, Label, Separator, Entry
)


class UiMergePDF(Frame):
    def __init__(self, master=None, **kw):
        super(UiMergePDF, self).__init__(master, **kw)
        self.FramePDFList = Labelframe(self)
        self.TreeViewPDFList = Treeview(self.FramePDFList)
        _columns = ['dir_name', 'file_name']
        _display_columns = ['dir_name', 'file_name']
        self.TreeViewPDFList.configure(columns=_columns, displaycolumns=_display_columns, show='headings')
        self.TreeViewPDFList.column('dir_name', anchor='center', stretch=True, width=150, minwidth=20)
        self.TreeViewPDFList.column('file_name', anchor='center', stretch=True, width=300, minwidth=20)
        self.TreeViewPDFList.heading('dir_name', anchor='center', text='Folder')
        self.TreeViewPDFList.heading(
            'file_name', anchor='center', text='File Name'
        )
        self.TreeViewPDFList.pack(
            expand=True, fill='both', padx=4, pady=4, side='left'
        )
        self.ScrollbarPDFList = Scrollbar(self.FramePDFList)
        self.ScrollbarPDFList.configure(orient='vertical')
        self.ScrollbarPDFList.pack(fill='y', pady=4, side='left')
        self.PDFListButtonFrame = Frame(self.FramePDFList)
        self.PDFListButtonFrame.configure(height=200)
        self.ButtonAddPDF = Button(self.PDFListButtonFrame)
        self.ButtonAddPDF.configure(text='Add PDF')
        self.ButtonAddPDF.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonAddPDF.configure(command=self.add_pdf)
        self.ButtonRemovePDF = Button(self.PDFListButtonFrame)
        self.ButtonRemovePDF.configure(text='Remove PDF')
        self.ButtonRemovePDF.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonRemovePDF.configure(command=self.remove_pdf)
        self.ButtonRemoveAll = Button(self.PDFListButtonFrame)
        self.ButtonRemoveAll.configure(text='Remove All')
        self.ButtonRemoveAll.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonRemoveAll.configure(command=self.remove_all)
        self.Separator = Separator(self.PDFListButtonFrame)
        self.Separator.configure(orient='horizontal')
        self.Separator.pack(fill='x', padx=2, pady='8', side='top')
        self.ButtonMoveTop = Button(self.PDFListButtonFrame)
        self.ButtonMoveTop.configure(text='Move to First')
        self.ButtonMoveTop.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonMoveTop.configure(command=self.move_top)
        self.ButtonMoveUp = Button(self.PDFListButtonFrame)
        self.ButtonMoveUp.configure(text='Move Up')
        self.ButtonMoveUp.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonMoveUp.configure(command=self.move_up)
        self.ButtonMoveDown = Button(self.PDFListButtonFrame)
        self.ButtonMoveDown.configure(text='Move Down')
        self.ButtonMoveDown.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonMoveDown.configure(command=self.move_down)
        self.ButtonMoveBottom = Button(self.PDFListButtonFrame)
        self.ButtonMoveBottom.configure(text='Move to Last')
        self.ButtonMoveBottom.pack(fill='x', ipadx=2, padx=2, pady=4, side='top')
        self.ButtonMoveBottom.configure(command=self.move_bottom)
        self.PDFListButtonFrame.pack(
            expand="false", fill="y", padx=6, side="right"
        )
        self.FramePDFList.configure(text='PDF List')
        self.FramePDFList.pack(expand=True, fill='both', padx=4, pady=4, side='top')
        self.FrameMergedPDFFile = Labelframe(self)
        self.EntryMergedPDFFile = Entry(self.FrameMergedPDFFile)
        self.merged_pdf_file = StringVar()
        self.EntryMergedPDFFile.configure(state='readonly', textvariable=self.merged_pdf_file)
        self.EntryMergedPDFFile.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonMergedPDFFile = Button(self.FrameMergedPDFFile, width=10)
        self.ButtonMergedPDFFile.configure(text='Browser')
        self.ButtonMergedPDFFile.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonMergedPDFFile.configure(command=self.set_merged_pdf_file)
        self.FrameMergedPDFFile.configure(height=200, text='Merged PDF File', width=200)
        self.FrameMergedPDFFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar()
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.LabelProcessInfo.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=10)
        self.ButtonProcess.configure(state='disabled', text='Merge')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='Merge PDF', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def add_pdf(self):
        pass

    def remove_pdf(self):
        pass

    def remove_all(self):
        pass

    def move_top(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

    def move_bottom(self):
        pass

    def set_merged_pdf_file(self):
        pass

    def process(self):
        pass
