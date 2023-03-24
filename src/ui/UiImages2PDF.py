from ttkbootstrap import (
    Frame, Labelframe, Treeview, Scrollbar, Button,
    StringVar, Label, Separator, Entry
)


class UiImages2PDF(Frame):
    def __init__(self, master=None, **kw):
        super(UiImages2PDF, self).__init__(master, **kw)

        self.FrameImageList = Labelframe(self)
        self.TreeViewImageList = Treeview(self.FrameImageList)
        _columns = ['dir_name', 'file_name']
        _display_columns = ['dir_name', 'file_name']
        self.TreeViewImageList.configure(columns=_columns, displaycolumns=_display_columns, show='headings')
        self.TreeViewImageList.column('dir_name', anchor='center', stretch=True, width=150, minwidth=150)
        self.TreeViewImageList.column('file_name', anchor='center', stretch=True, width=300, minwidth=150)
        self.TreeViewImageList.heading('dir_name', anchor='center', text='Folder')
        self.TreeViewImageList.heading('file_name', anchor='center', text='File Name')
        self.TreeViewImageList.pack(expand=True, fill='both', padx=4, pady=4, side='left')
        self.ScrollbarImagesList = Scrollbar(self.FrameImageList)
        self.ScrollbarImagesList.configure(orient='vertical')
        self.ScrollbarImagesList.pack(fill='y', pady=4, side='left')
        self.PDFListButtonFrame = Frame(self.FrameImageList)
        self.PDFListButtonFrame.configure(height=200)
        self.ButtonAddImages = Button(self.PDFListButtonFrame)
        self.ButtonAddImages.configure(text='Add Images')
        self.ButtonAddImages.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonAddImages.configure(command=self.add_images)
        self.ButtonRemoveImage = Button(self.PDFListButtonFrame)
        self.ButtonRemoveImage.configure(text='Remove Image')
        self.ButtonRemoveImage.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonRemoveImage.configure(command=self.remove_images)
        self.ButtonRemoveAll = Button(self.PDFListButtonFrame)
        self.ButtonRemoveAll.configure(text='Remove All')
        self.ButtonRemoveAll.pack(fill='x', ipadx=2, padx=4, pady=4, side='top')
        self.ButtonRemoveAll.configure(command=self.remove_all)
        self.Separator = Separator(self.PDFListButtonFrame)
        self.Separator.configure(orient='horizontal')
        self.Separator.pack(fill='x', padx=4, pady=8, side='top')
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
        self.FrameImageList.configure(text='Image List')
        self.FrameImageList.pack(expand=True, fill='both', padx=4, pady=4, side='top')
        self.FramePDFFile = Labelframe(self)
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.pdf_file = StringVar(value='')
        self.EntryPDFFile.configure(state='readonly', textvariable=self.pdf_file)
        self.EntryPDFFile.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonPDFFile = Button(self.FramePDFFile, width=12)
        self.ButtonPDFFile.configure(text='Browser')
        self.ButtonPDFFile.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonPDFFile.configure(command=self.set_pdf_file)
        self.FramePDFFile.configure(height=200, text='PDF File', width=200)
        self.FramePDFFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar(value='')
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.process_info = StringVar(value='')
        self.LabelProcessInfo.configure(textvariable=self.process_info)
        self.LabelProcessInfo.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=12)
        self.ButtonProcess.configure(state='disabled', text='Convert')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='Images to PDF', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def add_images(self):
        pass

    def remove_images(self):
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

    def set_pdf_file(self):
        pass

    def process(self):
        pass
