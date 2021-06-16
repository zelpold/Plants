# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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
        Form.setWindowModality(Qt.WindowModal)
        Form.resize(647, 591)
        Form.setStyleSheet(u"#widget_2 {\n"
"	background-image: url(back2.jpg);\n"
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
"#listWidget::item::pressed, #listWidget::item::selected{\n"
"	color: transparent;\n"
"\n"
""
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
"QScrollBar::up-arrow::vertical,"
                        "QScrollBar::down-arrow::vertical{\n"
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
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.widget = QWidget(self.widget_2)
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

        self.horizontalLayout_2.addWidget(self.widget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.listWidget = QListWidget(self.widget_2)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(400, 300))
        self.listWidget.setMaximumSize(QSize(400, 16777215))
        self.listWidget.setStyleSheet(u"")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.listWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setResizeMode(QListView.Fixed)
        self.listWidget.setLayoutMode(QListView.Batched)
        self.listWidget.setSpacing(2)
        self.listWidget.setViewMode(QListView.ListMode)
        self.listWidget.setUniformItemSizes(True)
        self.listWidget.setItemAlignment(Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.listWidget)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.edit_button = QPushButton(self.widget_2)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.edit_button)

        self.add_button = QPushButton(self.widget_2)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.add_button)

        self.delete_button = QPushButton(self.widget_2)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_3.addWidget(self.delete_button)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.search_button.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.edit_button.setText(QCoreApplication.translate("Form", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.add_button.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_button.setText(QCoreApplication.translate("Form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

