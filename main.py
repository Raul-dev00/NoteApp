from PyQt5.QtWidgets import QApplication
from not_giris_ekran_kod import GirisEkran

app = QApplication([])
window = GirisEkran()
window.show()
app.exec_()