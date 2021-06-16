import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QDialog

from error_message import MyError
from ui.uimainwindow import Ui_Application
from ui.ui_plantfrom import Ui_Form
from cur_plant import CurPlant
from autorization import Autorization
from edit_mode import EditMode
from utility import remove_spaces, fill_plants
from data_base_controller import DataBaseController


class PlantInform(QWidget):
    def __init__(self, plant_feature):
        super(PlantInform, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.name.setText(plant_feature[1])
        self.ui.category_name.setText(plant_feature[2])
        self.ui.autor_name.setText(plant_feature[3])


class Application(QMainWindow):
    # инцициализация компонентов и сигналов
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_Application()
        self.ui.setupUi(self)
        self.database = DataBaseController()
        self.edit_window = EditMode(self.database)
        plants = self.database.get_plants()
        self.cur = CurPlant()
        plant, insects, sicks, parents, children, fond = self.database.get_cur_plants(plants[0][1])
        self.cur.change_plants(plant, insects, sicks, parents, children, fond)
        self.ui.verticalLayout.addWidget(self.cur)
        fill_plants(self.ui.listWidget, plants)
        self.ui.listWidget.itemDoubleClicked.connect(self.change_cur_plant)
        self.cur.ui.list_parent.itemDoubleClicked.connect(self.set_selected_parent)
        self.cur.ui.list_children.itemDoubleClicked.connect(self.set_selected_child)
        self.ui.search_button.clicked.connect(self.search)
        self.ui.edit_button.clicked.connect(self.autorization)

    # изменить выбранное растение
    def change_cur_plant(self):
        name = self.ui.listWidget.currentItem().text()
        plant, insects, sicks, parents, children, fond = self.database.get_cur_plants(name)
        self.cur.change_plants(plant, insects, sicks, parents, children, fond)

    def set_selected_parent(self):
        name = self.cur.ui.list_parent.currentItem().text()
        if name != "нет":
            plant, insects, sicks, parents, children, fond = self.database.get_cur_plants(name)
            self.cur.change_plants(plant, insects, sicks, parents, children, fond)

    def set_selected_child(self):
        name = self.cur.ui.list_children.currentItem().text()
        if name != "нет":
            plant, insects, sicks, parents, children, fond = self.database.get_cur_plants(name)
            self.cur.change_plants(plant, insects, sicks, parents, children, fond)

    def autorization(self):
        autorization_window = Autorization(self.database)
        allowing_access = autorization_window.exec()
        if allowing_access == QDialog.Accepted:
            self.edit_window.show()
        else:
            print('отмена')

    # поиск
    def search(self):
        name = remove_spaces(self.ui.name_input.text())
        category = remove_spaces(self.ui.category_input.text())
        autor = remove_spaces(self.ui.autor_input.text())
        self.ui.name_input.setText(name)
        self.ui.category_input.setText(category)
        self.ui.autor_input.setText(autor)

        if (name == "" or name == " ") and (category == "" or category == " ") and (autor == "" or autor == " "):
            my_error = MyError()
            my_error.set_message("Все поля пустые!")
            my_error.exec()
        else:
            plants = self.database.get_plants(name=name, category=category, autor=autor)
            if plants:
                fill_plants(self.ui.listWidget, plants)
            else:
                my_error = MyError()
                my_error.set_message("По вашему запросу ничего не найдено!")
                my_error.exec()

    def update_data(self):
        plants = self.database.get_plants()
        fill_plants(self.ui.listWidget, plants)
        plant, insects, sicks, parents, children, fond = self.database.get_cur_plants(plants[0][1])
        self.cur.change_plants(plant, insects, sicks, parents, children, fond)


if __name__ == "__main__":
    app = QApplication([])
    widget = Application()
    widget.show()
    sys.exit(app.exec())
