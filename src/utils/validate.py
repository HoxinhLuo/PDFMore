
class ValidateDpi:

    def valid_image_dpi(self, d, P, V):
        if d == '0' \
                or d == '1' and not P.startswith('0') and P.isdigit() and 0 < int(P) \
                or V == 'focusout' and P.isdigit() and 0 < int(P):
            if self.ComboboxImageDPI.grab_status():
                self.ComboboxImageDPI.grab_release()
            return True

        self.ComboboxImageDPI.grab_set()
        self.ComboboxImageDPI.focus()
        return False
