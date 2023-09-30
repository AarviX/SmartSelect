import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QStackedWidget, QLabel
from settings import SettingsPage
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from landing import LandingPage
from designalbum import DesignAlbumPage
from help import HelpPage

class SmartSelect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.setWindowTitle('Smart Select')
        self.setGeometry(100, 100, 800, 600)
        self.central_widget = QStackedWidget(self)
        self.setCentralWidget(self.central_widget)

        self.landing_page = LandingPage(self)
        self.help_page = HelpPage(self)
        self.settings_page = SettingsPage(self)

        # Create an instance of DesignAlbumPage and store it as a member variable
        self.design_album_page = DesignAlbumPage(self)

        logo_label = QLabel(self)
        logo_pixmap = QPixmap('/Users/srialla/SmartSelect/venv/Media/Entry.png')
        if logo_pixmap.isNull():
            print("Error loading image")
        else:
            max_logo_size = QSize(800, 600)
            logo_pixmap = logo_pixmap.scaled(max_logo_size, Qt.KeepAspectRatio)
            logo_label.setPixmap(logo_pixmap)
            logo_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(logo_label)

        self.central_widget.addWidget(self.landing_page)
        self.central_widget.addWidget(self.help_page)
        self.central_widget.addWidget(self.settings_page)
        self.central_widget.addWidget(self.design_album_page)  # Add the DesignAlbumPage

        self.central_widget.setCurrentWidget(self.landing_page)

        design_album_button = QPushButton('Design Album', self)
        help_button = QPushButton('Help', self)
        settings_button = QPushButton('Settings', self)

        design_album_button.clicked.connect(self.show_design_album_page)
        help_button.clicked.connect(self.show_help_page)
        settings_button.clicked.connect(self.show_settings_page)

        layout.addWidget(design_album_button)
        layout.addWidget(help_button)
        layout.addWidget(settings_button)

        central_widget_container = QWidget()
        central_widget_container.setLayout(layout)
        self.setCentralWidget(central_widget_container)

    def show_design_album_page(self):
        # Set the current widget to the stored instance of DesignAlbumPage
        self.central_widget.setCurrentWidget(self.design_album_page)

    def show_help_page(self):
        self.central_widget.setCurrentWidget(self.help_page)

    def show_settings_page(self):
        self.central_widget.setCurrentWidget(self.settings_page)


def main():
    app = QApplication(sys.argv)
    smart_select = SmartSelect()
    smart_select.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
