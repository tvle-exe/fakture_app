from views.base_window import BaseWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__(resizable=True)  # resizable, veličina 900x700 po defaultu

        # Učitaj .ui file
        loader = QUiLoader()
        ui_file = QFile("ui/main_window.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Postavi centralni widget
        self.setCentralWidget(self.ui)
        self.setWindowTitle("Fakture App")

        # Otvori fullscreen
        self.show_fullscreen()
