import os

from PyQt5.QtWidgets import *
from not_giris_ekran import Ui_MainWindow
from not_yazi_ekran_kod import YaziEkran
from hata_ekran_kod import HataEkran

class GirisEkran(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self.girisekranform = Ui_MainWindow()
        self.girisekranform.setupUi(self)
        self.yaziekran = YaziEkran()
        self.hataekran = HataEkran()
        self.girisekranform.pushButton_not_ekle.clicked.connect(self.notekle)
        self.girisekranform.pushButton_notAc.clicked.connect(self.notac)
        self.comboBox = self.findChild(QComboBox, "comboBox")
        self.dosyalariGoster()

    def notekle(self):
        self.close()
        self.yaziekran.show()
    def dosyalariGoster(self):
        dizin = os.getcwd()
        dosyalar = [f for f in os.listdir(dizin) if f.endswith('Metin.txt')]
        self.comboBox.addItems(dosyalar)
    def notac(self):
        secilen_not = self.comboBox.currentText()
        if secilen_not == "":
            self.hataekran.show()
        else:
            self.close()
            self.yaziekran.notAc(secilen_not)
            self.yaziekran.show()