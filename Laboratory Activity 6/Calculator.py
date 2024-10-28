import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMenuBar, QAction, QFileDialog, QMessageBox, QGridLayout
from PyQt5.QtCore import Qt

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        
        buttons = [
            '7', '8', '9', '/', '',
            '4', '5', '6', '*', '',
            '1', '2', '3', '-', '',
            '0', '.', '=', '+', '',
            'sin', 'cos', 'C', '', ''
        ]
        
        self.textLine = QLineEdit(self)
        grid.addWidget(self.textLine, 0, 1, 1, 5)
        
        # Using a loop to generate positions
        positions = [(i, j) for i in range(1, 7) for j in range(1, 6)]
        for position, name in zip(positions, buttons):
            if name == '':
                continue
            button = QPushButton(name)
            button.clicked.connect(self.on_button_clicked)  # Connect button click
            grid.addWidget(button, *position)

        # Set up a central widget
        central_widget = QWidget()
        central_widget.setLayout(grid)
        self.setCentralWidget(central_widget)

        # Create menu bar
        self.menu_bar = self.menuBar()
        file_menu = self.menu_bar.addMenu('Menu Bar (Save or Exit)')

        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_to_file)
        file_menu.addAction(save_action)

        exit_action = QAction('Exit', self)
        exit_action.triggered.connect(self.close)
        exit_action.setShortcut('Ctrl+Q')
        file_menu.addAction(exit_action)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Calculator Program')
        self.show()

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == 'C':
            self.textLine.clear()
        elif text == '=':
            expression = self.textLine.text()
            try:
                result = eval(expression.replace('^', '**'))
                self.textLine.setText(str(result))
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        elif text in ['sin', 'cos']:
            expression = self.textLine.text()
            try:
                if text == 'sin':
                    result = math.sin(math.radians(float(expression)))
                elif text == 'cos':
                    result = math.cos(math.radians(float(expression)))
                self.textLine.setText(str(result))
            except Exception as e:
                QMessageBox.critical(self, "Error", str(e))
        else:
            current_text = self.textLine.text()
            new_text = current_text + text
            self.textLine.setText(new_text)

    def save_to_file(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if filename:
            with open(filename, 'w') as file:
                file.write(self.textLine.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())