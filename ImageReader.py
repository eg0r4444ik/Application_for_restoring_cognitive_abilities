import time
import random

import cv2
from cv2 import aruco
import numpy as np
from threading import Thread

from CommandDetector import CommandDetector
from ColorDetector import ColorDetector


class ImageReader(Thread):
    def __init__(self, frame, cb, source_idx):
        Thread.__init__(self)
        self.cb = cb
        self.video = cv2.VideoCapture(source_idx)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
        self.com_det = CommandDetector(frame)
        self.curr_command = -1
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

            self.com_det.update(ids, corners)

            self.cb(result)
            if time.time() - t > 6:
                if self.curr_command == 0:
                    bol = self.com_det.check_command()
                    if bol:
                        self.curr_command = random.randint(0, 1)
                        if self.curr_command == 0:
                            self.com_det.generate_command()
                        else:
                            self.com_det.replace()
                    else:
                        self.com_det.repeat_command()
                elif self.curr_command == 1:
                    bol = self.com_det.check_replace()
                    if bol:
                        self.curr_command = random.randint(0, 1)
                        if self.curr_command == 0:
                            self.com_det.generate_command()
                        else:
                            self.com_det.replace()
                    else:
                        self.com_det.repeat_replace()
                else:
                    self.curr_command = random.randint(0, 1)
                    if self.curr_command == 0:
                        self.com_det.generate_command()
                    else:
                        self.com_det.replace()

                t = time.time()

        self.video.release()
        cv2.destroyAllWindows()
