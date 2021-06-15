import sys
import pymysql.cursors
from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QListWidgetItem, QDialog
from PySide6.QtGui import QColor
from uimainwindow import Ui_Application
from ui_plantfrom import Ui_Form
from ui_curplant import Ui_Form as Cur
from ui_error import Ui_Dialog


class BdController:
    def __init__(self):
        try:
            self.connection = pymysql.connect(host="217.28.221.3", port=3306,
                                              user="leonid", password="Leopoya00*",
                                              db='plants')
            self.cursor = self.connection.cursor()
            self.connection.close()
        except pymysql.Error as e:
            print(e)

    def get_plants(self, name=" ", category=" ", autor=" "):
        self.connect_bd()
        flag = False
        q_string = "SELECT * From sorts"
        if name != " ":
            q_string += " WHERE name LIKE \'%" + name + "%\'"
            flag = True
        if category != " ":
            if flag:
                q_string += " AND category LIKE \'%" + category + "%\'"
            else:
                flag = True
                q_string += " WHERE category LIKE \'%" + category + "%\'"
        if autor != " ":
            if flag:
                q_string += " AND autor LIKE \'%" + autor + "%\'"
            else:
                q_string += " WHERE autor LIKE \'%" + autor + "%\'"
        self.cursor.execute(q_string)
        plants = self.cursor.fetchall()
        self.connect_close()
        return plants

    def get_cur_plants(self, name):
        self.connect_bd()
        self.cursor.execute("SELECT * From sorts WHERE name = \'" + name + "\'")
        plant = self.cursor.fetchall()
        self.cursor.execute("SELECT insect From insects WHERE sort = \'" + name + "\'")
        insects = self.cursor.fetchall()
        self.cursor.execute("SELECT sick From sicks WHERE sort = \'" + name + "\'")
        sicks = self.cursor.fetchall()
        self.cursor.execute("SELECT parent From parents WHERE child = \'" + name + "\'")
        parents = self.cursor.fetchall()
        self.cursor.execute("SELECT child From parents WHERE parent = \'" + name + "\'")
        children = self.cursor.fetchall()
        self.cursor.execute("SELECT fond From fonds WHERE sort = \'" + name + "\'")
        fond = self.cursor.fetchall()
        self.connect_close()
        return plant[0], insects, sicks, parents, children, fond

    def connect_bd(self):
        self.connection = pymysql.connect(host="217.28.221.3", port=3306,
                                          user="leonid", password="Leopoya00*",
                                          db='plants')
        self.cursor = self.connection.cursor()

    def connect_close(self):
        self.connection.close()


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


