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
    # 변수 정의
        # 결과 확인 
        self.statusLabel = QLabel(self)
        self.statusLabel.setText("시작")
        # 차트 그림 버튼
        self.pushButton = QPushButton("차트그리기")
        self.pushButton.clicked.connect(self.pushButtonClicked)        
        # 종목코드입력
        self.lineEdit1 = QLineEdit()
        #self.pushButton.clicked.connect(self.pushButtonClicked)
        # 시장 선택
        groupBox1 = QGroupBox("시장구분", self)
        self.radio1 = QRadioButton("KOSPI", self)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)
        self.radio2 = QRadioButton("KOSDAQ", self)
        self.radio2.clicked.connect(self.radioButtonClicked)
        
        # 기간 선택
        self.startDate = QLineEdit()
        self.endDate = QLineEdit()
        print(self.startDate, self.endDate)
        groupBox2 = QGroupBox("조회기간", self)

        # Left Layout
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)

        leftLayout = QVBoxLayout()
        leftLayout.addWidget(self.canvas)

        # Right Layout
            # 시장 선택 
        rightInner1 = QVBoxLayout()
        rightInner1.addWidget(self.radio1)
        rightInner1.addWidget(self.radio2)
        groupBox1.setLayout(rightInner1)
            # 기간 입력
        rightInner2 = QVBoxLayout()
        rightInner2.addWidget(self.startDate)
        rightInner2.addWidget(self.endDate)
        groupBox2.setLayout(rightInner2)
            # 우측 박스 구성
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButton)
        rightLayout.addWidget(self.lineEdit1)
        rightLayout.addWidget(groupBox1)
        rightLayout.addWidget(groupBox2)
        rightLayout.addWidget(self.statusLabel)
        rightLayout.addStretch(1)
        #전체구성
        layout = QHBoxLayout()
        layout.addLayout(leftLayout)
        layout.addLayout(rightLayout)
        layout.setStretchFactor(leftLayout, 1)
        layout.setStretchFactor(rightLayout, 0)

        self.setLayout(layout)

    def pushButtonClicked(self):
        code = self.lineEdit1.text()
        #df = web.DataReader(code, "yahoo")
        ticker = code + '.KS'
        a = self.startDate
        b = self.endDate
        print(a,b)
        # sDate = datetime.datetime.strptime(self.startDate, "%Y-%m-%d").date()
        # eDate = datetime.datetime.strptime(self.endDate, "%Y-%m-%d").date()
        
        df = web.get_data_yahoo(ticker, a)
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