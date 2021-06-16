from PySide6.QtWidgets import QDialog
from PySide6 import QtCore
from ui.ui_error import Ui_Dialog


class MyError(QDialog):
    def __init__(self):
        super(MyError, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.massage_close)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def set_message(self, string):
        self.ui.label.setText(string)

    def massage_close(self):
        self.close()
