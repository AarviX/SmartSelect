import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QListWidget, QListWidgetItem, QGridLayout, QScrollArea
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PIL import Image, ImageQt
import io

class SmartSelect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initui()
        self.photos = []  # List to store photo data

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

        self.photo_scroll_area = QScrollArea(self)
        layout.addWidget(self.photo_scroll_area)

        self.photo_scroll_content = QWidget(self)
        self.photo_scroll_area.setWidget(self.photo_scroll_content)

        self.photo_grid_layout = QGridLayout(self.photo_scroll_content)
        self.photo_grid_layout.setAlignment(QtCore.Qt.AlignTop)

        upload_button = QPushButton('Upload Photos', self)
        create_album_button = QPushButton('Create Album', self)

        upload_button.clicked.connect(self.uploadPhotos)
        create_album_button.clicked.connect(self.createAlbum)

        layout.addWidget(upload_button)
        layout.addWidget(create_album_button)

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
            image = Image.open(io.BytesIO(data))

            # Check if the image format is recognized (valid image)
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False


    def compressImage(self, photo_data, quality=75):
        # Create a PIL Image from the photo data
        image = Image.open(io.BytesIO(photo_data))

        # Compress the image using the specified quality (0-100)
        try:
            image = image.convert("RGB")  # Ensure the image is in RGB mode
            image = image.resize((300, 200), Image.ANTIALIAS)  # Resize for display (adjust dimensions as needed)
            output = io.BytesIO()
            image.save(output, format="JPEG", quality=quality)


            return output.getvalue()

        except Exception as e:
            print(f"failed to compress the image:{e}")
            return None

    def displayPhoto(self, photo_data):
        pixmap = QPixmap()
        image = ImageQt(Image.open(io.BytesIO(photo_data)))
        pixmap.convertFromImage(image)
        label = QLabel(self)
        label.setPixmap(pixmap)

        row, col = divmod(len(self.photos) - 1, 3)
        self.photo_grid_layout.addWidget(label, row, col)

    def createAlbum(self):
        album_window = AlbumWindow(self)
        album_window.show()

class AlbumWindow(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parents
        self.albums = {}
        self.initui()

    def initui(self):
        self.setWindowTitle('Album Management')
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout(self)

        self.album_list = QListWidget(self)
        layout.addWidget(self.album_list)

        add_photos_button = QPushButton('Add Photos to Album', self)
        create_album_button = QPushButton('Create Album', self)

        add_photos_button.clicked.connect(self.addPhotosToAlbum)
        create_album_button.clicked.connect(self.createAlbum)

        layout.addWidget(add_photos_button)
        layout.addWidget(create_album_button)

    def createAlbum(self):
        album_name, ok = QInputDialog.getText(self, 'Create Album', 'Enter album name:')
        if ok and album_name:
            self.albums[album_name] = []
            self.album_list.addItem(album_name)

    def addPhotosToAlbum(self):
        pass

def main():
    app = QApplication(sys.argv)
    smart_select = SmartSelect()
    smart_select.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
