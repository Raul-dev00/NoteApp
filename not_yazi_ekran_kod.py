import os

from PyQt5.QtWidgets import *
from not_yazi_ekran import Ui_Form

class YaziEkran(QWidget):
    def __init__(self)->None:
        super().__init__()
        self.yaziekranform = Ui_Form()
        self.yaziekranform.setupUi(self)
        self.yaziekranform.pushButton_kaydet.clicked.connect(self.Kaydet)
        self.secilenMetin=""  #secilen = xMetin.txt
        self.secilenBaslik=""
    def Kaydet(self):
        self.x=0
        baslik=self.yaziekranform.lineEdit.text()
        metin=self.yaziekranform.textEdit.toPlainText()
        dosyalar = [f for f in os.listdir(os.getcwd()) if f.endswith('.txt')]
        for dosya in dosyalar:
            if self.secilenMetin == dosya:
                self.x=1
        if self.x==1 and self.secilenMetin!="":
            with open(self.secilenBaslik, "w", encoding="utf-8") as dosya:
                dosya.write(baslik)
            with open(self.secilenMetin, "w", encoding="utf-8") as dosya:
                dosya.write(metin)
            self.close()
        else:
            dosya_sayisi = len(dosyalar)
            baslik_isim = "Baslik.txt"
            metin_isim = "Metin.txt"
            baslik_isim = str(int(dosya_sayisi/2 + 1)) + baslik_isim
            metin_isim = str(int(dosya_sayisi/2 + 1)) + metin_isim
            with open(baslik_isim, "w", encoding="utf-8") as dosya:
               dosya.write(baslik)
            with open(metin_isim, "w", encoding="utf-8") as dosya:
                dosya.write(metin)
            self.close()
    def notAc(self, secilenNot):
        self.secilenMetin=secilenNot
        with open(secilenNot, "r", encoding="utf-8") as dosya:
            metin=dosya.read()
            self.yaziekranform.textEdit.setPlainText(metin)
        secilen_baslik_uzunluk = len(secilenNot) - 9
        secilen_baslik = secilenNot[:secilen_baslik_uzunluk]
        secilen_baslik += "Baslik.txt"
        self.secilenBaslik=secilen_baslik
        with open(secilen_baslik, "r", encoding="utf-8") as dosya:
            baslik=dosya.read()
            self.yaziekranform.lineEdit.setText(baslik)
