from ArucoCoordsDetector import ArucoCoordsDetector
import numpy as np


class ColorDetector:
    def __init__(self):
        self.detector = ArucoCoordsDetector()
        self.ids = []
        self.corners = []
    def is_in_zone(self, x, y, x1, y1, x2, y2):
        if (x >= x1) and (x <= x2) and (y >= y1) and (y <= y2):
            return True
        return False

    def center_coords(self, aruco_id, corners):
        return self.detector.center_coords(aruco_id, corners)

    def in_red_zone(self, x, y):
        left_corner = self.define_params(0)
        right_corner = self.define_params(3)
        if left_corner is None or right_corner is None:
            if self.define_params(1) is not None and self.define_params(2) is not None:
                left_corner = self.define_params(1)
                right_corner = self.define_params(2)
                return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                                       max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))
            return False
        return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                               max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))

    def in_blue_zone(self, x, y):
        left_corner = self.define_params(4)
        right_corner = self.define_params(7)
        if left_corner is None or right_corner is None:
            if self.define_params(5) is not None and self.define_params(6) is not None:
                left_corner = self.define_params(5)
                right_corner = self.define_params(6)
                return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                                       max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))
            return False
        return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                               max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))

    def in_yellow_zone(self, x, y):
        left_corner = self.define_params(8)
        right_corner = self.define_params(11)
        if left_corner is None or right_corner is None:
            if self.define_params(9) is not None and self.define_params(10) is not None:
                left_corner = self.define_params(9)
                right_corner = self.define_params(10)
                return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                                       max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))
            return False
        return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                               max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))

    def in_green_zone(self, x, y):
        left_corner = self.define_params(12)
        right_corner = self.define_params(15)
        if left_corner is None or right_corner is None:
            if self.define_params(13) is not None and self.define_params(14) is not None:
                left_corner = self.define_params(13)
                right_corner = self.define_params(14)
                return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                                       max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))
            return False
        return self.is_in_zone(x, y, min(left_corner[0], right_corner[0]), min(left_corner[1], right_corner[1]),
                               max(left_corner[0], right_corner[0]), max(left_corner[1], right_corner[1]))

    def define_params(self, marker_id):
        if marker_id in np.ravel(self.ids):
            index = np.where(self.ids == marker_id)[0][0]
            return self.detector.center_coords(index, self.corners)
        return None

    def define_zone(self, ids, corners, idx):
        self.ids = ids
        self.corners = corners

        coords = self.center_coords(idx, self.corners)
        x = coords[0]
        y = coords[1]

        if self.in_red_zone(x, y):
            return "red"
        if self.in_blue_zone(x, y):
            return "blue"
        if self.in_yellow_zone(x, y):
            return "yellow"
        if self.in_green_zone(x, y):
            return "green"
        return "none"
