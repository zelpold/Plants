from PySide6.QtWidgets import QWidget
from ui.ui_curplant import Ui_Form
from utility import fill_list, fill_none


class CurPlant(QWidget):
    def __init__(self):
        super(CurPlant, self).__init__()
        self.ui = Ui_Form()
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