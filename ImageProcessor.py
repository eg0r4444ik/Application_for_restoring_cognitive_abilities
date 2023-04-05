import numpy as np
from skimage.color import rgb2lab, deltaE_cie76

int error = 1

class ImageProcessor:
    def __init__(self):
        pass

    def matches_red(self, pix):
        return (pix[0] - pix[1]) > 80 and (pix[0] - pix[2]) > 80

    def process(self, img):
        lab = rgb2lab(img)
        red1 = [200, 20, 20]
        red2 = [90, 20, 20]
        threshold1 = 30
        threshold2 = 10

        red_3d1 = np.uint8(np.asarray([[red1]]))
        red_3d2 = np.uint8(np.asarray([[red2]]))

        black_3d = np.uint8(np.asarray([[[0, 0, 0]]]))
        dE_red1 = deltaE_cie76(rgb2lab(red_3d1), lab)
        dE_red2 = deltaE_cie76(rgb2lab(red_3d2), lab)
        img[dE_red1 < threshold1] = black_3d
        img[dE_red2 < threshold2] = black_3d
