# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plantform.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(300, 100)
        Form.setMinimumSize(QSize(100, 100))
        Form.setMaximumSize(QSize(300, 100))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(u"#Form{background:transparent;}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setGeometry(QRect(0, 0, 300, 100))
        self.widget.setMinimumSize(QSize(0, 100))
        self.widget.setMaximumSize(QSize(16777215, 100))
        self.widget.setStyleSheet(u"#widget{background-color: rgba(0,0,0,0)}\n"
"#widget::hover{background-color:rgba(0, 170, 0, 0);}\n"
"#widget::pressed{\n"
"background-color:rgba(0, 170, 127,0.8);\n"
"}\n"
"#name{font-size:20px; color: rgb(255,255,255)}\n"
"QLabel {color: rgb(255,255,255)}\n"
"#line{background-color: rgb(255,255,255)}\n"
"#category,#autor{font-size:17px; color:rgb(202, 231, 201);}")
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 10, 291, 21))
        self.category = QLabel(self.widget)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(20, 40, 111, 16))
        self.autor = QLabel(self.widget)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(20, 66, 101, 20))
        self.category_name = QLabel(self.widget)
        self.category_name.setObjectName(u"category_name")
        self.category_name.setGeometry(QRect(110, 42, 131, 16))
        self.autor_name = QLabel(self.widget)
        self.autor_name.setObjectName(u"autor_name")
        self.autor_name.setGeometry(QRect(80, 70, 141, 16))
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 33, 260, 2))
        self.line.setStyleSheet(u"#line{\n"
"background-color: rgb(255,255,255);\n"
"border:none\n"
"}")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.category.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.autor.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440:", None))
        self.category_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.autor_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

