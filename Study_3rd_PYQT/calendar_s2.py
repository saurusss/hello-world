import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()
		
    def initUI(self):
        self.setGeometry(100,100,400,450)
        self.setWindowTitle('Calendar')
        self.setWindowIcon(QIcon('icon.png'))
	
        self.cal = QCalendarWidget(self)
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QDate].connect(self.showDate)

        date = self.cal.selectedDate()
        self.lbl = QLabel(self)
        self.lbl.setText(date.toString())
        self.lbl.move(20, 400)
        

        # StatusBar
        # self.statusBar = QStatusBar(self)
        # self.setStatusBar(self.statusBar)
        


		
    def showDate(self, date):
        self.lbl.setText(date.toString())
        # self.statusBar.showMessage(self, date.toString())
		
def main():

    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
	
if __name__ == '__main__':
    main()