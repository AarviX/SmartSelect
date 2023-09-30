from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QInputDialog, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
import os
import shutil

class DesignAlbumPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        create_album_button = QPushButton('Create Album', self)
        create_album_button.clicked.connect(self.design_album)
        layout.addWidget(create_album_button)

        back_button = QPushButton('Back to Landing Page', self)
        back_button.clicked.connect(self.parent.show_design_album_page)

        layout.addWidget(back_button)
        layout.addWidget(back_button, alignment=Qt.AlignTop | Qt.AlignLeft)
        # Add other widgets and layout for the Design Album page as needed

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
