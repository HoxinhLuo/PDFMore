from ttkbootstrap import (
    Frame, Labelframe, Button,
    StringVar, Label, Entry,
    IntVar, Scale, Combobox
)


class UiCompressPDF(Frame):
    def __init__(self, master=None, **kw):
        super(UiCompressPDF, self).__init__(master, **kw)
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
        self.FrameCompressedPDFFile = Labelframe(self)
        self.EntryCompressedPDFFile = Entry(self.FrameCompressedPDFFile)
        self.compressed_pdf_file = StringVar()
        self.EntryCompressedPDFFile.configure(state='readonly', textvariable=self.compressed_pdf_file)
        self.EntryCompressedPDFFile.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonCompressedPDFFile = Button(self.FrameCompressedPDFFile, width=10)
        self.ButtonCompressedPDFFile.configure(text='Browser')
        self.ButtonCompressedPDFFile.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonCompressedPDFFile.configure(command=self.set_compressed_pdf_file)
        self.FrameCompressedPDFFile.configure(height=200, text='Compressed PDF File', width=200)
        self.FrameCompressedPDFFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameOption = Labelframe(self)
        self.LabelImageQuality = Label(self.FrameOption)
        self.LabelImageQuality.configure(text='Image Quality')
        self.LabelImageQuality.pack(padx=4, pady=4, side='left')
        self.EntryImageQuality = Entry(self.FrameOption)
        self.image_quality = IntVar()
        self.EntryImageQuality.configure(justify='center', textvariable=self.image_quality, validate='all', width=3)
        self.EntryImageQuality.pack(padx=4, pady=4, side='left')
        _validatecmd = (self.EntryImageQuality.register(self.valid_image_quality), '%d', '%P', '%V')
        self.EntryImageQuality.configure(validatecommand=_validatecmd)
        self.ScaleImageQuality = Scale(self.FrameOption)
        self.ScaleImageQuality.configure(from_=0, orient='horizontal', to=100, value=80)
        self.ScaleImageQuality.configure(variable=self.image_quality)
        self.ScaleImageQuality.pack(padx=4, pady=4, side='left')
        self.ScaleImageQuality.configure(command=self.set_image_quality)
        self.FrameSpacer = Frame(self.FrameOption)
        self.FrameSpacer.configure(height=1, width=20)
        self.FrameSpacer.pack(padx=4, pady=4, side='left')
        self.LabelImageMaxDPI = Label(self.FrameOption)
        self.LabelImageMaxDPI.configure(text='Max DPI')
        self.LabelImageMaxDPI.pack(padx=4, pady=4, side='left')
        self.ComboboxDPI = Combobox(self.FrameOption)
        self.image_max_dpi = IntVar()
        self.ComboboxDPI.configure(justify='center', state='normal', textvariable=self.image_max_dpi, validate='all')
        self.ComboboxDPI.configure(values='96 144 192 244 288 384 480 576'.split(' '), width=3)
        self.ComboboxDPI.pack(padx=4, pady=4, side='left')
        _validatecmd = (self.ComboboxDPI.register(self.valid_image_dpi), '%d', '%P', '%V')
        self.ComboboxDPI.configure(validatecommand=_validatecmd)
        self.FrameOption.configure(height=200, text='Option', width=200)
        self.FrameOption.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelPDFInfo = Label(self.FrameProcess)
        self.pdf_info = StringVar()
        self.LabelPDFInfo.configure(textvariable=self.pdf_info)
        self.LabelPDFInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.process_info = StringVar()
        self.LabelProcessInfo.configure(textvariable=self.process_info)
        self.LabelProcessInfo.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=10)
        self.ButtonProcess.configure(state='disabled', text='Compress')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='Compress PDF', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def get_pdf_file(self):
        pass

    def set_compressed_pdf_file(self):
        pass

    def valid_image_quality(self, d, P, V):
        pass

    def set_image_quality(self, scale_value):
        pass

    def valid_image_dpi(self, d, P, V):
        pass

    def process(self):
        pass
