from ttkbootstrap import (
    Frame, Labelframe, Button,
    StringVar, Label, Entry
)


class UiExtractText(Frame):
    def __init__(self, master=None, **kw):
        super(UiExtractText, self).__init__(master, **kw)

        self.FramePDFFile = Labelframe(self)
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.pdf_file = StringVar(value='')
        self.EntryPDFFile.configure(state='readonly', textvariable=self.pdf_file)
        self.EntryPDFFile.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonPDFFile = Button(self.FramePDFFile, width=10)
        self.ButtonPDFFile.configure(text='Browser')
        self.ButtonPDFFile.pack(ipadx=2, padx=8, pady=4, side='right')
        self.ButtonPDFFile.configure(command=self.get_pdf_file)
        self.FramePDFFile.configure(text='PDF File')
        self.FramePDFFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameTextFile = Labelframe(self)
        self.EntryTextFile = Entry(self.FrameTextFile)
        self.text_file = StringVar(value='')
        self.EntryTextFile.configure(state='readonly', textvariable=self.text_file)
        self.EntryTextFile.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonTextFile = Button(self.FrameTextFile, width=10)
        self.ButtonTextFile.configure(text='Browser')
        self.ButtonTextFile.pack(ipadx=2, padx=8, pady=4, side='right')
        self.ButtonTextFile.configure(command=self.set_text_file)
        self.FrameTextFile.configure(height=200, text='Text File', width=200)
        self.FrameTextFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar(value='')
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.LabelProcessInfo.pack(padx=5, pady=5, side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=10)
        self.ButtonProcess.configure(state='disabled', text='Extract')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='right')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='Extract Text', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def get_pdf_file(self):
        pass

    def set_text_file(self):
        pass

    def process(self):
        pass
