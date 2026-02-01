from PySide6.QtWidgets import QMainWindow
import sys
import os


class BaseWindow(QMainWindow):
    def __init__(self, width=900, height=700, resizable=True):
        super().__init__()

        # Postavi početnu veličinu (za minimalnu veličinu ako korisnik resize-a)
        self.resize(width, height)

        if resizable:
            self.setMinimumSize(width, height)  # sprječava da prozor postane premali
        else:
            self.setFixedSize(width, height)  # fiksna veličina

    def show_fullscreen(self):
        """Otvoriti prozor odmah full screen nakon što je UI učitan"""
        self.showMaximized()
