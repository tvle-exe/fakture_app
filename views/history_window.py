from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from views.base_window import BaseWindow
from PySide6.QtWidgets import QHeaderView

class HistoryWindow(BaseWindow):
    def __init__(self):
        super().__init__(resizable=True)  # resizable, veličina 900x700 po defaultu

        # Učitaj .ui file
        loader = QUiLoader()
        ui_file = QFile("ui/history_window.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()

        # Postavi centralni widget
        self.setCentralWidget(self.ui)
        self.setWindowTitle("Povijest faktura")

        # Stretch kolone u tablicama
        self.ui.invoicesTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.itemsTableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Prikaži fullscreen
        self.show_fullscreen()
