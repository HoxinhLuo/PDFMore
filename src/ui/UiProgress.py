from ttkbootstrap import (
    Frame, Button, Toplevel, StringVar, Label, IntVar, Progressbar
)


class UiProgress(Toplevel):
    def __init__(self, master=None, **kw):
        super(UiProgress, self).__init__(master, **kw)
        self.Frame = Frame(self)
        self.FrameInfo = Frame(self.Frame)
        self.LabelAppInfo = Label(self.FrameInfo)
        self.app_info = StringVar()
        self.LabelAppInfo.configure(compound='top', textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=20, side='left')
        self.LabelProcessInfo = Label(self.FrameInfo)
        self.process_info = StringVar()
        self.LabelProcessInfo.configure(textvariable=self.process_info)
        self.LabelProcessInfo.pack(side='left')
        self.FrameInfo.configure(height=200, width=200)
        self.FrameInfo.pack(fill='x', pady=20, side='top')
        self.Progressbar = Progressbar(self.Frame)
        self.progress = IntVar()
        self.Progressbar.configure(length=400, orient='horizontal', variable=self.progress)
        self.Progressbar.pack(fill='y', padx=20, side='top')
        self.ButtonStop = Button(self.Frame)
        # self.ButtonStop.configure(text=_('Stop'))
        self.ButtonStop.configure(text='Stop')
        self.ButtonStop.pack(ipadx=2, pady=20, side='top')
        self.ButtonStop.configure(command=self.stop_process)
        self.Frame.configure(height=400, width='500')
        self.Frame.pack(expand=True, fill='both', side='top')

    def stop_process(self):
        pass
