from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtWidgets import QHeaderView
from views.base_window import BaseWindow
from utils.resource_path import resource_path


class HistoryWindow(BaseWindow):
    def __init__(self):
        super().__init__(resizable=True)

        loader = QUiLoader()
        ui_path = resource_path("ui/history_window.ui")
        ui_file = QFile(ui_path)

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Ne mogu otvoriti UI file: {ui_path}")

        ui = loader.load(ui_file, self)
        ui_file.close()

        if ui is None:
            raise RuntimeError("history_window.ui se nije učitao")

        # 🔑 AKO je UI QMainWindow
        if hasattr(ui, "centralWidget") and ui.centralWidget():
            self.setCentralWidget(ui.centralWidget())
            if ui.menuBar():
                self.setMenuBar(ui.menuBar())
            if ui.statusBar():
                self.setStatusBar(ui.statusBar())
        else:
            # 🔑 AKO je UI QWidget
            self.setCentralWidget(ui)

        self.ui = ui
        self.setWindowTitle("Povijest faktura")

        # Stretch kolone (ovo sada sigurno postoji)
        self.ui.invoicesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.itemsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.show_fullscreen()
