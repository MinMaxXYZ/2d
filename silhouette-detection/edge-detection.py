import numpy as np
import cv2
    
def main():
    background = cv2.imread('background.jpg', 0)
    front1 = cv2.imread('front1.jpg', 0)

    diff1 = front1 - background

    ret1,th1 = cv2.threshold(diff1,127,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    edges1 = cv2.Canny(diff1,100,200)

    while(1):
        cv2.imshow('image', th1)
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            break

if __name__ == "__main__":
    main()
