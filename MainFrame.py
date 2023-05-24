import sys
import wave
import simpleaudio as sa

import cv2
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QRect

from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication, QLineEdit, QPushButton, QFileDialog

# from ImageProcessor import ImageProcessor
from ImageReader import ImageReader


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")
        self.width = 640
        self.height = 700
        self.audio = []
        self.setFixedSize(self.width, self.height)
        # create the label that holds the image
        self.image_label = QLabel(self)
        # create a text label

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        font1 = QtGui.QFont("Roboto", 10)
        font2 = QtGui.QFont("Roboto", 16)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit1.setFixedWidth(250)
        self.edit2.setFixedWidth(250)
        self.edit3.setFixedWidth(250)
        self.edit4.setFixedWidth(250)
        self.start_btn = QPushButton('Старт', self)
        self.start_btn.setFont(font2)
        self.start_btn.clicked.connect(self.startClicked)
        self.load_button1 = QPushButton('Загрузить аудио-файлы', self)
        self.load_button1.setGeometry(290, 530, 325, 100)
        self.load_button1.setFont(font2)
        self.load_button1.clicked.connect(self.load_file1)
        label1 = QLabel('Название первого предмета:')
        label2 = QLabel('Название второго предмета:')
        label3 = QLabel('Название третьего предмета:')
        label4 = QLabel('Название четвертого предмета:')
        label1.setFont(font1)
        label2.setFont(font1)
        label3.setFont(font1)
        label4.setFont(font1)
        self.edit1.setFont(font1)
        self.edit2.setFont(font1)
        self.edit3.setFont(font1)
        self.edit4.setFont(font1)
        vbox.addWidget(self.start_btn)
        vbox.addWidget(self.image_label)
        vbox.addWidget(label1)
        vbox.addWidget(self.edit1)
        vbox.addWidget(label2)
        vbox.addWidget(self.edit2)
        vbox.addWidget(label3)
        vbox.addWidget(self.edit3)
        vbox.addWidget(label4)
        vbox.addWidget(self.edit4)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)
        # create a grey pixmap
        grey = QPixmap(self.width, self.height)
        grey.fill(QColor('darkGray'))
        # set the image image to the grey pixmap
        self.image_label.setPixmap(grey)
        self.reader = None

        # self.processor = ImageProcessor()
        # self.reader = ImageReader(self, self.process_img, 0)

    def load_file1(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', '(*.wav)')
        wave_obj = None

        if self.filename:
            wave_obj = sa.WaveObject.from_wave_file(self.filename)

        self.audio.append(wave_obj)

    def startClicked(self):
        self.reader = ImageReader(self, self.process_img, 1)
        self.reader.start()

    def process_img(self, img):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # self.processor.process(rgb_image)
        pix_map = self.convert_cv_qt(rgb_image)
        self.image_label.setPixmap(pix_map)

    def convert_cv_qt(self, cv_img):
        pass
        h, w, ch = cv_img.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(cv_img.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.width, self.height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.reader.stop()
        super().closeEvent(a0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = App()
    a.show()
    sys.exit(app.exec_())
