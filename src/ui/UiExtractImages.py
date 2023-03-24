from ttkbootstrap import (
    Frame, Labelframe, Button,
    StringVar, Label, Entry
)


class UiExtractImages(Frame):
    def __init__(self, master=None, **kw):
        super(UiExtractImages, self).__init__(master, **kw)

        self.FramePDFFile = Labelframe(self)
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.pdf_file = StringVar()
        self.EntryPDFFile.configure(state='readonly', textvariable=self.pdf_file)
        self.EntryPDFFile.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonPDFFile = Button(self.FramePDFFile, width=10)
        self.ButtonPDFFile.configure(text='Browser')
        self.ButtonPDFFile.pack(ipadx=2, padx=8, pady=4, side='right')
        self.ButtonPDFFile.configure(command=self.get_pdf_file)
        self.FramePDFFile.configure(text='PDF File')
        self.FramePDFFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameImagesDir = Labelframe(self)
        self.EntryImagesDir = Entry(self.FrameImagesDir)
        self.images_dir = StringVar()
        self.EntryImagesDir.configure(state='readonly', textvariable=self.images_dir)
        self.EntryImagesDir.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonImagesDir = Button(self.FrameImagesDir, width=10)
        self.ButtonImagesDir.configure(text='Browser')
        self.ButtonImagesDir.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonImagesDir.configure(command=self.set_images_dir)
        self.FrameImagesDir.configure(height=200, text='Images Folder', width=200)
        self.FrameImagesDir.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar()
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.LabelProcessInfo.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=10)
        self.ButtonProcess.configure(state='disabled', text='Extract')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='Extract Images', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def get_pdf_file(self):
        pass

    def set_images_dir(self):
        pass

    def process(self):
        pass
