

class Center:
    def _center(self):
        self.update_idletasks()
        width, height = self.winfo_width(), self.winfo_height()
        screen_width, screen_height = self.winfo_screenwidth(), self.winfo_screenheight() * 3 // 5
        left = (screen_width - width) // 2
        top = (screen_height - height) // 2
        self.wm_geometry(f'+{left}+{top}')
