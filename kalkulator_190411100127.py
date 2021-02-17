# importan yang digunakan
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import math

current = ""
def display():
    app = QApplication(sys.argv)
    win = QWidget()
    parent = QVBoxLayout()
    display = QLineEdit("")
    display.setAlignment(Qt.AlignRight)
    font = display.font()
    font.setPointSize(font.pointSize() + 8)
    display.setFont(font)

    qh1 = QHBoxLayout()
    button11 = QPushButton("Back")
    button12 = QPushButton("CE")
    button13 = QPushButton("C")
    qh1.addWidget(button11)
    qh1.addWidget(button12)
    qh1.addWidget(button13)
    #############################
    grid = QGridLayout()
    button21 = QPushButton("7")
    button22 = QPushButton("8")
    button23 = QPushButton("9")
    button24 = QPushButton("/")
    button25 = QPushButton("√")
    button31 = QPushButton("4")
    button32 = QPushButton("5")
    button33 = QPushButton("6")
    button34 = QPushButton("*")
    button35 = QPushButton("x²")
    grid.addWidget(button21, 1, 1)
    grid.addWidget(button22, 1, 2)
    grid.addWidget(button23, 1, 3)
    grid.addWidget(button24, 1, 4)
    grid.addWidget(button25, 1, 5)
    grid.addWidget(button31, 2, 1)
    grid.addWidget(button32, 2, 2)
    grid.addWidget(button33, 2, 3)
    grid.addWidget(button34, 2, 4)
    grid.addWidget(button35, 2, 5)
    ############################
    qh2 = QHBoxLayout()
    grid2 = QGridLayout()
    button41 = QPushButton("1")
    button42 = QPushButton("2")
    button43 = QPushButton("3")
    button44 = QPushButton("-")
    button51 = QPushButton("0")
    button52 = QPushButton("+/-")
    button53 = QPushButton(".")
    button54 = QPushButton("+")
    grid2.addWidget(button41, 3, 1)
    grid2.addWidget(button42, 3, 2)
    grid2.addWidget(button43, 3, 3)
    grid2.addWidget(button44, 3, 4)
    grid2.addWidget(button51, 4, 1)
    grid2.addWidget(button52, 4, 2)
    grid2.addWidget(button53, 4, 3)
    grid2.addWidget(button54, 4, 4)
    qh2.addLayout(grid2)
    button55 = QPushButton("=")
    qh2.addWidget(button55)
    ###########################

    def buttonClick1():
        global current
        current = current[:-1]
        display.setText(current)

    def buttonClick2():
        global current
        current = ""
        display.setText(current)

    def buttonClick3():
        win.close()

    def buttonClick4():
        global current
        current += "7"
        display.setText(current)

    def buttonClick5():
        global current
        current += "8"
        display.setText(current)

    def buttonClick6():
        global current
        current += "9"
        display.setText(current)

    def buttonClick7():
        global current
        current += "/"
        display.setText(current)

    def buttonClick8():
        try:
            global current
            current = float(current)
            current = math.sqrt(current)
            current = str(current)
            display.setText(current)
        except:
            display.setText("ERROR")

    def buttonClick9():
        global current
        current += "4"
        display.setText(current)

    def buttonClick10():
        global current
        current += "5"
        display.setText(current)

    def buttonClick11():
        global current
        current += "6"
        display.setText(current)

    def buttonClick12():
        global current
        current += "*"
        display.setText(current)

    def buttonClick13():
        global current
        current = float(current)
        current = current**2
        current = str(current)
        display.setText(current)

    def buttonClick14():
        global current
        current += "1"
        display.setText(current)

    def buttonClick15():
        global current
        current += "2"
        display.setText(current)

    def buttonClick16():
        global current
        current += "3"
        display.setText(current)

    def buttonClick17():
        global current
        current += "-"
        display.setText(current)

    def buttonClick18():
        global current
        current += "0"
        display.setText(current)

    def buttonClick19():
        global current
        current += "-"
        display.setText(current)

    def buttonClick20():
        global current
        current += "."
        display.setText(current)

    def buttonClick21():
        global current
        current += "+"
        display.setText(current)

    def buttonClick22():
        global current
        try:
            current = str(eval(current))
            display.setText(current)
        except:
            display.setText("ERROR")

        ########################
    parent.addWidget(display)
    parent.addLayout(qh1)
    parent.addLayout(grid)
    parent.addLayout(qh2)
    ######CONNECT#########
    button11.clicked.connect(buttonClick1)
    button12.clicked.connect(buttonClick2)
    button13.clicked.connect(buttonClick3)

    button21.clicked.connect(buttonClick4)
    button22.clicked.connect(buttonClick5)
    button23.clicked.connect(buttonClick6)
    button24.clicked.connect(buttonClick7)
    button25.clicked.connect(buttonClick8)
    button31.clicked.connect(buttonClick9)
    button32.clicked.connect(buttonClick10)
    button33.clicked.connect(buttonClick11)
    button34.clicked.connect(buttonClick12)
    button35.clicked.connect(buttonClick13)

    button41.clicked.connect(buttonClick14)
    button42.clicked.connect(buttonClick15)
    button43.clicked.connect(buttonClick16)
    button44.clicked.connect(buttonClick17)
    button51.clicked.connect(buttonClick18)
    button52.clicked.connect(buttonClick19)
    button53.clicked.connect(buttonClick20)
    button54.clicked.connect(buttonClick21)
    button55.clicked.connect(buttonClick22)

    win.setLayout(parent)
    win.show()
    win.setWindowTitle("Tugas_calculator")
    sys.exit(app.exec_())


if __name__ == '__main__':
    display()
