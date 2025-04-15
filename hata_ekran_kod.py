from PyQt5.QtWidgets import *
from hata_ekran import Ui_Dialog

class HataEkran(QDialog):
    def __init__(self)->None:
        super().__init__()
        self.hataekran = Ui_Dialog()
        self.hataekran.setupUi(self)
        self.hataekran.pushButton_OK.clicked.connect(self.OK)
    def OK(self):
        self.close()