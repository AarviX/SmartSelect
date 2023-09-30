from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize, Qt


class LandingPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        # header_label = QLabel('Smart Select', self)
        # header_label.setAlignment(QtCore.Qt.AlignCenter)
        # # header_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        # # layout.addWidget(header_label)

        # logo_label = QLabel(self)
        # logo_pixmap = QPixmap('venv/Media/Entry.png')
        # if logo_pixmap.isNull():
        #     print("Error loading image")
        # else:
        #     max_logo_size = QSize(800, 600)
        #     logo_pixmap = logo_pixmap.scaled(max_logo_size, Qt.KeepAspectRatio)
        #     logo_label.setPixmap(logo_pixmap)
        #     logo_label.setAlignment(Qt.AlignCenter)
        #     layout.addWidget(logo_label)

        design_album_button = QPushButton('Design Album', self)
        # design_album_button.clicked.connect(self.parent.show_design_album_page)
        layout.addWidget(design_album_button)
        # Add other widgets and layout for the Landing page as needed
