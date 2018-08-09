from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class window(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle('test')
        self.resize(250,200)

app=QApplication(sys.argv)
w=window()
w.show()
sys.exit(app.exec())
#sys.exit(app.exec_())