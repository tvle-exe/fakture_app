# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_client_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_NewClientDialog(object):
    def setupUi(self, NewClientDialog):
        if not NewClientDialog.objectName():
            NewClientDialog.setObjectName(u"NewClientDialog")
        NewClientDialog.setModal(True)
        NewClientDialog.setMinimumWidth(400)
        self.mainLayout = QVBoxLayout(NewClientDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.clientDataGroupBox = QGroupBox(NewClientDialog)
        self.clientDataGroupBox.setObjectName(u"clientDataGroupBox")
        self.formLayout = QFormLayout(self.clientDataGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.clientDataGroupBox)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.clientDataGroupBox)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.oibLabel = QLabel(self.clientDataGroupBox)
        self.oibLabel.setObjectName(u"oibLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.oibLabel)

        self.oibLineEdit = QLineEdit(self.clientDataGroupBox)
        self.oibLineEdit.setObjectName(u"oibLineEdit")
        self.oibLineEdit.setMaxLength(11)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.oibLineEdit)

        self.addressLabel = QLabel(self.clientDataGroupBox)
        self.addressLabel.setObjectName(u"addressLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.addressLabel)

        self.addressLineEdit = QLineEdit(self.clientDataGroupBox)
        self.addressLineEdit.setObjectName(u"addressLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.addressLineEdit)

        self.phoneLabel = QLabel(self.clientDataGroupBox)
        self.phoneLabel.setObjectName(u"phoneLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.phoneLabel)

        self.phoneLineEdit = QLineEdit(self.clientDataGroupBox)
        self.phoneLineEdit.setObjectName(u"phoneLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.phoneLineEdit)

        self.emailLabel = QLabel(self.clientDataGroupBox)
        self.emailLabel.setObjectName(u"emailLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.emailLabel)

        self.emailLineEdit = QLineEdit(self.clientDataGroupBox)
        self.emailLineEdit.setObjectName(u"emailLineEdit")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.emailLineEdit)


        self.mainLayout.addWidget(self.clientDataGroupBox)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonLayout.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(NewClientDialog)
        self.saveButton.setObjectName(u"saveButton")

        self.buttonLayout.addWidget(self.saveButton)

        self.cancelButton = QPushButton(NewClientDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.buttonLayout.addWidget(self.cancelButton)


        self.mainLayout.addLayout(self.buttonLayout)


        self.retranslateUi(NewClientDialog)

        QMetaObject.connectSlotsByName(NewClientDialog)
    # setupUi

    def retranslateUi(self, NewClientDialog):
        NewClientDialog.setWindowTitle(QCoreApplication.translate("NewClientDialog", u"Novi klijent", None))
        self.clientDataGroupBox.setTitle(QCoreApplication.translate("NewClientDialog", u"Podaci o klijentu", None))
        self.nameLabel.setText(QCoreApplication.translate("NewClientDialog", u"Naziv *", None))
        self.oibLabel.setText(QCoreApplication.translate("NewClientDialog", u"OIB *", None))
        self.addressLabel.setText(QCoreApplication.translate("NewClientDialog", u"Adresa", None))
        self.phoneLabel.setText(QCoreApplication.translate("NewClientDialog", u"Telefon", None))
        self.emailLabel.setText(QCoreApplication.translate("NewClientDialog", u"Email", None))
        self.saveButton.setText(QCoreApplication.translate("NewClientDialog", u"Spremi", None))
        self.cancelButton.setText(QCoreApplication.translate("NewClientDialog", u"Odustani", None))
    # retranslateUi

