from PySide6.QtGui import QColor
from PySide6.QtWidgets import QListWidgetItem
from plantinform import PlantInform
from error_message import MyError

def fill_list(list_items, items):
    for i in items:
        item = QListWidgetItem(list_items)
        item.setText(i[0])
        list_items.addItem(item)


def fill_none(list_items):
    item = QListWidgetItem(list_items)
    item.setText("нет")
    list_items.addItem(item)

def add_to_list(list_items, text):
    if text == "" or text == " ":
        error_message = MyError()
        error_message.set_message("Поле пустое!")
        error_message.exec()
    else:
        item = QListWidgetItem(list_items)
        item.setText(text)
        list_items.addItem(item)


def delete_from_list(list_item):
    if list_item.selectedItems():
        list_item.takeItem(list_item.row(list_item.currentItem()))
    else:
        error_message = MyError()
        error_message.set_message("Не выбран элемент списка!")
        error_message.exec()

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


def fill_plants(list_plants, plants):
    list_plants.clear()
    for i in plants:
        new_plant = PlantInform(i)
        item = QListWidgetItem(list_plants)
        item.setSizeHint(new_plant.size())
        item.setText(i[1])
        item.setForeground(QColor(0, 0, 0, 0))
        list_plants.addItem(item)
        list_plants.setItemWidget(item, new_plant)


def right_result(string):
    string = remove_spaces(string)
    if string == "" or string == " ":
        return "Неизвестно"
    else:
        return string
