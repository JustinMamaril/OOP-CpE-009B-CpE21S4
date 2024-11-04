import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout

class MyWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Midterm Exam in OOP")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        h_layout1 = QHBoxLayout()
        self.label1 = QLabel("Enter your fullname:")
        self.label1.setStyleSheet("color: red;")
        self.entry1 = QLineEdit()
        h_layout1.addWidget(self.label1)
        h_layout1.addWidget(self.entry1)


        h_layout2 = QHBoxLayout()
        self.button = QPushButton("Click to display your Fullname")
        self.button.setStyleSheet("color: red;")
        self.button.clicked.connect(self.display)
        self.entry2 = QLineEdit()
        h_layout2.addWidget(self.button)
        h_layout2.addWidget(self.entry2)


        layout.addLayout(h_layout1)
        layout.addLayout(h_layout2)

        self.setLayout(layout)
        
    def display(self):
        self.entry2.setText(self.entry1.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())