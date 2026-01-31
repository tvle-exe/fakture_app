from views.new_client_dialog import NewClientDialog


class NewClientController:
    def __init__(self, parent=None):
        self.dialog = NewClientDialog(parent=parent)

        self.dialog.saveButton.clicked.connect(self.save)
        self.dialog.cancelButton.clicked.connect(self.dialog.reject)

    def open(self):
        return self.dialog.open()

    def save(self):
        name = self.dialog.nameLineEdit.text()
        oib = self.dialog.oibLineEdit.text()
        address = self.dialog.addressLineEdit.text()
        phone = self.dialog.phoneLineEdit.text()
        email = self.dialog.emailLineEdit.text()

        # TODO: validacija
        # TODO: spremanje u bazu / JSON

        print("Novi klijent:")
        print(name, oib, address, phone, email)

        self.dialog.accept()
