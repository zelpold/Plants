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
        Application.resize(1032, 648)
        Application.setStyleSheet(u"")
        self.centralwidget = QWidget(Application)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"    background-image: url(back.jpg);\n"
"	\n"
"}\n"
"QListView{\n"
"	background-color:transparent;\n"
"	border:none;\n"
"outline: 0;\n"
"	color: transparent;\n"
"}\n"
"\n"
"QListView::item{\n"
"	background-color: rgba(0, 0, 0, 0.5);\n"
"	border:1px;\n"
"	border-color: rgba(0, 0, 0, 0.5);\n"
"outline: 0;\n"
"}\n"
"\n"
"QListView::item::hover {\n"
"	background-color:rgba(0, 170, 0, 0.5);\n"
"	border:1px;\n"
"	border-color: rgba(0, 0, 0, 0.5);\n"
"outline: 0;\n"
"}\n"
"QListView::item::pressed {\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"	border:1px;\n"
"	border-color: rgba(0, 0, 0, 0.5);\n"
"\n"
"}\n"
"QListView::item::selected {\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"	border:1px;\n"
"	border-color: rgba(0, 0, 0, 0.5);\n"
"	outline: 0;\n"
"}\n"
"QListView::item::focus {\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"	border:1px;\n"
"	border-color: rgba(0, 0, 0, 0.5);\n"
"outline: 0;\n"
"}\n"
"\n"
"#list_plants::item::pressed, #list_plants::item::selected{\n"
"	color: transp"
                        "arent;\n"
"\n"
"}\n"
"\n"
"#scrollArea{\n"
"	background-color: rgba(0,0,0,0.5);\n"
"	border:none;\n"
"}\n"
"#scrollAreaWidgetContents{\n"
"	background-color: rgba(0,0,0,0.5);\n"
"}\n"
"\n"
"#list_plants{\n"
"	background-color: transparent;\n"
"	border:none\n"
"}\n"
"\n"
"QScrollBar::Vertical{\n"
"	background-color:rgba(85, 170, 127, 0.4);\n"
"	border:none;\n"
"	width:10px;\n"
"	\n"
"	\n"
"}\n"
"QScrollBar::handle::Vertical{\n"
"	background-color: rgba(131, 255, 112, 0.8);\n"
"	height:100px;\n"
"	min-height: 50px;\n"
"	\n"
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
"	background-color:rgba(0, 170, 0, 1);\n"
"}\n"
"QScrollBar::handle::Vertical::pressed{\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"	border:1px ;\n"
"}\n"
"\n"
"QScrollBar::add-Page::vertical,QScrollBar::sub-Page::vertical{\n"
"	background:none;\n"
"}\n"
"QScrollBar::up"
                        "-arrow::vertical,QScrollBar::down-arrow::vertical{\n"
"	background:none;\n"
"}\n"
"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton{\n"
"	background-color:rgba(0, 170, 0, 0.5);\n"
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
"}\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(130, 220))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 111, 16))
        self.name_input = QLineEdit(self.widget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(0, 20, 113, 22))
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 50, 111, 16))
        self.autor_input = QLineEdit(self.widget)
        self.autor_input.setObjectName(u"autor_input")
        self.autor_input.setGeometry(QRect(0, 70, 111, 22))
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 100, 111, 16))
        self.category_input = QLineEdit(self.widget)
        self.category_input.setObjectName(u"category_input")
        self.category_input.setGeometry(QRect(0, 120, 111, 22))
        self.search_button = QPushButton(self.widget)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(0, 160, 111, 31))
        self.update_button = QPushButton(self.widget)
        self.update_button.setObjectName(u"update_button")
        self.update_button.setGeometry(QRect(0, 200, 111, 31))
        self.edit_button = QPushButton(self.widget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(0, 240, 111, 31))

        self.horizontalLayout_2.addWidget(self.widget)

        self.list_plants = QListWidget(self.centralwidget)
        self.list_plants.setObjectName(u"list_plants")
        self.list_plants.setMinimumSize(QSize(400, 300))
        self.list_plants.setMaximumSize(QSize(400, 16777215))
        self.list_plants.setStyleSheet(u"")
        self.list_plants.setFrameShape(QFrame.NoFrame)
        self.list_plants.setLineWidth(0)
        self.list_plants.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.list_plants.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.list_plants.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.list_plants.setProperty("isWrapping", False)
        self.list_plants.setResizeMode(QListView.Fixed)
        self.list_plants.setLayoutMode(QListView.Batched)
        self.list_plants.setSpacing(2)
        self.list_plants.setViewMode(QListView.ListMode)
        self.list_plants.setUniformItemSizes(True)
        self.list_plants.setItemAlignment(Qt.AlignTop)

        self.horizontalLayout_2.addWidget(self.list_plants)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(450, 300))
        self.scrollArea.setMaximumSize(QSize(450, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 450, 624))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        Application.setCentralWidget(self.centralwidget)

        self.retranslateUi(Application)

        QMetaObject.connectSlotsByName(Application)
    # setupUi

    def retranslateUi(self, Application):
        Application.setWindowTitle(QCoreApplication.translate("Application", u"\u0420\u0430\u0441\u0442\u0435\u043d\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Application", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Application", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.label_4.setText(QCoreApplication.translate("Application", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.search_button.setText(QCoreApplication.translate("Application", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.update_button.setText(QCoreApplication.translate("Application", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c", None))
        self.edit_button.setText(QCoreApplication.translate("Application", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