class PlantInform(QWidget):
    def __init__(self, plant_feature):
        super(PlantInform, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.name.setText(plant_feature[1])
        self.ui.category_name.setText(plant_feature[2])
        self.ui.autor_name.setText(plant_feature[3])


def fill_list(list_items, items):
    for i in items:
        item = QListWidgetItem(list_items)
        item.setText(i[0])
        list_items.addItem(item)


def fill_none(list_items):
    item = QListWidgetItem(list_items)
    item.setText("нет")
    list_items.addItem(item)


def remove_spaces(string: str):
    if len(string) <= 1:
        return string
    string = list(string)
    j = 1
    for i in range(1, len(string)):
        if string[i] == " " and string[i-1] == " ":
            pass
        else:
            string[j] = string[i]
            j += 1
    return ''.join(string[:j])


class CurPlant(QWidget):
    def __init__(self):
        super(CurPlant, self).__init__()
        self.ui = Cur()
        self.ui.setupUi(self)

    def change_plants(self, plant_feature, insects, sicks, parents, children, fond):
        self.ui.name.setText(plant_feature[1])
        self.ui.category_name.setText(plant_feature[2])
        self.ui.autor_name.setText(plant_feature[3])
        self.ui.fruit.setText(plant_feature[4])
        self.ui.fruit_feature.setText(plant_feature[5])
        self.ui.frost_resistance.setText(plant_feature[6])
        self.ui.list_insects.clear()
        self.ui.list_sicks.clear()
        self.ui.list_parent.clear()
        self.ui.list_children.clear()
        self.ui.list_foundations.clear()
        if insects:
            fill_list(self.ui.list_insects, insects)
        else:
            fill_none(self.ui.list_insects)
        if sicks:
            fill_list(self.ui.list_sicks, sicks)
        else:
            fill_none(self.ui.list_sicks)
        if parents:
            fill_list(self.ui.list_parent, parents)
        else:
            fill_none(self.ui.list_parent)
        if children:
            fill_list(self.ui.list_children, children)
        else:
            fill_none(self.ui.list_children)
        if fond:
            fill_list(self.ui.list_foundations, fond)
        else:
            fill_none(self.ui.list_foundations)


class Application(QMainWindow):
    # инцициализация компонентов и сигналов
    def __init__(self):
        super(Application, self).__init__()
        self.ui = Ui_Application()
        self.ui.setupUi(self)
        self.bd = BdController()
        plants = self.bd.get_plants()
        self.cur = CurPlant()
        plant, insects, sicks, parents, children, fond = self.bd.get_cur_plants(plants[0][1])
        self.cur.change_plants(plant, insects, sicks, parents, children, fond)
        self.ui.verticalLayout.addWidget(self.cur)
        self.fil_plants(plants)
        self.ui.listWidget.currentItemChanged.connect(self.change_cur_plant)
        self.cur.ui.list_parent.itemDoubleClicked.connect(self.set_selected_parent)
        self.cur.ui.list_children.itemDoubleClicked.connect(self.set_selected_child)
        self.ui.pushButton.clicked.connect(self.add_plant)
        self.ui.search_button.clicked.connect(self.search)

    def add_plant(self):
        new_plant = PlantInform(["1", "название", "категория", "автор"])
        item = QListWidgetItem(self.ui.listWidget)
        item.setSizeHint(new_plant.size())
        self.ui.listWidget.addItem(item)
        self.ui.listWidget.setItemWidget(item, new_plant)

    # изменить выбранное растение
    def change_cur_plant(self):
        name = self.ui.listWidget.currentItem().text()
        plant, insects, sicks, parents, children, fond = self.bd.get_cur_plants(name)
        self.cur.change_plants(plant, insects, sicks, parents, children, fond)

    def set_selected_parent(self):
        name = self.cur.ui.list_parent.currentItem().text()
        if name != "нет":
            plant, insects, sicks, parents, children, fond = self.bd.get_cur_plants(name)
            self.cur.change_plants(plant, insects, sicks, parents, children, fond)

    def set_selected_child(self):
        name = self.cur.ui.list_children.currentItem().text()
        if name != "нет":
            plant, insects, sicks, parents, children, fond = self.bd.get_cur_plants(name)
            self.cur.change_plants(plant, insects, sicks, parents, children, fond)

    # заполнить список растений
    def fil_plants(self, plants):
        self.ui.listWidget.clear()
        for i in plants:
            new_plant = PlantInform(i)
            item = QListWidgetItem(self.ui.listWidget)
            item.setSizeHint(new_plant.size())
            item.setText(i[1])
            item.setForeground(QColor(0, 0, 0, 0))
            self.ui.listWidget.addItem(item)
            self.ui.listWidget.setItemWidget(item, new_plant)

    # поиск
    def search(self):
        name = remove_spaces(self.ui.name_input.text())
        category = remove_spaces(self.ui.category_input.text())
        autor = remove_spaces(self.ui.autor_input.text())

        if (name == "" or name == " ") and (category == "" or category == " ") and (autor == "" or autor == " "):
            my_error = MyError()
            my_error.set_message("Все поля пустые")
            my_error.exec()

        else:
            plants = self.bd.get_plants(name=name,
                                        category=category,
                                        autor=autor)
            if plants:
                self.fil_plants(plants)
            else:
                my_error = MyError()
                my_error.set_message("По вашемузапросу ничего не найдено")
                my_error.exec()


if __name__ == "__main__":
    app = QApplication([])
    widget = Application()
    widget.show()
    sys.exit(app.exec())
