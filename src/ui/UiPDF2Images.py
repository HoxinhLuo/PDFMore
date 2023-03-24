from ttkbootstrap import (
    Frame, Labelframe, Button,
    StringVar, Label, Entry, Checkbutton,
    IntVar, Scale, Combobox, Radiobutton
)


class UiPDF2Images(Frame):
    def __init__(self, master=None, **kw):
        super(UiPDF2Images, self).__init__(master, **kw)
        self.FramePDFFile = Labelframe(self)
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.pdf_file = StringVar()
        self.EntryPDFFile.configure(
            state='readonly', textvariable=self.pdf_file
        )
        self.EntryPDFFile.pack(
            expand=True, fill='x', padx=4, pady=4, side='left'
        )
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
        self.FrameOption = Labelframe(self)
        self.LabelImageFormat = Label(self.FrameOption)
        self.LabelImageFormat.configure(text='Image Format')
        self.LabelImageFormat.pack(padx=4, pady=4, side='left')
        self.RadioButtonPNG = Radiobutton(self.FrameOption)
        self.image_format = StringVar(value='png')
        self.RadioButtonPNG.configure(text='PNG', value='png', variable=self.image_format)
        self.RadioButtonPNG.pack(padx=4, pady=4, side='left')
        self.RadioButtonPNG.configure(command=self.set_image_format)
        self.CheckbuttonPNGAlpha = Checkbutton(self.FrameOption)
        self.image_alpha = IntVar()
        self.CheckbuttonPNGAlpha.configure(offvalue=0, onvalue=1, text='Transparent', variable=self.image_alpha)
        self.CheckbuttonPNGAlpha.pack(padx=4, pady=4, side='left')
        self.CheckbuttonPNGAlpha.configure(command=self.set_image_alpha)
        self.RadioButtonJPEG = Radiobutton(self.FrameOption)
        self.RadioButtonJPEG.configure(text='JPEG', value='jpg', variable=self.image_format)
        self.RadioButtonJPEG.pack(padx=4, pady=4, side='left')
        self.RadioButtonJPEG.configure(command=self.set_image_format)
        self.LabelImageQuality = Label(self.FrameOption)
        self.LabelImageQuality.configure(state='disabled', text='Image Quality')
        self.LabelImageQuality.pack(padx=4, pady=4, side='left')
        self.EntryImageQuality = Entry(self.FrameOption)
        self.image_quality = IntVar()
        self.EntryImageQuality.configure(
            justify='center', state='disabled', textvariable=self.image_quality, validate='all'
        )
        self.EntryImageQuality.configure(width=3)
        self.EntryImageQuality.pack(padx=4, pady=4, side='left')
        _validatecmd = (self.EntryImageQuality.register(self.valid_image_quality), '%d', '%P', '%V')
        self.EntryImageQuality.configure(validatecommand=_validatecmd)
        self.ScaleImageQuality = Scale(self.FrameOption)
        self.ScaleImageQuality.configure(from_=0, orient='horizontal', state='disabled', to=100)
        self.ScaleImageQuality.configure(value=80, variable=self.image_quality)
        self.ScaleImageQuality.pack(padx=4, pady=4, side='left')
        self.ScaleImageQuality.configure(command=self.set_image_quality)
        self.LabelImageDPI = Label(self.FrameOption)
        self.LabelImageDPI.configure(state='disabled', text='DPI')
        self.LabelImageDPI.pack(padx=4, pady=4, side='left')
        self.ComboboxImageDPI = Combobox(self.FrameOption)
        self.image_dpi = IntVar()
        self.ComboboxImageDPI.configure(justify='center', state='disabled', textvariable=self.image_dpi, validate='all')
        self.ComboboxImageDPI.configure(values='96 144 192 240 288 336 384 432 480 528 576 624'.split(' '), width=4)
        self.ComboboxImageDPI.pack(padx=4, pady=4, side='left')
        # _validatecmd = (self.ComboboxImageDPI.register(self.valid_image_dpi), '%d', '%P', '%V')
        # self.ComboboxImageDPI.configure(validatecommand=_validatecmd)
        self.FrameOption.configure(height=200, text='Option', width=200)
        self.FrameOption.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar()
        self.LabelAppInfo.configure(justify='left', textvariable=self.app_info)
        self.LabelAppInfo.pack(fill='y', padx=4, pady=4, side='left')
        self.FrameSpacer = Frame(self.FrameProcess)
        self.FrameSpacer.configure(height=1, width=1)
        self.FrameSpacer.pack(expand=True, fill='y', side='left')
        self.ButtonProcess = Button(self.FrameProcess, width=10)
        self.ButtonProcess.configure(state='disabled', text='Convert')
        self.ButtonProcess.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        self.FrameProcess.configure(height=200, text='PDF to Images', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def get_pdf_file(self):
        pass

    def set_images_dir(self):
        pass

    def set_image_format(self):
        pass

    def set_image_alpha(self):
        pass

    def valid_image_quality(self, d, P, V):
        pass

    def set_image_quality(self, scale_value):
        pass

    def valid_image_dpi(self, d, P, V):
        pass

    def process(self):
        pass
