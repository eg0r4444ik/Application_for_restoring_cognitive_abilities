class ArucoCoordsDetector:

    def __init__(self):
        self.corners = []

    def center_coords(self, aruco_id, corners):
        self.corners = corners
        cornerUL = self.corners[aruco_id][0][0]
        cornerBR = self.corners[aruco_id][0][2]

        center = [(cornerUL[0] + cornerBR[0]) / 2, (cornerUL[1] + cornerBR[1]) / 2]

        return center
