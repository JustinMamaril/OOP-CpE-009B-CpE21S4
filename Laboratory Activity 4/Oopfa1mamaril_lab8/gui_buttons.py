import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
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
        
        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100,70) # button.move (x,y)
        
        # Create a new button named button2
        self.button2 = QPushButton('button2', self)
        self.button2.setToolTip("this button does nothing.. yet..")
        self.button2.move(100,120) # move the new button below the first one
    
        self.show()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())