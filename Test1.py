import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit


class HomePage(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel("Welcome to the Homepage")
        self.layout.addWidget(self.label)

        self.button1 = QPushButton("Page 1")
        self.button1.clicked.connect(self.show_page1)
        self.layout.addWidget(self.button1)

        self.button2 = QPushButton("Page 2")
        self.button2.clicked.connect(self.show_page2)
        self.layout.addWidget(self.button2)

        self.button3 = QPushButton("Page 3")
        self.button3.clicked.connect(self.show_page3)
        self.layout.addWidget(self.button3)

        self.setLayout(self.layout)

    def show_page1(self):
        self.page1 = Page1()
        self.page1.show()

    def show_page2(self):
        self.page2 = Page2()
        self.page2.show()

    def show_page3(self):
        self.page3 = Page3()
        self.page3.show()


class Page1(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel("Page 1")
        self.layout.addWidget(self.label)

        self.name_label = QLabel("Enter your name:")
        self.layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        self.layout.addWidget(self.name_input)

        self.setLayout(self.layout)


class Page2(QWidget):
    def __init__(self, name=""):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel("Page 2")
        self.layout.addWidget(self.label)

        if name:
            self.name_label = QLabel(f"Hello, {name}!")
        else:
            self.name_label = QLabel("Name not entered.")
        self.layout.addWidget(self.name_label)

        self.setLayout(self.layout)


class Page3(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.label = QLabel("Page 3")
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    home_page = HomePage()
    home_page.show()
    sys.exit(app.exec_())
