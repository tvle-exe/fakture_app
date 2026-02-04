# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QFormLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_HistoryWindow(object):
    def setupUi(self, HistoryWindow):
        if not HistoryWindow.objectName():
            HistoryWindow.setObjectName(u"HistoryWindow")
        HistoryWindow.resize(900, 700)
        self.verticalLayout = QVBoxLayout(HistoryWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.invoicesTable = QTableWidget(HistoryWindow)
        if (self.invoicesTable.columnCount() < 4):
            self.invoicesTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.invoicesTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.invoicesTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.invoicesTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.invoicesTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.invoicesTable.setObjectName(u"invoicesTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoicesTable.sizePolicy().hasHeightForWidth())
        self.invoicesTable.setSizePolicy(sizePolicy)
        self.invoicesTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.invoicesTable.setColumnCount(4)

        self.verticalLayout.addWidget(self.invoicesTable)

        self.invoiceInfoGroupBox = QGroupBox(HistoryWindow)
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

        self.clientLineEdit = QLineEdit(self.invoiceInfoGroupBox)
        self.clientLineEdit.setObjectName(u"clientLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.clientLineEdit)

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

        self.itemsTableWidget = QTableWidget(HistoryWindow)
        if (self.itemsTableWidget.columnCount() < 5):
            self.itemsTableWidget.setColumnCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.itemsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        self.itemsTableWidget.setObjectName(u"itemsTableWidget")
        sizePolicy.setHeightForWidth(self.itemsTableWidget.sizePolicy().hasHeightForWidth())
        self.itemsTableWidget.setSizePolicy(sizePolicy)
        self.itemsTableWidget.setColumnCount(5)

        self.verticalLayout.addWidget(self.itemsTableWidget)

        self.hboxLayout = QHBoxLayout()
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.addItemButton = QPushButton(HistoryWindow)
        self.addItemButton.setObjectName(u"addItemButton")

        self.hboxLayout.addWidget(self.addItemButton)

        self.removeItemButton = QPushButton(HistoryWindow)
        self.removeItemButton.setObjectName(u"removeItemButton")

        self.hboxLayout.addWidget(self.removeItemButton)


        self.verticalLayout.addLayout(self.hboxLayout)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.subtotalLabel = QLabel(HistoryWindow)
        self.subtotalLabel.setObjectName(u"subtotalLabel")

        self.hboxLayout1.addWidget(self.subtotalLabel)

        self.totalLineEdit = QLineEdit(HistoryWindow)
        self.totalLineEdit.setObjectName(u"totalLineEdit")
        self.totalLineEdit.setReadOnly(True)

        self.hboxLayout1.addWidget(self.totalLineEdit)

        self.pdvCheckBox = QCheckBox(HistoryWindow)
        self.pdvCheckBox.setObjectName(u"pdvCheckBox")
        self.pdvCheckBox.setChecked(True)

        self.hboxLayout1.addWidget(self.pdvCheckBox)


        self.verticalLayout.addLayout(self.hboxLayout1)

        self.hboxLayout2 = QHBoxLayout()
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.saveButton = QPushButton(HistoryWindow)
        self.saveButton.setObjectName(u"saveButton")

        self.hboxLayout2.addWidget(self.saveButton)

        self.deleteInvoiceButton = QPushButton(HistoryWindow)
        self.deleteInvoiceButton.setObjectName(u"deleteInvoiceButton")

        self.hboxLayout2.addWidget(self.deleteInvoiceButton)

        self.exportPDFButton = QPushButton(HistoryWindow)
        self.exportPDFButton.setObjectName(u"exportPDFButton")

        self.hboxLayout2.addWidget(self.exportPDFButton)

        self.closeButton = QPushButton(HistoryWindow)
        self.closeButton.setObjectName(u"closeButton")

        self.hboxLayout2.addWidget(self.closeButton)


        self.verticalLayout.addLayout(self.hboxLayout2)


        self.retranslateUi(HistoryWindow)

        QMetaObject.connectSlotsByName(HistoryWindow)
    # setupUi

    def retranslateUi(self, HistoryWindow):
        HistoryWindow.setWindowTitle(QCoreApplication.translate("HistoryWindow", u"Povijest faktura", None))
        ___qtablewidgetitem = self.invoicesTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("HistoryWindow", u"Broj fakture", None));
        ___qtablewidgetitem1 = self.invoicesTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("HistoryWindow", u"Klijent", None));
        ___qtablewidgetitem2 = self.invoicesTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("HistoryWindow", u"Datum", None));
        ___qtablewidgetitem3 = self.invoicesTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("HistoryWindow", u"Ukupno s PDV", None));
        self.invoiceInfoGroupBox.setTitle(QCoreApplication.translate("HistoryWindow", u"Podaci o fakturi", None))
        self.invoiceNumberLabel.setText(QCoreApplication.translate("HistoryWindow", u"Broj fakture:", None))
        self.clientLabel.setText(QCoreApplication.translate("HistoryWindow", u"Klijent:", None))
        self.descriptionLabel.setText(QCoreApplication.translate("HistoryWindow", u"Opis:", None))
        self.dateLabel.setText(QCoreApplication.translate("HistoryWindow", u"Datum:", None))
        ___qtablewidgetitem4 = self.itemsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("HistoryWindow", u"Roba / Usluga", None));
        ___qtablewidgetitem5 = self.itemsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("HistoryWindow", u"Koli\u010dina", None));
        ___qtablewidgetitem6 = self.itemsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("HistoryWindow", u"Jedinica", None));
        ___qtablewidgetitem7 = self.itemsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("HistoryWindow", u"Cijena", None));
        ___qtablewidgetitem8 = self.itemsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("HistoryWindow", u"Iznos", None));
        self.addItemButton.setText(QCoreApplication.translate("HistoryWindow", u"+ Dodaj stavku", None))
        self.removeItemButton.setText(QCoreApplication.translate("HistoryWindow", u"- Ukloni stavku", None))
        self.subtotalLabel.setText(QCoreApplication.translate("HistoryWindow", u"Ukupno:", None))
        self.pdvCheckBox.setText(QCoreApplication.translate("HistoryWindow", u"PDV 25%", None))
        self.saveButton.setText(QCoreApplication.translate("HistoryWindow", u"Spremi", None))
        self.deleteInvoiceButton.setText(QCoreApplication.translate("HistoryWindow", u"Obri\u0161i fakturu", None))
        self.exportPDFButton.setText(QCoreApplication.translate("HistoryWindow", u"Export PDF", None))
        self.closeButton.setText(QCoreApplication.translate("HistoryWindow", u"Zatvori", None))
    # retranslateUi

