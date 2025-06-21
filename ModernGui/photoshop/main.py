#Import module
import os
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance

#App setting
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("PhotoQt")
main_window.resize(1600,800)

#App widgets/objects
btn_folder = QPushButton("Folder")
file_list  = QListWidget()

left       = QPushButton("Left")
right      = QPushButton("Right")
mirror     = QPushButton("Mirror")
sharpness  = QPushButton("Sharpen")
gray       = QPushButton("B/W")
saturation = QPushButton("Color")
contrast   = QPushButton("Contrast")
blur       = QPushButton("Blur")

filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpen")
filter_box.addItem("B/W")
filter_box.addItem("Color")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

image_box = QLabel("Image display!")

#App design
master_layout = QHBoxLayout()

col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(left)
col1.addWidget(right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturation)
col1.addWidget(contrast)
col1.addWidget(blur)

col2.addWidget(image_box)

master_layout.addLayout(col1, 15)
master_layout.addLayout(col2, 85)

main_window.setLayout(master_layout)

#Filter file and extensions
working_dir = ""
def filter(files, extensions):
    results = []
    for file in files:
        for ext in extensions:
            if file.endswith(ext):
                results.append(file)
    return results

#Choose directory
def getWorkDir():
    global working_dir
    working_dir = QFileDialog.getExistingDirectory(None, "Select Directory", "D:/HienDuc/Hinh anh/Other")
    extensions = ['.png', '.jpg', '.jpeg']
    if len(working_dir) > 0:
        filenames = filter(os.listdir(working_dir), extensions)
        file_list.clear()
        for filename in filenames:
            file_list.addItem(filename)
    
class Editor():
    def __init__(self):
        self.image = None
        self.original = None
        self.filename = None
        self.save_folder = "edits/"

    def load_image(self, filename):
        self.filename = filename
        fullname = os.path.join(working_dir, filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(working_dir, self.save_folder)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

    def show_image(self, path):
        image_box.hide()
        image = QPixmap(path)
        w, h = image_box.width(), image_box.height()
        image = image.scaled(w, h, Qt.KeepAspectRatio)
        image_box.setPixmap(image)
        image_box.show()

    def gray(self):
        if self.image is None:
            return
        self.image = self.image.convert("L")
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def left(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def right(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def mirror(self):
        if self.image is None:
            return
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def sharpen(self):
        if self.image is None:
            return
        enhancer = ImageEnhance.Sharpness(self.image)
        self.image = enhancer.enhance(2.0)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def color(self):
        if self.image is None:
            return
        enhancer = ImageEnhance.Color(self.image)
        self.image = enhancer.enhance(2.0)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def contrast(self):
        if self.image is None:
            return
        enhancer = ImageEnhance.Contrast(self.image)
        self.image = enhancer.enhance(2.0)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def blur(self):
        if self.image is None:
            return
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

    def apply_filer(self, filter_name):
        if self.image is None:
            return

        if filter_name == "Original":
            self.image = self.original.copy()
        else:
            mapping = {
                "Left": lambda image : image.transpose(Image.ROTATE_90),
                "Right": lambda image : image.transpose(Image.ROTATE_270),
                "Mirror": lambda image : image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpen": lambda image : ImageEnhance.Sharpness(image).enhance(2.0),
                "B/W": lambda image : image.convert("L"),
                "Color": lambda image : ImageEnhance.Color(image).enhance(2.0),
                "Contrast": lambda image : ImageEnhance.Contrast(image).enhance(2.0),
                "Blur": lambda image : image.filter(ImageFilter.BLUR)
            }

            filter_func = mapping.get(filter_name)
            if filter_func:
                self.image = filter_func(self.original.copy())
            
        self.save_image()
        image_path = os.path.join(working_dir, self.save_folder, self.filename)
        self.show_image(image_path)

def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main_edit.load_image(filename)
        main_edit.show_image(os.path.join(working_dir, filename))

#Run
main_edit = Editor()
btn_folder.clicked.connect(getWorkDir)
file_list.currentRowChanged.connect(displayImage)

filter_box.currentTextChanged.connect(main_edit.apply_filer)

gray.clicked.connect(main_edit.gray)
left.clicked.connect(main_edit.left)
right.clicked.connect(main_edit.right)
mirror.clicked.connect(main_edit.mirror)
sharpness.clicked.connect(main_edit.sharpen)
saturation.clicked.connect(main_edit.color)
contrast.clicked.connect(main_edit.contrast)
blur.clicked.connect(main_edit.blur)

main_window.show()
app.exec()