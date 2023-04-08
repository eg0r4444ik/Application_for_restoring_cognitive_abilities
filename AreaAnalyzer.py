

class AreaAnalyzer:

    def __init__(self):
        self.red_s = 0
        self.blue_s = 0

    def analyze(self, new_r, new_b):
        if new_r - self.red_s > 2500 and new_r >= self.red_s:
            print("Убрали предмет из красной зоны")
        if self.red_s - new_r > 2500 and self.red_s >= new_r:
            print("Положили предмет в красную зону")
        if new_b - self.blue_s > 2500 and new_b >= self.blue_s:
            print("Убрали предмет из синей зоны")
        if self.blue_s - new_b > 2500 and self.blue_s >= new_b:
            print("Положили предмет в синюю зону")
        self.red_s = new_r
        self.blue_s = new_b