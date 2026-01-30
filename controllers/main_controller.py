from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from controllers.invoice_controller import InvoiceController

class MainController:
    def __init__(self):
        self.window = MainWindow()
        self.connect_signals()
        self.window.show()

    def connect_signals(self):
        self.window.ui.exitButton.clicked.connect(QApplication.quit)
        self.window.ui.novaFakturaButton.clicked.connect(self.open_invoice)

    def open_invoice(self):
        self.invoice_controller = InvoiceController()
        self.invoice_controller.open()
