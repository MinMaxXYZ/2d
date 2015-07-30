# USAGE
# python silhouette2.py -f ../images/front1.jpg

# import the necessary packages
import numpy as np
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--front", required = True,
    help = "Path to the front image")
args = vars(ap.parse_args())

# load the puzzle and waldo images
front = cv2.imread(args["front"])

# Load the image, convert it to grayscale, and blur it slightly
front = cv2.cvtColor(front, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(front, (5, 5), 0)
cv2.imshow("Image", front)

thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 4)
cv2.imshow("Mean Thresh", thresh)

# We can also apply Gaussian thresholding in the same manner
thresh = cv2.adaptiveThreshold(blurred, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 3)
cv2.imshow("Gaussian Thresh", thresh)
cv2.waitKey(0)