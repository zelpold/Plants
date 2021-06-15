# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'curplant.ui'
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
        Form.resize(450, 600)
        Form.setMinimumSize(QSize(0, 591))
        Form.setStyleSheet(u"#Form{background:transparent}")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 450, 601))
        self.widget.setMinimumSize(QSize(0, 591))
        self.widget.setStyleSheet(u"#widget{background-color: transparent}\n"
"#name{font-size:20px; color: rgb(255,255,255)}\n"
"QLabel{color: rgb(255,255,255)}\n"
"#category,#autor,#label,#label_2,#label_3,#label_4,#label_5,#label_7,#label_9,#label_10{font-size:17px; color:rgb(202, 231, 201);}\n"
"#line, #line_2,#line_3,#line_5,#line_6 {\n"
"background-color: rgb(255, 255,255);\n"
"border:none\n"
"}\n"
"\n"
"QListWidget{\n"
"	background-color: transparent;\n"
"	border: none;\n"
"	color: rgb(255,255,255);\n"
"}\n"
"\n"
"\n"
"QScrollBar::Vertical{\n"
"	background-color:rgba(85, 170, 127, 0.4);\n"
"	border:none;\n"
"	width:10px;\n"
"\n"
"	\n"
"}\n"
"QScrollBar::handle::Vertical{\n"
"	background-color: rgba(131, 255, 112, 0.8);\n"
"	height:100px;\n"
"	min-height: 50px;\n"
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
"	background-color:rgba(0, 170, 0, 1);\n"
"}\n"
"QScrollBar::han"
                        "dle::Vertical::pressed{\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"}\n"
