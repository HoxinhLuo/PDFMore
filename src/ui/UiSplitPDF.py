from ttkbootstrap import (
    Frame, Labelframe, Button,
    StringVar, Label, Entry,
    IntVar, Combobox, Radiobutton
)



class UiSplitPDF(Frame):
    def __init__(self, master=None, **kw):
        super(UiSplitPDF, self).__init__(master, **kw)
        self.FramePDFFile = Labelframe(self)
        self.EntryPDFFile = Entry(self.FramePDFFile)
        self.pdf_file = StringVar(value='')
        self.EntryPDFFile.configure(state='readonly', textvariable=self.pdf_file)
        self.EntryPDFFile.pack(expand=1, fill='x', padx=4, pady=4, side='left')
        self.ButtonPDFFile = Button(self.FramePDFFile, width=10)
        self.ButtonPDFFile.configure(text='Browser')
        self.ButtonPDFFile.pack(ipadx=2, padx=8, pady=4, side='right')
        self.ButtonPDFFile.configure(command=self.get_pdf_file)

        self.FramePDFFile.configure(text='PDF File')
        self.FramePDFFile.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameSplitPDFDir = Labelframe(self)
        self.EntrySplitPDFDir = Entry(self.FrameSplitPDFDir)
        self.split_pdf_dir = StringVar(value='')
        self.EntrySplitPDFDir.configure(state='readonly', textvariable=self.split_pdf_dir)
        self.EntrySplitPDFDir.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonSplitPDFDir = Button(self.FrameSplitPDFDir, width=10)
        self.ButtonSplitPDFDir.configure(text='Browser')
        self.ButtonSplitPDFDir.pack(ipadx=2, padx=8, pady=4, side='left')
        self.ButtonSplitPDFDir.configure(command=self.set_split_pdf_dir)
        self.FrameSplitPDFDir.configure(height=200, text='Split PDF Folder', width=200)
        self.FrameSplitPDFDir.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameOption = Labelframe(self)
        self.FrameSplitMode = Frame(self.FrameOption)
        self.RadiobuttonSplitSingle = Radiobutton(self.FrameSplitMode)
        self.split_mode = StringVar(value='single')
        self.RadiobuttonSplitSingle.configure(
                state='disabled', text='Per Page', value='single', variable=self.split_mode
                )
        self.RadiobuttonSplitSingle.pack(padx=4, pady=4, side='left')
        self.RadiobuttonSplitSingle.configure(command=self.set_split_mode)
        self.RadiobuttonSplitPage = Radiobutton(self.FrameSplitMode)
        self.RadiobuttonSplitPage.configure(
            state='disabled', text='By Pages', value='page', variable=self.split_mode
        )
        self.RadiobuttonSplitPage.pack(padx=4, pady=4, side='left')
        self.RadiobuttonSplitPage.configure(command=self.set_split_mode)
        self.EntrySplitPage = Entry(self.FrameSplitMode)
        self.split_page = IntVar()
        self.EntrySplitPage.configure(justify='center', state='disabled', textvariable=self.split_page, validate='all')
        self.EntrySplitPage.configure(width=4)
        self.EntrySplitPage.pack(padx=4, pady=4, side='left')
        _validatecmd = (self.EntrySplitPage.register(self.valid_split_pages), '%d', '%P', '%V')
        self.EntrySplitPage.configure(validatecommand=_validatecmd)
        self.RadiobuttonSplitCount = Radiobutton(self.FrameSplitMode)
        self.RadiobuttonSplitCount.configure(
            # state='disabled', text=_('By Count'), value='count', variable=self.split_mode
            state='disabled', text='By Count', value='count', variable=self.split_mode
        )
        self.RadiobuttonSplitCount.pack(padx=4, pady=4, side='left')
        self.RadiobuttonSplitCount.configure(command=self.set_split_mode)
        self.ComboboxSplitCount = Combobox(self.FrameSplitMode)
        self.split_count = IntVar()
        self.ComboboxSplitCount.configure(justify='center', state='disabled', textvariable=self.split_count, width=4)
        self.ComboboxSplitCount.pack(padx=4, pady=4, side='left')
        self.RadiobuttonSplitRange = Radiobutton(self.FrameSplitMode)
        self.RadiobuttonSplitRange.configure(
            # state='disabled', text=_('By Range'), value='range', variable=self.split_mode
            state='disabled', text='By Range', value='range', variable=self.split_mode
        )
        self.RadiobuttonSplitRange.pack(padx=4, pady=4, side='left')
        self.RadiobuttonSplitRange.configure(command=self.set_split_mode)
        self.EntrySplitRangeStart = Entry(self.FrameSplitMode)
        self.split_range_start = IntVar()
        self.EntrySplitRangeStart.configure(
            justify='center', state='disabled', textvariable=self.split_range_start, validate='all'
        )
        self.EntrySplitRangeStart.configure(width=5)
        self.EntrySplitRangeStart.pack(padx=4, pady=4, side='left')
        _validatecmd = (self.EntrySplitRangeStart.register(self.valid_split_range), '%d', '%P', '%V', '%W')
        self.EntrySplitRangeStart.configure(validatecommand=_validatecmd)
        self.LabelSplitRangeTo = Label(self.FrameSplitMode)
        self.LabelSplitRangeTo.configure(state='disabled', text='-')
        self.LabelSplitRangeTo.pack(padx=2, pady=4, side='left')
        self.EntrySplitRangeStop = Entry(self.FrameSplitMode)
        self.split_range_stop = IntVar()
        self.EntrySplitRangeStop.configure(
            justify='center', state='disabled', textvariable=self.split_range_stop, validate='all'
        )
        self.EntrySplitRangeStop.configure(width=5)
        self.EntrySplitRangeStop.pack(padx=4, pady=4, side='left')
        _validatecmd = (self.EntrySplitRangeStop.register(self.valid_split_range), '%d', '%P', '%V', '%W')
        self.EntrySplitRangeStop.configure(validatecommand=_validatecmd)
        self.FrameSplitMode.configure(height=200, width=200)
        self.FrameSplitMode.pack(fill='x', side='top')
        # self.FrameOption.configure(height=200, text=_('Option'), width=200)
        self.FrameOption.configure(height=200, text='Option', width=200)
        self.FrameOption.pack(fill='x', padx=4, pady=4, side='top')
        self.FrameProcess = Labelframe(self)
        self.LabelAppInfo = Label(self.FrameProcess)
        self.app_info = StringVar(value='')
        self.LabelAppInfo.configure(textvariable=self.app_info)
        self.LabelAppInfo.pack(padx=4, pady=4, side='left')
        self.LabelProcessInfo = Label(self.FrameProcess)
        self.process_info = StringVar(value='')
        self.LabelProcessInfo.configure(textvariable=self.process_info)
        self.LabelProcessInfo.pack(expand=True, fill='x', padx=4, pady=4, side='left')
        self.ButtonProcess = Button(self.FrameProcess)
        # self.ButtonProcess.configure(state='disabled', text=_('Split'))
        self.ButtonProcess.configure(state='disabled', text='Split')
        self.ButtonProcess.pack(ipadx=2, padx=4, pady=4, side='left')
        self.ButtonProcess.configure(command=self.process)
        # self.FrameProcess.configure(height=200, text=_('Split PDF'), width=200)
        self.FrameProcess.configure(height=200, text='Split PDF', width=200)
        self.FrameProcess.pack(fill='x', padx=4, pady=4, side='top')

    def get_pdf_file(self):
        pass

    def set_split_pdf_dir(self):
        pass

    def set_split_mode(self):
        pass

    def valid_split_pages(self, d, P, V):
        pass

    def valid_split_range(self, d, P, V, W):
        pass

    def process(self):
        pass
