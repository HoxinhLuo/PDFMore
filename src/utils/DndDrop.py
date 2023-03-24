from tkinterdnd2 import DND_FILES


class DndDrop:
    def drop(self):
        self.drop_target_register(DND_FILES)
        self.dnd_bind('<<Drop>>', self.drop_file)

    def drop_file(self, event):
        pass
