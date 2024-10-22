from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
class chiqar(QWidget):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("font-size:25px;color:white;background-color:#222222")
        self.setFixedSize(450,350)
        self.setWindowTitle("Kankulyator")
    
        self.hisob=QLabel(self)
        self.hisob.move(40,40)

        self.bir=QPushButton("1",self)
        self.bir.move(20,100)
        self.bir.clicked.connect(lambda: self.chiqar(self.bir.text()))

        self.ikki=QPushButton("2",self)
        self.ikki.move(120,100)
        self.ikki.clicked.connect(lambda: self.chiqar(self.ikki.text()))

        self.uch=QPushButton("3",self)
        self.uch.move(220,100)
        self.uch.clicked.connect(lambda: self.chiqar(self.uch.text()))

        self.ayir=QPushButton("-",self)
        self.ayir.move(320,100)
        self.ayir.clicked.connect(lambda: self.chiqar(self.ayir.text()))
        self.ayir.setStyleSheet("color:blue")

        self.tort=QPushButton("4",self)
        self.tort.move(20,150)
        self.tort.clicked.connect(lambda: self.chiqar(self.tort.text()))

        self.besh=QPushButton("5",self)
        self.besh.move(120,150)
        self.besh.clicked.connect(lambda: self.chiqar(self.besh.text()))

        self.olti=QPushButton("6",self)
        self.olti.move(220,150)
        self.olti.clicked.connect(lambda: self.chiqar(self.olti.text()))

        self.pilus=QPushButton("+",self)
        self.pilus.move(320,150)
        self.pilus.clicked.connect(lambda: self.chiqar(self.pilus.text()))
        self.pilus.setStyleSheet("color:blue")

        self.yetti=QPushButton("7",self)
        self.yetti.move(20,200)
        self.yetti.clicked.connect(lambda: self.chiqar(self.yetti.text()))

        self.sakkiz=QPushButton("8",self)
        self.sakkiz.move(120,200)
        self.sakkiz.clicked.connect(lambda: self.chiqar(self.sakkiz.text()))

        self.toqqiz=QPushButton("9",self)
        self.toqqiz.move(220,200)
        self.toqqiz.clicked.connect(lambda: self.chiqar(self.toqqiz.text()))

        self.bolish=QPushButton("/",self)
        self.bolish.move(320,200)
        self.bolish.clicked.connect(lambda: self.chiqar(self.bolish.text()))
        self.bolish.setStyleSheet("color:blue")

        self.tozala=QPushButton("Clear",self)
        self.tozala.move(20,250)
        self.tozala.clicked.connect(self.tozalaa)
        self.tozala.setStyleSheet("color:blue")

        self.nol=QPushButton("0",self)
        self.nol.move(120,250)
        self.nol.clicked.connect(lambda: self.chiqar(self.nol.text()))

        self.tenglik=QPushButton("=",self)
        self.tenglik.move(220,250)
        self.tenglik.clicked.connect(lambda: self.hisobla(self.tenglik.text()))
        self.tenglik.setStyleSheet("color:blue")

        self.kopaytir=QPushButton("*",self)
        self.kopaytir.move(320,250)
        self.kopaytir.clicked.connect(lambda: self.chiqar(self.kopaytir.text()))
        self.kopaytir.setStyleSheet("color:blue")

    def chiqar(self,obj):
        if obj == "/" or obj == "*" or obj == "+":
            if self.hisob.text():
                son=self.hisob.text()+obj
                self.hisob.setStyleSheet("color:red")
                self.hisob.setText(f"{son}")
                self.hisob.adjustSize()
        else:
            son=self.hisob.text()+obj
            self.hisob.setStyleSheet("color:red")
            self.hisob.setText(f"{son}")
            self.hisob.adjustSize()
    def hisobla(self,obj):
        self.hisob.setText(f"{eval(self.hisob.text())}")
        self.hisob.adjustSize()
    def tozalaa(self):
        self.hisob.clear()
        self.hisob.adjustSize()
app=QApplication([])
win=chiqar()
win.show()
app.exec_()