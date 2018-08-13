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

# stock code load  https://wikidocs.net/5236       
# sc = pd.read_csv('c:\\TEMP\\stock.csv', index_col=0)
    
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(600, 200, 1200, 600)
        self.setWindowTitle("PyChart Viewer v0.1")
        self.setWindowIcon(QIcon('stock.png'))
        # 변수 정의
        # 종목 입력 결과  
        self.labelMkt = QLabel(self)
        self.labelMkt.setText("종목코드 입력")
        # 차트 그리기 버튼
        self.pushButtonDraw = QPushButton("차트그리기")
        self.pushButtonDraw.clicked.connect(self.pushButtonDrawClicked) 

        # 화면 리셋 버튼
        self.pushButtonReset = QPushButton("화면 리셋")
        self.pushButtonReset.clicked.connect(self.pushButtonResetClicked)        
        
        # 종목코드입력
        self.lineEditStock = QLineEdit("", self)
        self.lineEditStock.returnPressed.connect(self.lineEditReturnPressed)
        self.lineEditStock.textChanged.connect(self.lineEditChanged)
        # 자주사용되는 QLineEdit signal
        # textChanged( )   QLineEdit 객체에서 텍스트가 변경될 때 발생
        # returnPressed( ) QLineEdit 객체를 통해 사용자가 엔터키를 눌렀을 때
        self.labelStockname = QLabel("종목 미선택", self) #  코드 입력된 종목 이름 표시
        # 시장 선택
        groupBox1 = QGroupBox("시장구분", self)
        self.radio1 = QRadioButton("KOSPI", self)
        self.radio1.setChecked(True)
        self.radio1.clicked.connect(self.radioButtonClicked)
        self.radio2 = QRadioButton("KOSDAQ", self)
        self.radio2.clicked.connect(self.radioButtonClicked)
        # self.radio1.textChanged(self.radiotextChanged)
        # self.radio2.textChanged(self.radiotextChanged)
        
        # 기간 선택
        self.startDate = QLineEdit(str(datetime.date.today().year-1)+"-01-01", self)
        self.endDate = QLineEdit(str(datetime.date.today()), self)
        self.labelDateStatus = QLabel("날짜입력", self)
        self.startDate.returnPressed.connect(self.dateReturnPressed)
        self.endDate.returnPressed.connect(self.dateReturnPressed)
        # self.startDate.textChanged.connect(self.dateEditChanged)

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
        rightInner1.addWidget(self.labelMkt)
        groupBox1.setLayout(rightInner1)
            # 기간 입력
        rightInner2 = QVBoxLayout()
        rightInner2.addWidget(self.startDate)
        rightInner2.addWidget(self.endDate)
        rightInner2.addWidget(self.labelDateStatus)
        groupBox2.setLayout(rightInner2)
            # 우측 전체 박스 구성
        rightLayout = QVBoxLayout()
        rightLayout.addWidget(self.pushButtonDraw)
        rightLayout.addWidget(self.lineEditStock)
        rightLayout.addWidget(self.labelStockname)
        rightLayout.addWidget(groupBox1)
        rightLayout.addWidget(groupBox2)
        rightLayout.addWidget(self.pushButtonReset)
        rightLayout.addStretch(1)
        #전체구성
        self.layout = QHBoxLayout()
        self.layout.addLayout(leftLayout)
        self.layout.addLayout(rightLayout)
        self.layout.setStretchFactor(leftLayout, 1)
        self.layout.setStretchFactor(rightLayout, 0)

        self.setLayout(self.layout)

    def pushButtonResetClicked(self):
        # pass
        del self.fig
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)
        self.canvas.draw()
        self.setLayout(self.layout)
        # ax = self.fig.add_subplot(111) -오류 발생
        # self.canvas.draw()
        # self.ax = plt.Figure()
        # self.canvas = FigureCanvas(self.fig)
        # self.canvas.draw()
        
    def pushButtonDrawClicked(self):
        # code = self.lineEditStock.text()

        if self.radio1.isChecked():
            ticker = self.lineEditStock.text() + '.KS'
        else:
            ticker = self.lineEditStock.text() + '.KQ'
        
        sDate = str(datetime.datetime.strptime(self.startDate.text(), "%Y-%m-%d").date())
        eDate = str(datetime.datetime.strptime(self.endDate.text(), "%Y-%m-%d").date())
        
        try:
            df = web.get_data_yahoo(ticker, sDate, eDate)
            # print(df)
            df['MA20'] = df['Adj Close'].rolling(window=20).mean()
            df['MA60'] = df['Adj Close'].rolling(window=60).mean()

            self.ax = self.fig.add_subplot(111)
            self.ax.plot(df.index, df['Adj Close'], label='Adj Close')
            self.ax.plot(df.index, df['MA20'], label='MA20')
            self.ax.plot(df.index, df['MA60'], label='MA60')
            self.ax.legend(loc='upper right')
            self.ax.grid()

            self.canvas.draw()

        except:
            self.labelMkt.setText("시장구분을 점검해주세요")

    def radioButtonClicked(self):
        msg = ""
        if self.radio1.isChecked():
            msg = "KS"
        else:
            msg = "KQ"
        self.labelMkt.setText(msg)

    def lineEditChanged(self):
        # sname = self.sc.loc['A' + self.lineEditStock.text()]
        # print(sname)
        self.labelStockname.setText(self.lineEditStock.text())

    def lineEditReturnPressed(self):
        self.sinput =  self.lineEditStock.text()
        self.scode =  'A' + self.sinput 
        try:
            sc = pd.read_csv('c:\\TEMP\\stock.csv', index_col=0)
            self.labelStockname.setText(sc.ix[self.scode].stock_name)
        except  KeyError as err1:
            try:
                sn = pd.read_csv('c:\\TEMP\\stockn.csv', index_col=0) 
                s_result = (sn.ix[self.sinput].stock_code)
                self.lineEditStock.setText(s_result[1:])
                self.labelStockname.setText(self.sinput)
            except:
                self.labelStockname.setText("해당 종목 없음!")
            
        except:
            self.labelStockname.setText("입력 오류!!!")
            
    def dateReturnPressed(self):
        try:
            sd = datetime.datetime.strptime(self.startDate.text(), '%Y-%m-%d')
            ed = datetime.datetime.strptime(self.endDate.text(), '%Y-%m-%d')

            if sd > ed:
                raise ValueError("시작일자가 종료일자보다 늦습니다")
            # self.labelDateStatus.setText(self.startDate.text() + "~" + self.endDate.text())
            self.labelDateStatus.setText(self.startDate.text() + " ~ " + self.endDate.text())
        # except ValueError:
        except ValueError as err1:
            # print(err1)
            self.labelDateStatus.setText(str(err1))  
        except:
            # raise ValueError("Incorrect data format, should be YYYY-MM-DD")
            self.labelDateStatus.setText("Incorrect data format, should be YYYY-MM-DD")   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()