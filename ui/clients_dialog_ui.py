# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clients_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHBoxLayout,
    QHeaderView, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_ClientsDialog(object):
    def setupUi(self, ClientsDialog):
        if not ClientsDialog.objectName():
            ClientsDialog.setObjectName(u"ClientsDialog")
        ClientsDialog.resize(700, 400)
        self.mainLayout = QVBoxLayout(ClientsDialog)
        self.mainLayout.setObjectName(u"mainLayout")
        self.clientsTableWidget = QTableWidget(ClientsDialog)
        if (self.clientsTableWidget.columnCount() < 5):
            self.clientsTableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.clientsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.clientsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.clientsTableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.clientsTableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.clientsTableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.clientsTableWidget.setObjectName(u"clientsTableWidget")
        self.clientsTableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.clientsTableWidget.setRowCount(0)
        self.clientsTableWidget.setColumnCount(5)

        self.mainLayout.addWidget(self.clientsTableWidget)

        self.buttonsLayout = QHBoxLayout()
        self.buttonsLayout.setObjectName(u"buttonsLayout")
        self.addClientButton = QPushButton(ClientsDialog)
        self.addClientButton.setObjectName(u"addClientButton")

        self.buttonsLayout.addWidget(self.addClientButton)

        self.editClientButton = QPushButton(ClientsDialog)
        self.editClientButton.setObjectName(u"editClientButton")

        self.buttonsLayout.addWidget(self.editClientButton)

        self.deleteClientButton = QPushButton(ClientsDialog)
        self.deleteClientButton.setObjectName(u"deleteClientButton")

        self.buttonsLayout.addWidget(self.deleteClientButton)

        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.buttonsLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(ClientsDialog)
        self.closeButton.setObjectName(u"closeButton")

        self.buttonsLayout.addWidget(self.closeButton)


        self.mainLayout.addLayout(self.buttonsLayout)


        self.retranslateUi(ClientsDialog)

        QMetaObject.connectSlotsByName(ClientsDialog)
    # setupUi

    def retranslateUi(self, ClientsDialog):
        ClientsDialog.setWindowTitle(QCoreApplication.translate("ClientsDialog", u"Klijenti", None))
        ___qtablewidgetitem = self.clientsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ClientsDialog", u"Naziv", None));
        ___qtablewidgetitem1 = self.clientsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ClientsDialog", u"OIB", None));
        ___qtablewidgetitem2 = self.clientsTableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ClientsDialog", u"Adresa", None));
        ___qtablewidgetitem3 = self.clientsTableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ClientsDialog", u"Telefon", None));
        ___qtablewidgetitem4 = self.clientsTableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ClientsDialog", u"Email", None));
        self.addClientButton.setText(QCoreApplication.translate("ClientsDialog", u"Dodaj", None))
        self.editClientButton.setText(QCoreApplication.translate("ClientsDialog", u"Uredi", None))
        self.deleteClientButton.setText(QCoreApplication.translate("ClientsDialog", u"Obri\u0161i", None))
        self.closeButton.setText(QCoreApplication.translate("ClientsDialog", u"Zatvori", None))
    # retranslateUi

