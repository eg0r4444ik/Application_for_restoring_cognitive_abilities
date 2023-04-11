import time

import cv2

from threading import Thread


class ImageReader(Thread):
    def __init__(self, cb, source_idx):
        Thread.__init__(self)
        self.cb = cb
        self.video = cv2.VideoCapture(source_idx)
        self.video.set(cv2.CAP_PROP_BUFFERSIZE, 2)
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
            if time.time() - t > 10:
                self.cb(img)
                print("Совершите действие")
                t = time.time()
        self.video.release()
        cv2.destroyAllWindows()
