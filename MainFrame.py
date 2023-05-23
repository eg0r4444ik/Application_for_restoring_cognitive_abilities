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
        self.audio1 = None
        self.audio2 = None
        self.audio3 = None
        self.audio4 = None
        self.audio5 = None
        self.audio6 = None
        self.setFixedSize(self.width, self.height)
        # create the label that holds the image
        self.image_label = QLabel(self)
        # create a text label

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        font = QtGui.QFont("Roboto", 10)
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.edit4 = QLineEdit()
        self.edit1.setFixedWidth(250)
        self.edit2.setFixedWidth(250)
        self.edit3.setFixedWidth(250)
        self.edit4.setFixedWidth(250)
        self.start_btn = QPushButton('Старт', self)
        self.start_btn.setFont(font)
        self.start_btn.clicked.connect(self.startClicked)
        self.load_button1 = QPushButton('Загрузить аудио-файл', self)
        self.load_button2 = QPushButton('Загрузить аудио-файл', self)
        self.load_button3 = QPushButton('Загрузить аудио-файл', self)
        self.load_button4 = QPushButton('Загрузить аудио-файл', self)
        self.load_button5 = QPushButton('Загрузить файл с похвалой', self)
        self.load_button6 = QPushButton('Загрузить файл "не получилось"', self)
        self.load_button1.setGeometry(325, 470, 200, 40)
        self.load_button2.setGeometry(325, 530, 200, 40)
        self.load_button3.setGeometry(325, 590, 200, 40)
        self.load_button4.setGeometry(325, 650, 200, 40)
        self.load_button5.setGeometry(530, 530, 200, 40)
        self.load_button6.setGeometry(530, 590, 200, 40)
        self.load_button1.clicked.connect(self.load_file1)
        self.load_button2.clicked.connect(self.load_file2)
        self.load_button3.clicked.connect(self.load_file3)
        self.load_button4.clicked.connect(self.load_file4)
        self.load_button5.clicked.connect(self.load_file5)
        self.load_button6.clicked.connect(self.load_file6)
        label1 = QLabel('Название первого предмета:')
        label2 = QLabel('Название второго предмета:')
        label3 = QLabel('Название третьего предмета:')
        label4 = QLabel('Название четвертого предмета:')
        label1.setFont(font)
        label2.setFont(font)
        label3.setFont(font)
        label4.setFont(font)
        self.edit1.setFont(font)
        self.edit2.setFont(font)
        self.edit3.setFont(font)
        self.edit4.setFont(font)
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

        self.audio1 = wave_obj

    def load_file2(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', '(*.wav)')
        wave_obj = None

        if self.filename:
            wave_obj = sa.WaveObject.from_wave_file(self.filename)

        self.audio2 = wave_obj

    def load_file3(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', '(*.wav)')
        wave_obj = None

        if self.filename:
            wave_obj = sa.WaveObject.from_wave_file(self.filename)

        self.audio3 = wave_obj

    def load_file4(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', '(*.wav)')
        wave_obj = None

        if self.filename:
            wave_obj = sa.WaveObject.from_wave_file(self.filename)

        self.audio4 = wave_obj

    def load_file5(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', '(*.wav)')
        wave_obj = None

        if self.filename:
            wave_obj = sa.WaveObject.from_wave_file(self.filename)

        self.audio5 = wave_obj

    def load_file6(self):
        self.filename, _ = QFileDialog.getOpenFileName(self, 'Выберите файл', '', '(*.wav)')
        wave_obj = None

        if self.filename:
            wave_obj = sa.WaveObject.from_wave_file(self.filename)

        self.audio6 = wave_obj

    def startClicked(self):
        self.reader = ImageReader(self, self.process_img, 0)
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
