from PySide6.QtWidgets import QApplication
from views.main_window import MainWindow
from controllers.invoice_controller import InvoiceController
from controllers.clients_controller import ClientsController
from controllers.history_controller import HistoryController


class MainController:
    def __init__(self):
        self.window = MainWindow()
        self.connect_signals()
        self.window.show()

    def connect_signals(self):
        self.window.ui.exitButton.clicked.connect(QApplication.quit)
        self.window.ui.novaFakturaButton.clicked.connect(self.open_invoice)
        self.window.ui.clientsButton.clicked.connect(self.open_clients)
        self.window.ui.povijestFakturaButton.clicked.connect(self.open_history)

    def open_invoice(self):
        self.invoice_controller = InvoiceController()
        self.invoice_controller.open()

    def open_clients(self):
        self.clients_controller = ClientsController()
        self.clients_controller.open()

    def open_history(self): 
        self.history_controller = HistoryController()
        self.history_controller.open()