import cv2
import pyttsx3
import random


class CommandDetector:

    def __init__(self):
        self.colors = ["red", "blue", "yellow", "green"]
        self.curr = "red"
        self.engine = pyttsx3.init()

    def generate_command(self):
        idx = random.randint(0, 3)
        if self.curr == self.colors[idx]:
            idx = (idx+1) % 4
        self.curr = self.colors[idx]
        if self.curr == "red":
            self.engine.say("Положите предмет в красную зону")
        elif self.curr == "blue":
            self.engine.say("Положите предмет в синюю зону")
        elif self.curr == "yellow":
            self.engine.say("Положите предмет в желтую зону")
        else:
            self.engine.say("Положите предмет в зеленую зону")
        self.engine.runAndWait()
        return self.colors[idx]

    def repeat_command(self):
        if self.curr == "red":
            self.engine.say("Положите предмет в красную зону")
        elif self.curr == "blue":
            self.engine.say("Положите предмет в синюю зону")
        elif self.curr == "yellow":
            self.engine.say("Положите предмет в желтую зону")
        else:
            self.engine.say("Положите предмет в зеленую зону")
        self.engine.runAndWait()

    def check_command(self, res):
        if self.curr == res:
            self.engine.say("Прекрасно")
            self.engine.runAndWait()
            return True
        else:
            self.engine.say("Не получилось, попробуйте еще раз")
            self.engine.runAndWait()
            return False
