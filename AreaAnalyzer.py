import cv2
import pyttsx3


class AreaAnalyzer:

    def __init__(self):
        self.red_s = 0
        self.blue_s = 0
        self.engine = pyttsx3.init()

    def analyze(self, new_r, new_b):
        b = True
        if new_r - self.red_s > 1500 and new_r >= self.red_s:
            self.engine.say("Убрали предмет из красной зоны")
            b = False
        if self.red_s - new_r > 1500 and self.red_s >= new_r:
            self.engine.say("Положили предмет в красную зону")
            b = False
        if new_b - self.blue_s > 1500 and new_b >= self.blue_s:
            self.engine.say("Убрали предмет из синей зоны")
            b = False
        if self.blue_s - new_b > 1500 and self.blue_s >= new_b:
            self.engine.say("Положили предмет в синюю зону")
            b = False
        self.red_s = new_r
        self.blue_s = new_b
        if b:
            self.engine.say("Ничего не изменилось")
        self.engine.runAndWait()

    def detS(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return cv2.countNonZero(gray)
