import cv2
import numpy as np
import skimage.morphology
from skimage.morphology import convex_hull_image, erosion
from skimage.morphology import square
from PIL import Image as im
import math

class Extract_FingerPrint(object):
    def __init__(self):
        self.mask = []
        self.skel = []
        self.minutiaTerm = []
        self.minutiaBif = []

    def get_fingerprint_data(self, image):
        self.get_skeletonize(image)

        self.get_termination_bifurication()

    def get_termination_bifurication(self):
        # change self.skel to true or false based on if it is of the white or black color
        self.skel = self.skel == 255

        # get number of rows and columns
        (rows, cols) = self.skel.shape

        self.minutiaTerm = np.zeros(self.skel.shape)
        self.minutiaBif = np.zeros(self.skel.shape)

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                if self.skel[i][j] == 1:
                    # False represents Black and True represents White
                    block = self.skel[i - 1:i + 2, j - 1: j + 2]

                    # sum up number of trues
                    block_val = np.sum(block)

                    # 2 trues => termination as 2 white lines end
                    # 4 trues => bifurication as 4 white lines are connected
                    if block_val == 2:
                        self.minutiaTerm[i, j] = 1
                    elif block_val == 4:
                        self.minutiaBif[i, j] = 1

    def get_skeletonize(self, image):
        # get array of only > gray color
        image = np.uint8(image > 128)

        # skeletonize the image array
        self.skel = skimage.morphology.skeletonize(image)

        data = im.fromarray(self.skel)
        data.save("skel_image.png")

        # increase sensitivity of color
        self.skel = np.uint8(self.skel) * 255

        data = im.fromarray(self.skel)
        data.save("skel_image_255.png")

        # generate mask of the image
        self.mask = image * 255

        data = im.fromarray(self.mask)
        data.save("mask_of_image.png")


def main(image_object):
    finger_extraction = Extract_FingerPrint()
    finger_extraction.get_fingerprint_data(image_object)

image = cv2.imread('Images\image1.jpg', 0)
main(image)