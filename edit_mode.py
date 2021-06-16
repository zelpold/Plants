from PySide6.QtWidgets import QWidget
from error_message import MyError
from ui.ui_edit import Ui_Form
from utility import remove_spaces, fill_plants
from edited_plant import EditPlant


class EditMode(QWidget):

    def __init__(self, database):
        super(EditMode, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.database = database
        plants = self.database.get_plants()
        fill_plants(self.ui.listWidget, plants)
        self.ui.search_button.clicked.connect(self.search)
        self.ui.edit_button.clicked.connect(self.edit_cur)
        self.ui.add_button.clicked.connect(self.add_plant)
        self.ui.delete_button.clicked.connect(self.delete_plant)

    def add_plant(self):
        cur_plant = EditPlant(self.database)
        if cur_plant.exec():
            plants = self.database.get_plants()
            fill_plants(self.ui.listWidget, plants)

    def edit_cur(self):
        cur_plant = EditPlant(self.database)
        cur_plant.set_plant(self.ui.listWidget.currentItem().text())
        if cur_plant.exec():
            plants = self.database.get_plants()
            fill_plants(self.ui.listWidget, plants)

    def delete_plant(self):
        text = self.ui.listWidget.currentItem().text()
        if text:
            self.database.delete_plant(text)
            plants = self.database.get_plants()
            fill_plants(self.ui.listWidget, plants)


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
