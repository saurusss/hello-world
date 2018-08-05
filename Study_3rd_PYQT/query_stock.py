import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas_datareader.data as web
import fix_yahoo_finance as yf
yf.pdr_override()
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import datetime

from pandas import Series, DataFrame

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        self.setWindowIcon(QIcon('stock.png'))

        # 결과 확인 
        statusLabel = QLabel(self)
        statusLabel.setText("시작")
        
        self.pushButton = QPushButton("차트그리기")

        #종목코드입력
        self.lineEdit = QLineEdit()
        self.pushButton.clicked.connect(self.pushButtonClicked)
        
        # 시장 선택
        groupBox = QGroupBox("시장구분", self)
        self.radio1 = QRadioButton("KOSPI", self)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton("KOSDAQ", self)
        self.radio2.clicked.connect(self.radioButtonClicked)


        # 시작 일자 선택
        # 시장 선택
        groupBox = QGroupBox("조회기간", self)
        self.radio1 = QRadioButton("KOSPI", self)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)

        self.radio2 = QRadioButton("KOSDAQ", self)
        self.radio2.clicked.connect(self.radioButtonClicked)


        # 종료 일자 선택
        
        


        # Left Layout
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
        

        rightInnerLayout = QVBoxLayout()
        rightInnerLayout.addWidget(self.radio1)
        rightInnerLayout.addWidget(self.radio2)
        groupBox.setLayout(rightInnerLayout)

        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton)
        rightLayout.addWidget(self.lineEdit)
        rightLayout.addWidget(groupBox)
        rightLayout.addWidget(statusLabel)
        rightLayout.addStretch(1)

        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        code = self.lineEdit.text()
        #df = web.DataReader(code, "yahoo")
        ticker = code + '.KS'
       
        df = web.get_data_yahoo(ticker, '2017-01-01')
        df['MA20'] = df['Adj Close'].rolling(window=20).mean()
        df['MA60'] = df['Adj Close'].rolling(window=60).mean()

        ax = self.fig.add_subplot(111)
        ax.plot(df.index, df['Adj Close'], label='Adj Close')
        ax.plot(df.index, df['MA20'], label='MA20')
        ax.plot(df.index, df['MA60'], label='MA60')
        ax.legend(loc='upper right')
        ax.grid()

        self.canvas.draw()

    def radioButtonClicked(self):
        msg = ""
        if self.radio1.isChecked():
            msg = "KS"
        else:
            msg = "KQ"
        self.statusLabel.setText(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()