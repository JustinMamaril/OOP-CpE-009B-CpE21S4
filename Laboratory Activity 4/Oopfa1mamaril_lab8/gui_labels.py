import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon

class App(QWidget):
    
    def __init__(self):
        super().__init__() #initializes the main window like in the previous one
        # window - QMainWindow()
        self.title = "PyQt Button"
        self.x = 200 # or left
        self.y = 200 # or top
        self.width = 300
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        self.textboxlbl = QLabel("Hello World! ", self)
        self.textboxlbl.move(125,100)
        self.textboxlbl2 = QLabel("This Program is written in PyCharm", self)
        self.textboxlbl2.move(75,120)
        
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())