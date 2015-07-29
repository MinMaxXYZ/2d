import numpy as np
import cv2
    
def main():
    background = cv2.imread('../images/bg.png', 0)
    front1 = cv2.imread('../images/ft.png', 0)

    # Get the different between background image an front view image
    diff1 = background - front1

    # Binary different image
    # increase second params to reduce big salt and peppersize noise
    blur = cv2.medianBlur(diff1,9) 
    ret1,th1 = cv2.threshold(blur,225,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

    # Apply the canny filter to the different
    edges1 = cv2.Canny(diff1,100,200)

    # View the result
    while(1):
        cv2.imshow('image', th1)
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            break

if __name__ == "__main__":
    main()
