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

    def get_fingerprint_data(self, image):
       self.get_skeletonize(image)

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

image = cv2.imread('D:\Desktop\Spring2021\CSE410\FingerPrint\Images\image1.jpg', 0)
main(image)