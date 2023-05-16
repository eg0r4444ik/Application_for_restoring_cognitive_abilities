import cv2
import pyttsx3
import random
import numpy as np

from ColorDetector import ColorDetector


class CommandDetector:

    def __init__(self):
        self.ids = []
        self.corners = []
        self.detector = ColorDetector()
        self.colors = ["red", "blue", "yellow", "green"]
        self.objs = {16: "коробку", 17: "маркер", 18: "ложку", 19: "книгу"}
        self.curr_zone = "red"
        self.curr_obj = 16
        self.curr1 = 16
        self.curr2 = 17
        self.curr1_zone = "red"
        self.curr2_zone = "blue"
        self.engine = pyttsx3.init()

    def update(self, ids, corners):
        self.ids = ids
        self.corners = corners

    def replace(self):
        objects = list()
        for marker_id in self.objs.keys():
            if marker_id in np.ravel(self.ids):
                objects.append(marker_id)
        self.curr1 = objects[random.randint(0, len(objects) - 1)]
        self.curr2 = objects[random.randint(0, len(objects) - 1)]

        count = 0
        while self.curr1 == self.curr2:
            count += 1
            self.curr2 = (self.curr2+1) % 4
            if count > 10:
                break

        self.curr1_zone = self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr1)[0][0])
        self.curr2_zone = self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr2)[0][0])

        self.engine.say("Поменяйте " + self.objs[self.curr1] + " и " + self.objs[self.curr2] + " местами")
        self.engine.runAndWait()
        return True

    def repeat_replace(self):
        self.engine.say("Поменяйте " + self.objs[self.curr1] + " и " + self.objs[self.curr2] + " местами")
        self.engine.runAndWait()

    def check_replace(self):
        if self.curr1 in np.ravel(self.ids) and self.curr2 in np.ravel(self.ids) and self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr1)[0][0]) == self.curr2_zone and self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr2)[0][0]) == self.curr1_zone:
            self.engine.say("Прекрасно")
            self.engine.runAndWait()
            return True
        else:
            self.engine.say("Не получилось, попробуйте еще раз")
            self.engine.runAndWait()
            return False

    def generate_command(self):
        objects = list()
        for marker_id in self.objs.keys():
            if marker_id in np.ravel(self.ids):
                objects.append(marker_id)

        self.curr_obj = objects[random.randint(0, len(objects) - 1)]
        zone = self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr_obj)[0][0])

        zone_idx = random.randint(0, 3)
        if zone == self.colors[zone_idx]:
            zone_idx = (zone_idx+1) % 4

        self.curr_zone = self.colors[zone_idx]
        if self.curr_zone == "red":
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в красную зону")
        elif self.curr_zone == "blue":
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в синюю зону")
        elif self.curr_zone == "yellow":
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в желтую зону")
        else:
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в зеленую зону")
        self.engine.runAndWait()
        return self.curr_zone

    def repeat_command(self):
        if self.curr_zone == "red":
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в красную зону")
        elif self.curr_zone == "blue":
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в синюю зону")
        elif self.curr_zone == "yellow":
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в желтую зону")
        else:
            self.engine.say("Положите " + self.objs[self.curr_obj] + " в зеленую зону")
        self.engine.runAndWait()

    def check_command(self):
        if self.curr_obj in np.ravel(self.ids) and \
                self.curr_zone == self.detector.define_zone(self.ids, self.corners,
                                                            np.where(self.ids == self.curr_obj)[0][0]):
            self.engine.say("Прекрасно")
            self.engine.runAndWait()
            return True
        else:
            self.engine.say("Не получилось, попробуйте еще раз")
            self.engine.runAndWait()
            return False
