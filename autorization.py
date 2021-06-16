from PySide6.QtWidgets import QDialog
from ui.ui_autorization import Ui_Dialog
from PySide6 import QtCore
from error_message import MyError
from utility import remove_spaces


class Autorization(QDialog):
    def __init__(self, database):
        super(Autorization, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui.enter_button.clicked.connect(self.chek_user)
        self.ui.exit_button.clicked.connect(self.close_dialog)
        self.database = database

    def chek_user(self):
        login = remove_spaces(self.ui.login_input.text())
        password = remove_spaces(self.ui.password_input.text())
        if password == " " or password == "" or login == " " or login == "":
            my_error = MyError()
            my_error.set_message("Заполните все поля!")
            my_error.exec()
        else:
            worker = self.database.get_worker(self.ui.login_input.text(),
                                              self.ui.password_input.text())
            if worker:
                self.accept()
            else:
                my_error = MyError()
                my_error.set_message("Работник не найден!")
                my_error.exec()
                self.ui.password_input.setText("")

    def close_dialog(self):
        self.reject()
