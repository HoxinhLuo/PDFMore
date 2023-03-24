from ttkbootstrap import PhotoImage
from webbrowser import open_new_tab
from constants import ABOUT_ICON, APP_URL, APP_ICON
from ui.UiAbout import UiAbout
from utils.center import Center


class About(UiAbout, Center):
    def __init__(self, master, **kw):
        super(About, self).__init__(master, **kw)

        self._center()

        # self.app_name.set(APP_NAME)
        # self.app_version.set(APP_VERSION)
        # self.app_url.set(APP_URL)
        self.img_PDFMore = PhotoImage(file=ABOUT_ICON)
        self.LabelLogo.configure(image=self.img_PDFMore)
        self.wm_iconphoto(False, PhotoImage(file=APP_ICON))
        self.ButtonOK.focus_set()
        self.grab_set()

    def open_url(self, event=None):
        open_new_tab(APP_URL)

    def close_about(self):
        self.destroy()
