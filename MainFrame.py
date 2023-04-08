import sys
import cv2
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QApplication

from ImageProcessor import ImageProcessor
from ImageReader import ImageReader


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt static label demo")
        self.width = 640
        self.height = 480
        # create the label that holds the image
        self.image_label = QLabel(self)
        # create a text label
        self.textLabel = QLabel('Demo')

        # create a vertical box layout and add the two labels
        vbox = QVBoxLayout()
        vbox.addWidget(self.image_label)
        vbox.addWidget(self.textLabel)
        # set the vbox layout as the widgets layout
        self.setLayout(vbox)
        # create a grey pixmap
        grey = QPixmap(self.width, self.height)
        grey.fill(QColor('darkGray'))
        # set the image image to the grey pixmap
        self.image_label.setPixmap(grey)

        self.processor = ImageProcessor()
        self.reader = ImageReader(self.process_img, 1)
        self.reader.start()

    def process_img(self, img):
        rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.processor.process(rgb_image)
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
