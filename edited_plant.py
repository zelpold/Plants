from PySide6.QtWidgets import QDialog
from utility import fill_list, remove_spaces, right_result, add_to_list, delete_from_list
from ui.ui_edit_plant import Ui_Dialog
from error_message import MyError


class EditPlant(QDialog):
    def __init__(self, database):
        super(EditPlant, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.database = database
        self.ui.save_button.clicked.connect(self.chek_inputs)
        self.ui.add_child_button.clicked.connect(self.add_child)
        self.ui.add_parent_button.clicked.connect(self.add_parent)
        self.ui.add_insect_button.clicked.connect(self.add_insect)
        self.ui.add_sick_button.clicked.connect(self.add_sick)
        self.ui.add_fond_button.clicked.connect(self.add_fond)
        self.ui.delete_child_button.clicked.connect(self.delete_child)
        self.ui.delete_parent_button.clicked.connect(self.delete_parent)
        self.ui.delete_insect_button.clicked.connect(self.delete_insect)
        self.ui.delete_sick_button.clicked.connect(self.delete_sick)
        self.ui.delete_fond_button.clicked.connect(self.delete_fond)

    def set_plant(self, name):
        plant, insects, sicks, parents, children, fond = self.database.get_cur_plants(name)
        self.ui.name_input.setText(plant[1])
        self.ui.category_input.setText(plant[2])
        self.ui.autor_input.setText(plant[3])
        self.ui.fruit_input.setText(plant[4])
        self.ui.fruit_feature_input.setText(plant[5])
        self.ui.frost_resistance_input.setText(plant[6])
        self.fill_lists(insects, sicks, parents, children, fond)

    def fill_lists(self, insects, sicks, parents, children, fond):
        self.ui.list_insects.clear()
        self.ui.list_sicks.clear()
        self.ui.list_parents.clear()
        self.ui.list_children.clear()
        self.ui.list_foundations.clear()
        if insects:
            fill_list(self.ui.list_insects, insects)
        if sicks:
            fill_list(self.ui.list_sicks, sicks)
        if parents:
            fill_list(self.ui.list_parents, parents)
        if children:
            fill_list(self.ui.list_children, children)
        if fond:
            fill_list(self.ui.list_foundations, fond)

    def add_child(self):
        text = right_result(self.ui.child_input.text())
        if self.database.plant_exist(text):
            add_to_list(self.ui.list_children, text)
        else:
            error_message = MyError()
            error_message.set_message("Такого сорта нет в базе данных!")
            error_message.exec()

    def add_parent(self):
        text = right_result(self.ui.parent_input.text())
        if self.database.plant_exist(text):
            add_to_list(self.ui.list_parents, text)
        else:
            error_message = MyError()
            error_message.set_message("Такого сорта нет в базе данных!")
            error_message.exec()

    def add_insect(self):
        text = right_result(self.ui.insect_input.text())
        add_to_list(self.ui.list_insects, text)

    def add_sick(self):
        text = right_result(self.ui.sick_input.text())
        add_to_list(self.ui.list_sicks, text)

    def add_fond(self):
        text = right_result(self.ui.fond_input.text())
        add_to_list(self.ui.list_foundations, text)

    def delete_child(self):
        delete_from_list(self.ui.list_children)

    def delete_parent(self):
        delete_from_list(self.ui.list_parents)

    def delete_insect(self):
        delete_from_list(self.ui.list_insects)

    def delete_sick(self):
        delete_from_list(self.ui.list_sicks)

    def delete_fond(self):
        delete_from_list(self.ui.list_foundations)

    def chek_inputs(self):
        name = remove_spaces(self.ui.name_input.text())
        if name == "" or name == " ":
            error_message = MyError()
            error_message.set_message("Название растения - обязательно поле!")
            error_message.exec()
        else:
            category = right_result(self.ui.category_input.text())
            autor = right_result(self.ui.autor_input.text())
            fruit = right_result(self.ui.fruit_input.text())
            fruit_feature = right_result(self.ui.fruit_feature_input.text())
            fruit_resistance = right_result(self.ui.frost_resistance_input.text())
            self.database.update_data(name, category, autor, fruit, fruit_feature, fruit_resistance)
            self.database.update_data_lists(name, self.ui.list_insects, self.ui.list_sicks,
                                            self.ui.list_parents, self.ui.list_children,
                                            self.ui.list_foundations)

            self.accept()
