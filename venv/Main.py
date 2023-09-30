import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QGridLayout, QScrollArea, QInputDialog, QMessageBox
from PyQt5.QtGui import QPixmap, QImage
from PIL import Image, ImageQt
from PyQt5 import QtCore
from PyQt5.QtCore import QSize
import io
class SmartSelect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()
        self.photos = []  # List to store photo data
        self.photo_grid_layout = QGridLayout()
    def initui(self):
        self.setWindowTitle('Smart Select Photo Album App')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        header_label = QLabel('Smart Select', self)
        header_label.setAlignment(QtCore.Qt.AlignCenter)
        header_label.setStyleSheet('font-size: 24px; font-weight: bold;')
        layout.addWidget(header_label)

        logo_label = QLabel(self)
        logo_pixmap = QPixmap('/Users/srialla/SmartSelect/venv/Media/Entry.png')
        if logo_pixmap.isNull():
            print("Error loading image")
        else:
            max_logo_size = QSize(800,600)
            logo_pixmap = logo_pixmap.scaled(max_logo_size, QtCore.Qt.KeepAspectRatio)
            logo_label.setPixmap(logo_pixmap)
            logo_label.setAlignment(QtCore.Qt.AlignCenter)
            layout.addWidget(logo_label)

        # self.photo_scroll_area = QScrollArea(self)
        # layout.addWidget(self.photo_scroll_area)
        #
        # self.photo_scroll_content = QWidget(self)
        # self.photo_scroll_area.setWidget(self.photo_scroll_content)
        #
        # self.photo_grid_layout = QGridLayout(self.photo_scroll_content)
        # self.photo_grid_layout.setAlignment(QtCore.Qt.AlignTop)

        design_album_button = QPushButton('Design Album', self)
        help_button = QPushButton('Help', self)
        settings_button = QPushButton('Settings', self)

        design_album_button.clicked.connect(self.design_album)
        help_button.clicked.connect(self.help)
        settings_button.clicked.connect(self.settings)

        layout.addWidget(design_album_button)
        layout.addWidget(help_button)
        layout.addWidget(settings_button)

    def design_album(self):
        while True:
            album_name, ok = QInputDialog.getText(self, 'Create Album', 'Enter album name:')

            if not ok:
                return  # User canceled

            if album_name:
                album_dir = f'./{album_name}'  # You can change the directory path as needed

                # Check if the directory already exists
                if os.path.exists(album_dir):
                    QMessageBox.warning(self, 'Album Name Exists', f'Album name "{album_name}" already exists. Please provide a unique name.')
                else:
                    try:
                        os.makedirs(album_dir)
                        QMessageBox.information(self, 'Success', f'Album "{album_name}" created successfully!')
                        break  # Exit the loop when a unique name is provided and directory is created
                    except OSError as e:
                        QMessageBox.critical(self, 'Error', f'Failed to create album directory: {str(e)}')

        # Proceed to upload photos to the album directory
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_paths, _ = QFileDialog.getOpenFileNames(self, f'Upload Photos to {album_name}', '', 'Images (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*)', options=options)

        if file_paths:
            for file_path in file_paths:
                try:
                    shutil.copy(file_path, album_dir)
                except Exception as e:
                    print(f"Error copying file: {str(e)}")
        else:
            QMessageBox.information(self, 'Info', 'No photos selected for upload.')

    def displayPhoto(self, photo_data):
        try:
            pixmap = QPixmap()
            image = ImageQt.ImageQt(Image.open(io.BytesIO(photo_data)))
            pixmap.convertFromImage(image)

            # Create a QLabel to display the photo
            label = QLabel(self)
            label.setPixmap(pixmap)

            # Create a small tile for the photo
            tile = QWidget(self)
            tile_layout = QVBoxLayout(tile)
            tile_layout.addWidget(label)

            # Add the tile to the grid layout
            row, col = divmod(len(self.photos), 3)
            self.photo_grid_layout.addWidget(tile, row, col)

        except Exception as e:
            print(f"Error displaying photo: {e}")

    def help(self):
        # Replace this with the code to open the Help page
        pass

    def settings(self):
        # Replace this with the code to open the Settings page
        pass

    def uploadPhotos(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_paths, _ = QFileDialog.getOpenFileNames(self, 'Upload Photos', '', 'Images (*.png *.jpg *.jpeg *.gif *.bmp);;All Files (*)', options=options)

        if file_paths:
            for file_path in file_paths:
                with open(file_path, 'rb') as file:
                    photo_data = file.read()

                if self.isValidImage(photo_data):
                    compressed_photo_data = self.compressImage(photo_data)
                    if compressed_photo_data:
                        self.photos.append(compressed_photo_data)
                        self.displayPhoto(compressed_photo_data)
                else:
                    print(f"Error: Invalid image file: {file_path}")

    def isValidImage(self, data):
        try:
            Image.open(io.BytesIO(data))
            # Check if the image format is recognized (valid image)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    def compressImage(self, photo_data, quality=75):
        try:
            image = Image.open(io.BytesIO(photo_data))
            image = image.convert("RGB")  # Ensure the image is in RGB mode
            image = image.resize((300, 200), Image.ANTIALIAS)  # Resize for display (adjust dimensions as needed)
            output = io.BytesIO()
            image.save(output, format="JPEG", quality=quality)
            return output.getvalue()
        except Exception as e:
            print(f"Failed to compress the image: {e}")
            return None

def main():
    app = QApplication(sys.argv)
    smart_select = SmartSelect()
    smart_select.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
