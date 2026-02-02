from views.base_window import BaseWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from utils.resource_path import resource_path


class MainWindow(BaseWindow):
    def __init__(self):
        super().__init__(resizable=True)

        loader = QUiLoader()
        ui_path = resource_path("ui/main_window.ui")
        ui_file = QFile(ui_path)

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        ui = loader.load(ui_file)
        ui_file.close()

   
        self.setCentralWidget(ui.centralWidget())

        # ako postoje
        if ui.menuBar():
            self.setMenuBar(ui.menuBar())
        if ui.statusBar():
            self.setStatusBar(ui.statusBar())

        self.ui = ui
        self.setWindowTitle("Fakture App")
        self.show_fullscreen()