import time

import cv2
from cv2 import aruco
import numpy as np
from threading import Thread

from CommandDetector import CommandDetector
from ColorDetector import ColorDetector


class ImageReader(Thread):
    def __init__(self, cb, source_idx):
        Thread.__init__(self)
        self.cb = cb
        self.video = cv2.VideoCapture(source_idx)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        self.detector = ColorDetector()
        self.com_det = CommandDetector()
        self.com_det.generate_command()
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
            dict_aruco = aruco.Dictionary_get(aruco.DICT_4X4_50)
            parameters = aruco.DetectorParameters_create()

            corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, dict_aruco, parameters=parameters)

            result = aruco.drawDetectedMarkers(img.copy(), corners, ids)

            markers_id = [16]

            self.cb(result)
            if time.time() - t > 5:
                bol = False
                for marker_id in markers_id:
                    if marker_id in np.ravel(ids):
                        index = np.where(ids == marker_id)[0][0]
                        bol = self.com_det.check_command(self.detector.define_zone(ids, corners, index))
                if bol:
                    self.com_det.generate_command()
                t = time.time()

        self.video.release()
        cv2.destroyAllWindows()
