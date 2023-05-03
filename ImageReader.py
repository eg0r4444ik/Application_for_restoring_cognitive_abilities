import time

import cv2
from cv2 import aruco
import numpy as np
from threading import Thread
from pyzbar.pyzbar import decode

from AreaAnalyzer import AreaAnalyzer


class ImageReader(Thread):
    def __init__(self, cb, source_idx):
        Thread.__init__(self)
        self.cb = cb
        self.video = cv2.VideoCapture(source_idx)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        self.analyzer = AreaAnalyzer()
        self.running = False

    def start(self):
        self.running = True
        super().start()

    def stop(self):
        self.running = False

    def run(self):
        t = time.time()
        while self.running:
            _, img = self.video.read()
            hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

            m = cv2.inRange(hsv_img, (0, 0, 0), (255, 255, 255))

            lower_blue = (100, 150, 150)
            upper_blue = (140, 255, 255)
            mask3 = cv2.inRange(hsv_img, lower_blue, upper_blue)

            lower_red = np.array([0, 150, 100])
            upper_red = np.array([10, 255, 255])
            mask1 = cv2.inRange(hsv_img, lower_red, upper_red)

            lower_red = np.array([170, 150, 100])
            upper_red = np.array([180, 255, 255])
            mask2 = cv2.inRange(hsv_img, lower_red, upper_red)

            # Объединение масок
            mask = mask1 + mask2 + mask3

            # применение маски к изображению
            result = cv2.bitwise_and(img, img, mask=None)

            blue = cv2.bitwise_and(img, img, mask=mask3)
            red = cv2.bitwise_and(img, img, mask=(mask1+mask2))

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
            parameters = aruco.DetectorParameters_create()

            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)

            result = aruco.drawDetectedMarkers(img.copy(), corners, ids)

            qr_codes = decode(gray)
            for qr in qr_codes:
                (x, y, w, h) = qr.rect
                cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)
                print(qr.data.decode("utf-8"))



            self.cb(result)
            if time.time() - t > 10:
                self.analyzer.analyze(self.analyzer.detS(red), self.analyzer.detS(blue))
                t = time.time()

        self.video.release()
        cv2.destroyAllWindows()
