# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit_plant.ui'
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
        Dialog.resize(808, 647)
        Dialog.setStyleSheet(u"#widget{background-image:url(back3.jpg);}\n"
"QLabel{font-size:17px; color:rgb(202, 231, 201);}\n"
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
"QScrollBar::handle::Vertical::pressed{\n"
"	background-color:rgba(0, 170, 127,0.8);\n"
"}\n"
"\n"
"QScrollBar::add-Page::vertical,QScrollBar::sub-Page::vertical{\n"
"	background:none;\n"
"}\n"
"QScrollBar::up-arrow::vertical,QScrollBar::down-arrow::vertical{\n"
"	background:none;\n"
"}\n"
"QP"
                        "ushButton{\n"
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
"}")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label, 0, 5, 1, 1)

        self.add_sick_button = QPushButton(self.widget)
        self.add_sick_button.setObjectName(u"add_sick_button")
        self.add_sick_button.setMinimumSize(QSize(100, 25))
        self.add_sick_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.add_sick_button, 8, 6, 1, 1)

        self.category_input = QLineEdit(self.widget)
        self.category_input.setObjectName(u"category_input")

        self.gridLayout.addWidget(self.category_input, 0, 4, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_9.setWordWrap(True)

        self.gridLayout.addWidget(self.label_9, 12, 0, 1, 1)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_7, 5, 3, 1, 2)

        self.list_insects = QListWidget(self.widget)
        self.list_insects.setObjectName(u"list_insects")
        self.list_insects.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.list_insects, 7, 1, 1, 3)

        self.list_sicks = QListWidget(self.widget)
        self.list_sicks.setObjectName(u"list_sicks")
        self.list_sicks.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.list_sicks, 7, 5, 1, 3)

        self.list_parents = QListWidget(self.widget)
        self.list_parents.setObjectName(u"list_parents")
        self.list_parents.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.list_parents, 12, 1, 1, 3)

        self.delete_child_button = QPushButton(self.widget)
        self.delete_child_button.setObjectName(u"delete_child_button")
        self.delete_child_button.setMinimumSize(QSize(100, 25))
        self.delete_child_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.delete_child_button, 13, 7, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.delete_fond_button = QPushButton(self.widget)
        self.delete_fond_button.setObjectName(u"delete_fond_button")
        self.delete_fond_button.setMinimumSize(QSize(100, 25))
        self.delete_fond_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.delete_fond_button, 18, 3, 1, 1)

        self.line_3 = QFrame(self.widget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 4, 0, 1, 8)

        self.sick_input = QLineEdit(self.widget)
        self.sick_input.setObjectName(u"sick_input")

        self.gridLayout.addWidget(self.sick_input, 8, 4, 1, 2)

        self.add_insect_button = QPushButton(self.widget)
        self.add_insect_button.setObjectName(u"add_insect_button")
        self.add_insect_button.setMinimumSize(QSize(100, 25))
        self.add_insect_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.add_insect_button, 8, 2, 1, 1)

        self.list_foundations = QListWidget(self.widget)
        self.list_foundations.setObjectName(u"list_foundations")

        self.gridLayout.addWidget(self.list_foundations, 16, 1, 1, 3)

        self.delete_sick_button = QPushButton(self.widget)
        self.delete_sick_button.setObjectName(u"delete_sick_button")
        self.delete_sick_button.setMinimumSize(QSize(100, 25))
        self.delete_sick_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.delete_sick_button, 8, 7, 1, 1)

        self.insect_input = QLineEdit(self.widget)
        self.insect_input.setObjectName(u"insect_input")

        self.gridLayout.addWidget(self.insect_input, 8, 0, 1, 2)

        self.delete_insect_button = QPushButton(self.widget)
        self.delete_insect_button.setObjectName(u"delete_insect_button")
        self.delete_insect_button.setMinimumSize(QSize(100, 25))
        self.delete_insect_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.delete_insect_button, 8, 3, 1, 1)

        self.line_2 = QFrame(self.widget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 8)

        self.fruit_input = QLineEdit(self.widget)
        self.fruit_input.setObjectName(u"fruit_input")

        self.gridLayout.addWidget(self.fruit_input, 5, 1, 1, 2)

        self.fruit_feature_input = QLineEdit(self.widget)
        self.fruit_feature_input.setObjectName(u"fruit_feature_input")

        self.gridLayout.addWidget(self.fruit_feature_input, 5, 5, 1, 3)

        self.delete_parent_button = QPushButton(self.widget)
        self.delete_parent_button.setObjectName(u"delete_parent_button")
        self.delete_parent_button.setMinimumSize(QSize(100, 25))
        self.delete_parent_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.delete_parent_button, 13, 3, 1, 1)

        self.parent_input = QLineEdit(self.widget)
        self.parent_input.setObjectName(u"parent_input")

        self.gridLayout.addWidget(self.parent_input, 13, 0, 1, 2)

        self.add_fond_button = QPushButton(self.widget)
        self.add_fond_button.setObjectName(u"add_fond_button")
        self.add_fond_button.setMinimumSize(QSize(100, 25))
        self.add_fond_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.add_fond_button, 18, 2, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_8, 7, 4, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.line_4 = QFrame(self.widget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 6, 0, 1, 8)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_4, 7, 0, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_11.setWordWrap(True)

        self.gridLayout.addWidget(self.label_11, 16, 0, 1, 1)

        self.add_parent_button = QPushButton(self.widget)
        self.add_parent_button.setObjectName(u"add_parent_button")
        self.add_parent_button.setMinimumSize(QSize(100, 25))
        self.add_parent_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.add_parent_button, 13, 2, 1, 1)

        self.frost_resistance_input = QLineEdit(self.widget)
        self.frost_resistance_input.setObjectName(u"frost_resistance_input")

        self.gridLayout.addWidget(self.frost_resistance_input, 3, 1, 1, 2)

        self.fond_input = QLineEdit(self.widget)
        self.fond_input.setObjectName(u"fond_input")

        self.gridLayout.addWidget(self.fond_input, 18, 0, 1, 2)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 9, 0, 1, 8)

        self.child_input = QLineEdit(self.widget)
        self.child_input.setObjectName(u"child_input")

        self.gridLayout.addWidget(self.child_input, 13, 4, 1, 2)

        self.list_children = QListWidget(self.widget)
        self.list_children.setObjectName(u"list_children")

        self.gridLayout.addWidget(self.list_children, 12, 5, 1, 3)

        self.add_child_button = QPushButton(self.widget)
        self.add_child_button.setObjectName(u"add_child_button")
        self.add_child_button.setMinimumSize(QSize(100, 25))
        self.add_child_button.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.add_child_button, 13, 6, 1, 1)

        self.name_input = QLineEdit(self.widget)
        self.name_input.setObjectName(u"name_input")

        self.gridLayout.addWidget(self.name_input, 0, 1, 1, 2)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.label_10.setWordWrap(True)

        self.gridLayout.addWidget(self.label_10, 12, 4, 1, 1)

        self.line_5 = QFrame(self.widget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 14, 0, 1, 8)

        self.autor_input = QLineEdit(self.widget)
        self.autor_input.setObjectName(u"autor_input")

        self.gridLayout.addWidget(self.autor_input, 0, 6, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.save_button = QPushButton(self.widget)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(150, 40))
        self.save_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.save_button)

        self.exit_button = QPushButton(self.widget)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setMinimumSize(QSize(150, 40))
        self.exit_button.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.exit_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addWidget(self.widget)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0410\u0432\u0442\u043e\u0440", None))
        self.add_sick_button.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u0445\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438 \u043f\u043b\u043e\u0434\u0430", None))
        self.delete_child_button.setText(QCoreApplication.translate("Dialog", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 ", None))
        self.delete_fond_button.setText(QCoreApplication.translate("Dialog", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_insect_button.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.delete_sick_button.setText(QCoreApplication.translate("Dialog", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.delete_insect_button.setText(QCoreApplication.translate("Dialog", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.delete_parent_button.setText(QCoreApplication.translate("Dialog", u"\u0443\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_fond_button.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0411\u043e\u043b\u0435\u0437\u043d\u0438", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u041c\u043e\u0440\u043e\u0437\u043e\u0443\u0441\u0442\u043e\u0439\u0447\u0438\u0432\u043e\u0441\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0412\u0440\u0435\u0434\u0438\u0442\u0435\u043b\u0438", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u043d\u0430\u043b\u0438\u0447\u0438\u0435 \u0432 \u0441\u0435\u043b\u0435\u043a\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0444\u043e\u043d\u0434\u0430\u0445", None))
        self.add_parent_button.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u043b\u043e\u0434", None))
        self.add_child_button.setText(QCoreApplication.translate("Dialog", u"\u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0447\u0435\u0440\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.save_button.setText(QCoreApplication.translate("Dialog", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.exit_button.setText(QCoreApplication.translate("Dialog", u"\u043e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

