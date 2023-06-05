import pyttsx3
import random
import numpy as np

from detector.ColorDetector import ColorDetector


class CommandDetector:

    def __init__(self, frame):
        self.frame = frame
        self.audios = {16: [frame.audio[0], frame.audio[1], frame.audio[2], frame.audio[3]],
                       17: [frame.audio[4], frame.audio[5], frame.audio[6], frame.audio[7]],
                       18: [frame.audio[8], frame.audio[9], frame.audio[10], frame.audio[11]],
                       19: [frame.audio[12], frame.audio[13], frame.audio[14], frame.audio[15]], 4: frame.audio[22],
                       5: frame.audio[23],
                       6: [frame.audio[16], frame.audio[17], frame.audio[18], frame.audio[19], frame.audio[20],
                           frame.audio[21]]}
        self.ids = []
        self.corners = []
        self.detector = ColorDetector()
        self.colors = ["red", "blue", "yellow", "green"]
        self.objs = {16: frame.edit1.text(), 17: frame.edit2.text(), 18: frame.edit3.text(), 19: frame.edit4.text()}
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

        self.curr1_zone = self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr1)[0][0])
        self.curr2_zone = self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr2)[0][0])

        count = 0
        while self.curr1_zone == self.curr2_zone:
            count += 1
            self.curr2 = self.curr2 + 1
            if self.curr2 == 20:
                self.curr2 = 16
            self.curr2_zone = self.detector.define_zone(self.ids, self.corners, np.where(self.ids == self.curr2)[0][0])
            if count > 10:
                break

        if ((self.curr1 == 16 and self.curr2 == 17) or (self.curr1 == 17 and self.curr2 == 16)) and self.audios[6][
            0] is not None:
            play_obj = self.audios[6][0].play()
            play_obj.wait_done()
        elif ((self.curr1 == 16 and self.curr2 == 18) or (self.curr1 == 18 and self.curr2 == 16)) and self.audios[6][
            1] is not None:
            play_obj = self.audios[6][1].play()
            play_obj.wait_done()
        elif ((self.curr1 == 16 and self.curr2 == 19) or (self.curr1 == 19 and self.curr2 == 16)) and self.audios[6][
            2] is not None:
            play_obj = self.audios[6][2].play()
            play_obj.wait_done()
        elif ((self.curr1 == 17 and self.curr2 == 18) or (self.curr1 == 18 and self.curr2 == 17)) and self.audios[6][
            3] is not None:
            play_obj = self.audios[6][3].play()
            play_obj.wait_done()
        elif ((self.curr1 == 17 and self.curr2 == 19) or (self.curr1 == 19 and self.curr2 == 17)) and self.audios[6][
            4] is not None:
            play_obj = self.audios[6][4].play()
            play_obj.wait_done()
        elif ((self.curr1 == 18 and self.curr2 == 19) or (self.curr1 == 19 and self.curr2 == 18)) and self.audios[6][
            5] is not None:
            play_obj = self.audios[6][5].play()
            play_obj.wait_done()
        else:
            self.engine.say("Поменяйте " + self.objs[self.curr1] + " и " + self.objs[self.curr2] + " местами")
            self.engine.runAndWait()

        return True

    def repeat_replace(self):
        if ((self.curr1 == 16 and self.curr2 == 17) or (self.curr1 == 17 and self.curr2 == 16)) and self.audios[6][
            0] is not None:
            play_obj = self.audios[6][0].play()
            play_obj.wait_done()
        elif ((self.curr1 == 16 and self.curr2 == 18) or (self.curr1 == 18 and self.curr2 == 16)) and self.audios[6][
            1] is not None:
            play_obj = self.audios[6][1].play()
            play_obj.wait_done()
        elif ((self.curr1 == 16 and self.curr2 == 19) or (self.curr1 == 19 and self.curr2 == 16)) and self.audios[6][
            2] is not None:
            play_obj = self.audios[6][2].play()
            play_obj.wait_done()
        elif ((self.curr1 == 17 and self.curr2 == 18) or (self.curr1 == 18 and self.curr2 == 17)) and self.audios[6][
            3] is not None:
            play_obj = self.audios[6][3].play()
            play_obj.wait_done()
        elif ((self.curr1 == 17 and self.curr2 == 19) or (self.curr1 == 19 and self.curr2 == 17)) and self.audios[6][
            4] is not None:
            play_obj = self.audios[6][4].play()
            play_obj.wait_done()
        elif ((self.curr1 == 18 and self.curr2 == 19) or (self.curr1 == 19 and self.curr2 == 18)) and self.audios[6][
            5] is not None:
            play_obj = self.audios[6][5].play()
            play_obj.wait_done()
        else:
            self.engine.say("Поменяйте " + self.objs[self.curr1] + " и " + self.objs[self.curr2] + " местами")
            self.engine.runAndWait()

    def check_replace(self):
        if self.curr1 in np.ravel(self.ids) and self.curr2 in np.ravel(self.ids) and self.detector.define_zone(self.ids,
                                                                                                               self.corners,
                                                                                                               np.where(
                                                                                                                   self.ids == self.curr1)[
                                                                                                                   0][
                                                                                                                   0]) == self.curr2_zone and self.detector.define_zone(
            self.ids, self.corners, np.where(self.ids == self.curr2)[0][0]) == self.curr1_zone:
            if self.audios[4] is not None:
                play_obj = self.audios[4].play()
                play_obj.wait_done()
            else:
                self.engine.say("Прекрасно")
                self.engine.runAndWait()
            return True
        else:
            if self.audios[5] is not None:
                play_obj = self.audios[5].play()
                play_obj.wait_done()
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
            zone_idx = (zone_idx + 1) % 4

        self.curr_zone = self.colors[zone_idx]
        if self.curr_zone == "red":
            if self.audios[self.curr_obj][0] is not None:
                play_obj = self.audios[self.curr_obj][0].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в красную зону")
                self.engine.runAndWait()
        elif self.curr_zone == "blue":
            if self.audios[self.curr_obj][1] is not None:
                play_obj = self.audios[self.curr_obj][1].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в синюю зону")
                self.engine.runAndWait()
        elif self.curr_zone == "yellow":
            if self.audios[self.curr_obj][2] is not None:
                play_obj = self.audios[self.curr_obj][2].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в желтую зону")
                self.engine.runAndWait()
        else:
            if self.audios[self.curr_obj][3] is not None:
                play_obj = self.audios[self.curr_obj][3].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в зеленую зону")
                self.engine.runAndWait()
        return self.curr_zone

    def repeat_command(self):
        if self.curr_zone == "red":
            if self.audios[self.curr_obj][0] is not None:
                play_obj = self.audios[self.curr_obj][0].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в красную зону")
                self.engine.runAndWait()
        elif self.curr_zone == "blue":
            if self.audios[self.curr_obj][1] is not None:
                play_obj = self.audios[self.curr_obj][1].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в синюю зону")
                self.engine.runAndWait()
        elif self.curr_zone == "yellow":
            if self.audios[self.curr_obj][2] is not None:
                play_obj = self.audios[self.curr_obj][2].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в желтую зону")
                self.engine.runAndWait()
        else:
            if self.audios[self.curr_obj][3] is not None:
                play_obj = self.audios[self.curr_obj][3].play()
                play_obj.wait_done()
            else:
                self.engine.say("Положите " + self.objs[self.curr_obj] + " в зеленую зону")
                self.engine.runAndWait()

    def check_command(self):
        if self.curr_obj in np.ravel(self.ids) and \
                self.curr_zone == self.detector.define_zone(self.ids, self.corners,
                                                            np.where(self.ids == self.curr_obj)[0][0]):
            if self.audios[4] is not None:
                play_obj = self.audios[4].play()
                play_obj.wait_done()
            else:
                self.engine.say("Прекрасно")
                self.engine.runAndWait()
            return True
        else:
            if self.audios[5] is not None:
                play_obj = self.audios[5].play()
                play_obj.wait_done()
            else:
                self.engine.say("Не получилось, попробуйте еще раз")
                self.engine.runAndWait()
            return False
