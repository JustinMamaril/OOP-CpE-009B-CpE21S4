import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle("Account Registration System")
        self.setStyleSheet("background-color: #DCB494;")
        
        # Program title
        self.program_title = QLabel("<b>Account Registration Form</b>")
        self.program_title.setFont(QFont("Arial Narrow", 16))
        self.program_title.setAlignment(Qt.AlignCenter)

        # Create form layout
        self.form_layout = QVBoxLayout()
        self.form_layout.addWidget(self.program_title)

        # First name
        self.first_name_label = QLabel("First Name:")
        self.first_name_input = QLineEdit()
        self.first_name_layout = QHBoxLayout()
        self.first_name_layout.addWidget(self.first_name_label)
        self.first_name_layout.addWidget(self.first_name_input)
        self.form_layout.addLayout(self.first_name_layout)

        # Last name
        self.last_name_label = QLabel("Last Name:")
        self.last_name_input = QLineEdit()
        self.last_name_layout = QHBoxLayout()
        self.last_name_layout.addWidget(self.last_name_label)
        self.last_name_layout.addWidget(self.last_name_input)
        self.form_layout.addLayout(self.last_name_layout)

        # Username
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        self.username_layout = QHBoxLayout()
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_input)
        self.form_layout.addLayout(self.username_layout)

        # Password
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_layout = QHBoxLayout()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_input)
        self.form_layout.addLayout(self.password_layout)

        # Email address
        self.email_label = QLabel("Email Address:")
        self.email_input = QLineEdit()
        self.email_layout = QHBoxLayout()
        self.email_layout.addWidget(self.email_label)
        self.email_layout.addWidget(self.email_input)
        self.form_layout.addLayout(self.email_layout)

        # Contact number
        self.contact_number_label = QLabel("Contact Number:")
        self.contact_number_input = QLineEdit()
        self.contact_number_layout = QHBoxLayout()
        self.contact_number_layout.addWidget(self.contact_number_label)
        self.contact_number_layout.addWidget(self.contact_number_input)
        self.form_layout.addLayout(self.contact_number_layout)

        # Submit and clear buttons
        self.submit_button = QPushButton("Submit")
        self.clear_button = QPushButton("Clear")
        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.submit_button)
        self.button_layout.addStretch()
        self.button_layout.addWidget(self.clear_button)
        self.form_layout.addLayout(self.button_layout)

        self.setLayout(self.form_layout)

        # Center the window
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    registration_form = RegistrationForm()
    registration_form.show()
    sys.exit(app.exec_())