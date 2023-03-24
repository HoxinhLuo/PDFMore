from ttkbootstrap import (
    Label, Toplevel, StringVar, Frame, Button
)


class UiAboutV1(Toplevel):
    def __init__(self, master=None, **kw):
        super(UiAboutV1, self).__init__(master, **kw)
        self.FrameAbout = Frame(self)
        self.LabelAppName = Label(self.FrameAbout)
        self.app_name = StringVar(value='PDFMore')
        self.LabelAppName.configure(font='{Arial} 36 {bold}', text='PDFMore', textvariable=self.app_name)
        self.LabelAppName.pack(padx=60, pady=40, side='top')
        self.LabelAppVersion = Label(self.FrameAbout)
        self.app_version = StringVar(value='0.1-BETA')
        self.LabelAppVersion.configure(font='{Arial} 14 {bold}', text='0.1-BETA', textvariable=self.app_version)
        self.LabelAppVersion.pack(side='top')
        self.LabelUrl = Label(self.FrameAbout)
        self.app_url = StringVar(value='https://github.com/HoxinhLuo/PDFMore')
        self.LabelUrl.configure(
            cursor='hand2', font='{Arial} 10 {underline}', foreground='#0000ff',
            text='https://github.com/HoxinhLuo/PDFMore'
        )
        self.LabelUrl.configure(textvariable=self.app_url)
        self.LabelUrl.pack(pady='20', side='top')
        self.LabelUrl.bind('<Button-1>', self.open_url, add='')
        self.ButtonOK = Button(self.FrameAbout)
        self.ButtonOK.configure(text='OK')
        self.ButtonOK.pack(ipadx='2', pady='30', side='top')
        self.ButtonOK.configure(command=self.close_about)
        self.FrameAbout.configure(height='200', width='200')
        self.FrameAbout.pack(side='top')

    def open_url(self, event=None):
        pass

    def close_about(self):
        pass


class UiAbout(Toplevel):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.configure(height=200, width=400)
        self.resizable(False, False)
        self.title('About PDFMore')
        self.FrameAbout = Frame(self)
        self.FrameAbout.configure(height=200, width=200)
        self.FrameLogo = Frame(self.FrameAbout)
        self.FrameLogo.configure(height=200, width=200)
        self.LabelLogo = Label(self.FrameLogo)

        self.LabelLogo.pack(padx=10, pady=40, side="left")
        self.LabelAppName = Label(self.FrameLogo)
        self.app_name = StringVar(value="PDFMore")
        self.LabelAppName.configure(
            font="{Arial} 36 {bold}", text="PDFMore", textvariable=self.app_name
        )
        self.LabelAppName.pack(padx=10, pady=40, side="left")
        self.FrameLogo.pack(padx=30, pady=5, side="top")
        self.LabelAppVersion = Label(self.FrameAbout)
        self.app_version = StringVar(value="1.0.0-BETA")
        self.LabelAppVersion.configure(
            font="{Arial} 14 {bold}", text="1.0.0-BETA", textvariable=self.app_version
        )
        self.LabelAppVersion.pack(side="top")
        self.LabelUrl = Label(self.FrameAbout)
        self.app_url = StringVar(value="https://github.com/HoxinhLuo/PDFMore")
        self.LabelUrl.configure(
            cursor="hand2",
            font="{Arial} 10 {underline}",
            foreground="#0000ff",
            text="https://github.com/HoxinhLuo/PDFMore",
            textvariable=self.app_url,
        )
        self.LabelUrl.pack(pady=15, side="top")
        self.LabelUrl.bind("<Button-1>", self.open_url, add="")
        self.ButtonOK = Button(self.FrameAbout)
        self.ButtonOK.configure(text="OK")
        self.ButtonOK.pack(ipadx=2, pady=20, side="top")
        self.ButtonOK.configure(command=self.close_about)
        self.FrameAbout.pack(side="top")

    def open_url(self, event=None):
        pass

    def close_about(self):
        pass
