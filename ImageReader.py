import time

import cv2
from cv2 import aruco
import numpy as np
from threading import Thread

from ColorDetector import ColorDetector


class ImageReader(Thread):
    def __init__(self, cb, source_idx):
        Thread.__init__(self)
        self.cb = cb
        self.video = cv2.VideoCapture(source_idx)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        self.detector = ColorDetector()
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

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            dict_aruco = aruco.Dictionary_get(aruco.DICT_5X5_50)
            parameters = aruco.DetectorParameters_create()

            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)

            result = aruco.drawDetectedMarkers(img.copy(), corners, ids)

            markers_id = [16]

            for marker_id in markers_id:
                if marker_id in np.ravel(ids):
                    index = np.where(ids == marker_id)[0][0]
                    print(self.detector.define_zone(ids, corners, index))

            self.cb(result)

        self.video.release()
        cv2.destroyAllWindows()
