import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Button(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.title = "Special Midterm Exam in OOP"
        self.x = 600
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        self.button = QPushButton('Click to Change Color', self)
        self.button.move(100,120) # button.move(x,y)
        self.button.clicked.connect(self.on_click)
        
        self.show()
        
    @pyqtSlot()
    def on_click(self):
        self.button.setStyleSheet("background-color: yellow;")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Button()
    sys.exit(app.exec_())

