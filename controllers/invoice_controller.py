from views.invoice_dialog import InvoiceDialog


class InvoiceController:
    def __init__(self):
        self.dialog = InvoiceDialog()

        self.dialog.closeButton.clicked.connect(self.dialog.close)
        self.dialog.saveButton.clicked.connect(self.save)

    def open(self):
        self.dialog.open()

    def save(self):
        client = self.dialog.clientComboBox.currentText()
        description = self.dialog.descriptionLineEdit.text()

        print("Faktura spremljena:")
        print("Klijent:", client)
        print("Opis:", description)

        self.dialog.close()
