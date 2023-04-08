import time

import numpy as np
from skimage.color import rgb2lab, deltaE_cie76

from AreaAnalyzer import AreaAnalyzer


# final test
class ImageProcessor:
    def __init__(self):
        self.analyzer = AreaAnalyzer()

    def matches_red(self, pix):
        return (pix[0] - pix[1]) > 80 and (pix[0] - pix[2]) > 80

    def process(self, img):
        pixels_counter = [0, 0, 0]

        lab = rgb2lab(img)

        red1 = [255, 70, 70]
        red2 = [100, 20, 20]
        threshold1 = 40
        threshold2 = 20

        blue1 = [60, 120, 200]
        blue2 = [120, 150, 235]
        # blue3 = [50, 60, 100] # Это вроде синий, но темный другого оттенка тоже берет
        threshold3 = 20
        threshold4 = 20
        # threshold5 = 5

        green1 = [255, 255, 255]
        threshold6 = 10

        red_3d1 = np.uint8(np.asarray([[red1]]))
        red_3d2 = np.uint8(np.asarray([[red2]]))

        blue_3d1 = np.uint8(np.asarray([[blue1]]))
        blue_3d2 = np.uint8(np.asarray([[blue2]]))
        # blue_3d3 = np.uint8(np.asarray([[blue3]]))

        green_3d1 = np.uint8(np.asarray([[blue1]]))

        black_3d = np.uint8(np.asarray([[[0, 0, 0]]]))
        dE_red1 = deltaE_cie76(rgb2lab(red_3d1), lab)
        dE_red2 = deltaE_cie76(rgb2lab(red_3d2), lab)
        dE_blue1 = deltaE_cie76(rgb2lab(blue_3d1), lab)
        dE_blue2 = deltaE_cie76(rgb2lab(blue_3d2), lab)
        dE_green1 = deltaE_cie76(rgb2lab(green_3d1), lab)
        # dE_green2 = deltaE_cie76(rgb2lab(green_3d2), lab)
        # dE_blue3 = deltaE_cie76(rgb2lab(blue_3d3), lab)
        pixels_counter[0] = len(img[dE_red1 < threshold1]) + len(img[dE_red2 < threshold2])
        pixels_counter[1] = len(img[dE_blue1 < threshold3]) + len(
            img[dE_blue2 < threshold4])  # + len(img[dE_blue3 < threshold5])
        pixels_counter[1] = len(img[dE_green1 < threshold6])
        # print(pixels_counter[0])
        # print(pixels_counter[1])
        # print(pixels_counter[2])
        self.analyzer.analyze(pixels_counter[0], pixels_counter[1])
        time.sleep(10)
        img[dE_red1 < threshold1] = black_3d
        img[dE_red2 < threshold2] = black_3d

        img[dE_blue1 < threshold3] = black_3d
        img[dE_blue2 < threshold4] = black_3d
        # img[dE_blue3 < threshold4] = black_3d

        img[dE_green1 < threshold6] = black_3d
        # img[dE_green2 < threshold7] = black_3d