# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'autorization.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(330, 300)
        Dialog.setStyleSheet(u"#Dialog{\n"
"	background-color: rgb(0,0,0);\n"
"\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	align=\"center\"\n"
"}\n"
"QPushButton{\n"
"	background-color:rgba(0, 170, 0, 1);\n"
"	border:none;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgba(131, 255, 112, 0.5);\n"
"	border:none;\n"
"	color: white;\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color:rgba(0, 170, 127,1);\n"
"	border:none;\n"
"	color: white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.login_input = QLineEdit(Dialog)
        self.login_input.setObjectName(u"login_input")
        self.login_input.setFrame(True)

        self.horizontalLayout_4.addWidget(self.login_input)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.password_input = QLineEdit(Dialog)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setFrame(True)

        self.horizontalLayout_3.addWidget(self.password_input)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.enter_button = QPushButton(Dialog)
        self.enter_button.setObjectName(u"enter_button")
        self.enter_button.setMinimumSize(QSize(120, 50))

        self.horizontalLayout.addWidget(self.enter_button)

        self.exit_button = QPushButton(Dialog)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(120, 50))

        self.horizontalLayout.addWidget(self.exit_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041b\u043e\u0433\u0438\u043d:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u041f\u0430\u0440\u043e\u043b\u044c:", None))
        self.enter_button.setText(QCoreApplication.translate("Dialog", u"\u0412\u043e\u0439\u0442\u0438", None))
        self.exit_button.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

