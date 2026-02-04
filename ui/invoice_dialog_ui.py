# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'invoice_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFormLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_InvoiceWindow(object):
    def setupUi(self, InvoiceWindow):
        if not InvoiceWindow.objectName():
            InvoiceWindow.setObjectName(u"InvoiceWindow")
        InvoiceWindow.resize(720, 520)
        self.verticalLayout = QVBoxLayout(InvoiceWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.invoiceInfoGroupBox = QGroupBox(InvoiceWindow)
        self.invoiceInfoGroupBox.setObjectName(u"invoiceInfoGroupBox")
        self.formLayout = QFormLayout(self.invoiceInfoGroupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.invoiceNumberLabel = QLabel(self.invoiceInfoGroupBox)
        self.invoiceNumberLabel.setObjectName(u"invoiceNumberLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.invoiceNumberLabel)

        self.invoiceNumberLineEdit = QLineEdit(self.invoiceInfoGroupBox)
        self.invoiceNumberLineEdit.setObjectName(u"invoiceNumberLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.invoiceNumberLineEdit)

        self.clientLabel = QLabel(self.invoiceInfoGroupBox)
        self.clientLabel.setObjectName(u"clientLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.clientLabel)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.clientComboBox = QComboBox(self.invoiceInfoGroupBox)
        self.clientComboBox.setObjectName(u"clientComboBox")

        self.hboxLayout.addWidget(self.clientComboBox)

        self.addClientButton = QPushButton(self.invoiceInfoGroupBox)
        self.addClientButton.setObjectName(u"addClientButton")
        self.addClientButton.setMaximumWidth(30)

        self.hboxLayout.addWidget(self.addClientButton)


        self.formLayout.setLayout(1, QFormLayout.ItemRole.FieldRole, self.hboxLayout)

        self.descriptionLabel = QLabel(self.invoiceInfoGroupBox)
        self.descriptionLabel.setObjectName(u"descriptionLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.descriptionLabel)

        self.descriptionLineEdit = QLineEdit(self.invoiceInfoGroupBox)
        self.descriptionLineEdit.setObjectName(u"descriptionLineEdit")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.descriptionLineEdit)

        self.dateLabel = QLabel(self.invoiceInfoGroupBox)
        self.dateLabel.setObjectName(u"dateLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.dateLabel)

        self.dateEdit = QDateEdit(self.invoiceInfoGroupBox)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.dateEdit)


        self.verticalLayout.addWidget(self.invoiceInfoGroupBox)

        self.itemsTableWidget = QTableWidget(InvoiceWindow)
        if (self.itemsTableWidget.columnCount() < 5):
            self.itemsTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.itemsTableWidget.setObjectName(u"itemsTableWidget")
        self.itemsTableWidget.setColumnCount(5)

        self.verticalLayout.addWidget(self.itemsTableWidget)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.addItemButton = QPushButton(InvoiceWindow)
        self.addItemButton.setObjectName(u"addItemButton")

        self.hboxLayout1.addWidget(self.addItemButton)

        self.removeItemButton = QPushButton(InvoiceWindow)
        self.removeItemButton.setObjectName(u"removeItemButton")

        self.hboxLayout1.addWidget(self.removeItemButton)


        self.verticalLayout.addLayout(self.hboxLayout1)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.totalLabel = QLabel(InvoiceWindow)
        self.totalLabel.setObjectName(u"totalLabel")

        self.hboxLayout2.addWidget(self.totalLabel)

        self.totalLineEdit = QLineEdit(InvoiceWindow)
        self.totalLineEdit.setObjectName(u"totalLineEdit")
        self.totalLineEdit.setReadOnly(True)

        self.hboxLayout2.addWidget(self.totalLineEdit)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout2.addItem(self.spacerItem)

        self.pdvCheckBox = QCheckBox(InvoiceWindow)
        self.pdvCheckBox.setObjectName(u"pdvCheckBox")
        self.pdvCheckBox.setChecked(True)

        self.hboxLayout2.addWidget(self.pdvCheckBox)

        self.saveButton = QPushButton(InvoiceWindow)
        self.saveButton.setObjectName(u"saveButton")

        self.hboxLayout2.addWidget(self.saveButton)

        self.closeButton = QPushButton(InvoiceWindow)
        self.closeButton.setObjectName(u"closeButton")

        self.hboxLayout2.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.hboxLayout2)


        self.retranslateUi(InvoiceWindow)

        QMetaObject.connectSlotsByName(InvoiceWindow)
    # setupUi

    def retranslateUi(self, InvoiceWindow):
        InvoiceWindow.setWindowTitle(QCoreApplication.translate("InvoiceWindow", u"Faktura", None))
        self.invoiceInfoGroupBox.setTitle(QCoreApplication.translate("InvoiceWindow", u"Podaci o fakturi", None))
        self.invoiceNumberLabel.setText(QCoreApplication.translate("InvoiceWindow", u"Broj fakture:", None))
        self.clientLabel.setText(QCoreApplication.translate("InvoiceWindow", u"Klijent:", None))
        self.addClientButton.setText(QCoreApplication.translate("InvoiceWindow", u"+", None))
        self.descriptionLabel.setText(QCoreApplication.translate("InvoiceWindow", u"Opis:", None))
        self.dateLabel.setText(QCoreApplication.translate("InvoiceWindow", u"Datum:", None))
        ___qtablewidgetitem = self.itemsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("InvoiceWindow", u"Roba / Usluga", None));
        ___qtablewidgetitem1 = self.itemsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("InvoiceWindow", u"Koli\u010dina", None));
        ___qtablewidgetitem2 = self.itemsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("InvoiceWindow", u"Jedinica", None));
        ___qtablewidgetitem3 = self.itemsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("InvoiceWindow", u"Cijena", None));
        ___qtablewidgetitem4 = self.itemsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("InvoiceWindow", u"Iznos", None));
        self.addItemButton.setText(QCoreApplication.translate("InvoiceWindow", u"+ Dodaj stavku", None))
        self.removeItemButton.setText(QCoreApplication.translate("InvoiceWindow", u"- Ukloni stavku", None))
        self.totalLabel.setText(QCoreApplication.translate("InvoiceWindow", u"Ukupno:", None))
        self.pdvCheckBox.setText(QCoreApplication.translate("InvoiceWindow", u"PDV 25%", None))
        self.saveButton.setText(QCoreApplication.translate("InvoiceWindow", u"Spremi", None))
        self.closeButton.setText(QCoreApplication.translate("InvoiceWindow", u"Zatvori", None))
    # retranslateUi