"\n"
"QScrollBar::add-Page::vertical,QScrollBar::sub-Page::vertical{\n"
"	background:none;\n"
"}\n"
"QScrollBar::up-arrow::vertical,QScrollBar::down-arrow::vertical{\n"
"	background:none;\n"
"}")
        self.name = QLabel(self.widget)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 0, 151, 51))
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 40, 401, 2))
        self.line.setStyleSheet(u"")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.category = QLabel(self.widget)
        self.category.setObjectName(u"category")
        self.category.setGeometry(QRect(20, 50, 91, 31))
        self.category_name = QLabel(self.widget)
        self.category_name.setObjectName(u"category_name")
        self.category_name.setGeometry(QRect(110, 50, 311, 31))
        self.autor = QLabel(self.widget)
        self.autor.setObjectName(u"autor")
        self.autor.setGeometry(QRect(20, 85, 91, 21))
        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(20, 110, 401, 2))
        self.line_2.setStyleSheet(u"#line{\n"
"background-color: rgb(0, 170, 0);\n"
"border:none\n"
"}\n"
"")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(20, 270, 401, 2))
        self.line_3.setStyleSheet(u"#line{\n"
"background-color: rgb(0, 170, 0);\n"
"border:none\n"
"}\n"
"")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.autor_name = QLabel(self.widget)
        self.autor_name.setObjectName(u"autor_name")
        self.autor_name.setGeometry(QRect(80, 80, 341, 31))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 181, 16))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(220, 120, 201, 20))
        self.list_insects = QListWidget(self.widget)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        QListWidgetItem(self.list_insects)
        self.list_insects.setObjectName(u"list_insects")
        self.list_insects.setGeometry(QRect(20, 140, 191, 88))
        self.list_insects.setLineWidth(0)
        self.list_insects.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_insects.setProperty("isWrapping", False)
        self.list_insects.setWordWrap(True)
        self.list_sicks = QListWidget(self.widget)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        QListWidgetItem(self.list_sicks)
        self.list_sicks.setObjectName(u"list_sicks")
        self.list_sicks.setGeometry(QRect(220, 140, 201, 88))
        self.list_sicks.setLineWidth(0)
        self.list_sicks.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_parent = QListWidget(self.widget)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        QListWidgetItem(self.list_parent)
        self.list_parent.setObjectName(u"list_parent")
        self.list_parent.setGeometry(QRect(20, 310, 191, 91))
        self.list_parent.setLineWidth(0)
        self.list_parent.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_parent.setProperty("isWrapping", False)
        self.list_parent.setWordWrap(True)
        self.list_children = QListWidget(self.widget)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        QListWidgetItem(self.list_children)
        self.list_children.setObjectName(u"list_children")
        self.list_children.setGeometry(QRect(220, 310, 201, 91))
        self.list_children.setLineWidth(0)
        self.list_children.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_children.setProperty("isWrapping", False)
        self.list_children.setWordWrap(True)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 280, 181, 16))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 280, 201, 20))
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 429, 61, 21))
        self.fruit = QLabel(self.widget)
        self.fruit.setObjectName(u"fruit")
        self.fruit.setGeometry(QRect(70, 430, 71, 21))
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 450, 191, 21))
        self.fruit_feature = QLabel(self.widget)
        self.fruit_feature.setObjectName(u"fruit_feature")
        self.fruit_feature.setGeometry(QRect(20, 470, 401, 21))
        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(20, 490, 401, 2))
        self.line_5.setStyleSheet(u"#line{\n"
"background-color: rgb(0, 170, 0);\n"
"border:none\n"
"}\n"
"")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)
        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 500, 271, 21))
        self.list_foundations = QListWidget(self.widget)
        QListWidgetItem(self.list_foundations)
        self.list_foundations.setObjectName(u"list_foundations")
        self.list_foundations.setGeometry(QRect(20, 530, 401, 61))
        self.list_foundations.setLineWidth(0)
        self.list_foundations.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.list_foundations.setProperty("isWrapping", False)
        self.list_foundations.setWordWrap(True)
        self.line_6 = QFrame(self.widget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setGeometry(QRect(20, 420, 401, 2))
        self.line_6.setStyleSheet(u"#line{\n"
"background-color: rgb(0, 170, 0);\n"
"border:none\n"
"}\n"
"")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 230, 171, 31))
        self.frost_resistance = QLabel(self.widget)
        self.frost_resistance.setObjectName(u"frost_resistance")
        self.frost_resistance.setGeometry(QRect(200, 240, 231, 16))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.category.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.category_name.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.autor.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440:", None))
        self.autor_name.setText(QCoreApplication.translate("Form", u"\u0438\u043c\u044f \u0430\u0432\u0442\u043e\u0440\u0430", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u0438", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0411\u043e\u043b\u0435\u0437\u043d\u0438", None))

        __sortingEnabled = self.list_insects.isSortingEnabled()
        self.list_insects.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_insects.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u044c", None));
        ___qlistwidgetitem1 = self.list_insects.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"\u0432\u0440\u0435\u0434\u0438\u0442", None));
        ___qlistwidgetitem2 = self.list_insects.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem3 = self.list_insects.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem4 = self.list_insects.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem5 = self.list_insects.item(5)
        ___qlistwidgetitem5.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 fdsfasdfsafsafsdfsafafds", None));
        ___qlistwidgetitem6 = self.list_insects.item(6)
        ___qlistwidgetitem6.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem7 = self.list_insects.item(7)
        ___qlistwidgetitem7.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem8 = self.list_insects.item(8)
        ___qlistwidgetitem8.setText(QCoreApplication.translate("Form", u"\u0432", None));
        self.list_insects.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.list_sicks.isSortingEnabled()
        self.list_sicks.setSortingEnabled(False)
        ___qlistwidgetitem9 = self.list_sicks.item(0)
        ___qlistwidgetitem9.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u044c", None));
        ___qlistwidgetitem10 = self.list_sicks.item(1)
        ___qlistwidgetitem10.setText(QCoreApplication.translate("Form", u"\u0432\u0440\u0435\u0434\u0438\u0442", None));
        ___qlistwidgetitem11 = self.list_sicks.item(2)
        ___qlistwidgetitem11.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem12 = self.list_sicks.item(3)
        ___qlistwidgetitem12.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem13 = self.list_sicks.item(4)
        ___qlistwidgetitem13.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem14 = self.list_sicks.item(5)
        ___qlistwidgetitem14.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem15 = self.list_sicks.item(6)
        ___qlistwidgetitem15.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem16 = self.list_sicks.item(7)
        ___qlistwidgetitem16.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem17 = self.list_sicks.item(8)
        ___qlistwidgetitem17.setText(QCoreApplication.translate("Form", u"\u0432", None));
        self.list_sicks.setSortingEnabled(__sortingEnabled1)


        __sortingEnabled2 = self.list_parent.isSortingEnabled()
        self.list_parent.setSortingEnabled(False)
        ___qlistwidgetitem18 = self.list_parent.item(0)
        ___qlistwidgetitem18.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u044c", None));
        ___qlistwidgetitem19 = self.list_parent.item(1)
        ___qlistwidgetitem19.setText(QCoreApplication.translate("Form", u"\u0432\u0440\u0435\u0434\u0438\u0442", None));
        ___qlistwidgetitem20 = self.list_parent.item(2)
        ___qlistwidgetitem20.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem21 = self.list_parent.item(3)
        ___qlistwidgetitem21.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem22 = self.list_parent.item(4)
        ___qlistwidgetitem22.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem23 = self.list_parent.item(5)
        ___qlistwidgetitem23.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 fdsfasdfsafsafsdfsafafds", None));
        ___qlistwidgetitem24 = self.list_parent.item(6)
        ___qlistwidgetitem24.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem25 = self.list_parent.item(7)
        ___qlistwidgetitem25.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem26 = self.list_parent.item(8)
        ___qlistwidgetitem26.setText(QCoreApplication.translate("Form", u"\u0432", None));
        self.list_parent.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.list_children.isSortingEnabled()
        self.list_children.setSortingEnabled(False)
        ___qlistwidgetitem27 = self.list_children.item(0)
        ___qlistwidgetitem27.setText(QCoreApplication.translate("Form", u"\u0412\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u044c", None));
        ___qlistwidgetitem28 = self.list_children.item(1)
        ___qlistwidgetitem28.setText(QCoreApplication.translate("Form", u"\u0432\u0440\u0435\u0434\u0438\u0442", None));
        ___qlistwidgetitem29 = self.list_children.item(2)
        ___qlistwidgetitem29.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem30 = self.list_children.item(3)
        ___qlistwidgetitem30.setText(QCoreApplication.translate("Form", u"\u0432", None));
        ___qlistwidgetitem31 = self.list_children.item(4)
        ___qlistwidgetitem31.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem32 = self.list_children.item(5)
        ___qlistwidgetitem32.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442 fdsfasdfsafsafsdfsafafds", None));
        ___qlistwidgetitem33 = self.list_children.item(6)
        ___qlistwidgetitem33.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem34 = self.list_children.item(7)
        ___qlistwidgetitem34.setText(QCoreApplication.translate("Form", u"\u041d\u043e\u0432\u044b\u0439 \u044d\u043b\u0435\u043c\u0435\u043d\u0442", None));
        ___qlistwidgetitem35 = self.list_children.item(8)
        ___qlistwidgetitem35.setText(QCoreApplication.translate("Form", u"\u0432", None));
        self.list_children.setSortingEnabled(__sortingEnabled3)

        self.label_3.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c \u0434\u043b\u044f ", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u041f\u043b\u043e\u0434:", None))
        self.fruit.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u043f\u043b\u043e\u0434\u0430:", None))
        self.fruit_feature.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u043b\u0438\u0447\u0438\u0435 \u0432 \u0441\u0435\u043b\u0435\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0444\u043e\u043d\u0434\u0430\u0445:", None))

        __sortingEnabled4 = self.list_foundations.isSortingEnabled()
        self.list_foundations.setSortingEnabled(False)
        ___qlistwidgetitem36 = self.list_foundations.item(0)
        ___qlistwidgetitem36.setText(QCoreApplication.translate("Form", u"\u043e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442", None));
        self.list_foundations.setSortingEnabled(__sortingEnabled4)

        self.label_10.setText(QCoreApplication.translate("Form", u"\u041c\u043e\u0440\u043e\u0437\u043e\u0443\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0441\u0442\u044c:", None))
        self.frost_resistance.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

