from ttkbootstrap import (
    Frame, Labelframe, Treeview, Button,
    Scrollbar, StringVar, Label, Separator, Entry,
    Radiobutton, IntVar, BooleanVar, Checkbutton
)


class UiRotatePDF(Frame):
    def __init__(self, master=None, **kw):
        super(UiRotatePDF, self).__init__(master, **kw)
        self.FramePDFList = Labelframe(self)
        self.TreeViewPDFList = Treeview(self.FramePDFList)
        _columns = ['dir_name', 'file_name']
        _display_columns = ['dir_name', 'file_name']
        self.TreeViewPDFList.configure(columns=_columns, displaycolumns=_display_columns, show='headings')
        self.TreeViewPDFList.column('dir_name', anchor='center', stretch=True, width=150, minwidth=20)
        self.TreeViewPDFList.column('file_name', anchor='center', stretch=True, width=300, minwidth=20)
        self.TreeViewPDFList.heading('dir_name', anchor='center', text='Folder')
        self.TreeViewPDFList.heading('file_name', anchor='center', text='File Name')
        self.TreeViewPDFList.pack(expand=True, fill='both', padx=4, pady=4, side='left')
        self.ScrollbarPDFList = Scrollbar(self.FramePDFList)
        self.ScrollbarPDFList.configure(orient='vertical')
        self.ScrollbarPDFList.pack(fill='y', pady=4, side='left')
        self.PDFListButtonFrame = Frame(self.FramePDFList)
        self.PDFListButtonFrame.configure(height=200)
        self.ButtonAddPDF = Button(self.PDFListButtonFrame)
        self.ButtonAddPDF.configure(text='Add PDF')
        self.ButtonAddPDF.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonAddPDF.configure(command=self.add_pdf)
        self.ButtonRemovePDF = Button(self.PDFListButtonFrame)
        self.ButtonRemovePDF.configure(text='Remove PDF')
        self.ButtonRemovePDF.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonRemovePDF.configure(command=self.remove_pdf)
        self.ButtonRemoveAll = Button(self.PDFListButtonFrame)
        self.ButtonRemoveAll.configure(text='Remove All')
        self.ButtonRemoveAll.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonRemoveAll.configure(command=self.remove_all)
        self.Separator = Separator(self.PDFListButtonFrame)
        self.Separator.configure(orient='horizontal')
        self.Separator.pack(fill='x', padx=4, pady='8', side='top')
        self.ButtonMoveTop = Button(self.PDFListButtonFrame)
        self.ButtonMoveTop.configure(text='Move to First')
        self.ButtonMoveTop.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonMoveTop.configure(command=self.move_top)
        self.ButtonMoveUp = Button(self.PDFListButtonFrame)
        self.ButtonMoveUp.configure(text='Move Up')
        self.ButtonMoveUp.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonMoveUp.configure(command=self.move_up)
        self.ButtonMoveDown = Button(self.PDFListButtonFrame)
        self.ButtonMoveDown.configure(text='Move Down')
        self.ButtonMoveDown.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonMoveDown.configure(command=self.move_down)
        self.ButtonMoveBottom = Button(self.PDFListButtonFrame)
        self.ButtonMoveBottom.configure(text='Move to Last')
        self.ButtonMoveBottom.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonMoveBottom.configure(command=self.move_bottom)
        self.PDFListButtonFrame.pack(
            expand="false", fill="y", padx=6, side="right"
        )
        self.FramePDFList.configure(text='PDF List')
        self.FramePDFList.pack(expand=True, fill='both', padx=4, pady=4, side='top')

        self.FrameOption = Labelframe(self)
        self.LabelRotateDegree = Label(self.FrameOption)
        self.LabelRotateDegree.configure(text='Rotation Degree(Clockwise)')
        self.LabelRotateDegree.pack(padx=4, pady=4, side='left')
        self.Radiobutton90 = Radiobutton(self.FrameOption)
        self.rotate_degree = IntVar(value=90)
        self.Radiobutton90.configure(text='90°', value='90', variable=self.rotate_degree)
        self.Radiobutton90.pack(padx=4, pady=4, side='left')
        self.Radiobutton180 = Radiobutton(self.FrameOption)
        self.Radiobutton180.configure(text='180°', value='180', variable=self.rotate_degree)
        self.Radiobutton180.pack(padx=4, pady=4, side='left')
        self.Radiobutton270 = Radiobutton(self.FrameOption)
        self.Radiobutton270.configure(text='-90°', value='270', variable=self.rotate_degree)
        self.Radiobutton270.pack(padx=4, pady=4, side='left')
        self.FrameOption.configure(height=200, text='Option', width=200)
        self.FrameOption.pack(fill='x', padx=4, pady=4, side='top')

        self.FrameOutputDir = Labelframe(self)
        self.EntryOutputDir = Entry(self.FrameOutputDir)
        self.output_dir = StringVar(value='')
        self.EntryOutputDir.configure(state='disabled', textvariable=self.output_dir)
        self.EntryOutputDir.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonOutputDir = Button(self.FrameOutputDir, width=10)
        self.ButtonOutputDir.configure(text='Browser')
        self.ButtonOutputDir.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonOutputDir.configure(command=self.set_output_dir)
        self.CheckButtonSourceDir = Checkbutton(self.FrameOutputDir)
        self.use_source_folder = BooleanVar(value=True)
        self.CheckButtonSourceDir.configure(text='Source Folder', variable=self.use_source_folder)
        self.CheckButtonSourceDir.configure(command=self.set_source_folder)
        self.CheckButtonSourceDir.pack(ipadx=4, ipady=4, side='right')
        self.FrameOutputDir.configure(height=200, text='Rotated PDF Folder', width=200)
        self.FrameOutputDir.pack(fill='x', padx=4, pady=4, side='top')

        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar(value='')
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.LabelProcessInfo.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=10)
        self.ButtonProcess.configure(state='disabled', text='Rotate')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='Rotate PDF', width=200)
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

    def set_output_dir(self):
        pass

    def set_source_folder(self):
        pass

    def process(self):
        pass
