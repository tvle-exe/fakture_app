from PySide6.QtWidgets import QDialog

class BaseDialog(QDialog):
    def __init__(self, width=900, height=700, resizable=True, parent=None):
        super().__init__(parent)

        # Postavi početnu veličinu
        self.resize(width, height)

        if resizable:
            self.setMinimumSize(width, height)
        else:
            self.setFixedSize(width, height)

    def show_fullscreen(self):
        """Otvoriti dijalog odmah full screen"""
        self.showMaximized()
