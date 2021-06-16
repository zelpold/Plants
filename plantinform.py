from ui.ui_plantfrom import Ui_Form
from PySide6.QtWidgets import QWidget


class PlantInform(QWidget):
    def __init__(self, plant_feature):
        super(PlantInform, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.name.setText(plant_feature[1])
        self.ui.category_name.setText(plant_feature[2])
        self.ui.autor_name.setText(plant_feature[3])