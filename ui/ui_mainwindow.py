# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Application(object):
    def setupUi(self, Application):
        if not Application.objectName():
            Application.setObjectName(u"Application")
        Application.resize(787, 470)
        Application.setStyleSheet(u"")
        self.centralwidget = QWidget(Application)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"    background-image: url(back.jpg);\n"
"	\n"
"}\n"
"\n"
"#listWidget{\n"
"	background-color: transparent;\n"
"	border:none\n"
"}\n"
"\n"
"QScrollBar::Vertical{\n"
"	background-color:rgba(85, 170, 127, 0.4);\n"
"	border:none;\n"
"	width:10px;\n"
"	\n"
"}\n"
"QScrollBar::handle::Vertical{\n"
"	background-color: rgba(131, 255, 112, 0.8);\n"
"	height:100px;\n"
"	min-height: 50px;\n"
"	\n"
"}\n"
"QScrollBar::add-line::vertical{\n"
"	border:none;\n"
"	background:none;\n"
"}\n"
"QScrollBar::sub-line::vertical{\n"
"	border:none;\n"
"	background:none;\n"
"}\n"
"\n"
"QScrollBar::handle::Vertical::hover{\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"}\n"
"QScrollBar::handle::Vertical::pressed{\n"
"	background-color:rgba(0, 170, 0, 1);\n"
"	border:1px ;\n"
"}\n"
"\n"
"QScrollBar::add-Page::vertical,QScrollBar::sub-Page::vertical{\n"
"	background:none;\n"
"}\n"
"QScrollBar::up-arrow::vertical,QScrollBar::down-arrow::vertical{\n"
"	background:none;\n"
"}\n"
"")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(390, 20, 151, 61))
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(580, 20, 151, 61))
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(280, 19, 24, 24))
        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 110, 751, 351))
        self.listWidget.setStyleSheet(u"")
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)
        self.listWidget.setSpacing(5)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(170, 20, 113, 22))
        Application.setCentralWidget(self.centralwidget)

        self.retranslateUi(Application)

        QMetaObject.connectSlotsByName(Application)
    # setupUi

    def retranslateUi(self, Application):
        Application.setWindowTitle(QCoreApplication.translate("Application", u"\u0420\u0430\u0441\u0442\u0435\u043d\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("Application", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Application", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Application", u"\ud83d\udd0d", None))
    # retranslateUi

