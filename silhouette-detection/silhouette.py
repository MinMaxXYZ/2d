import numpy as np
import cv2
    
def main():
    background = cv2.imread('../images/background.jpg', 1)
    front1 = cv2.imread('../images/side1.jpg', 1)

    # Change all images to HSV to remove the shadow
    hsv_background = cv2.cvtColor(background,cv2.COLOR_BGR2HSV)
    hsv_front1 = cv2.cvtColor(front1,cv2.COLOR_BGR2HSV)

    # Remove shadow from front image by setting v channel to fixed value
    hsv_front1[:,:,2] = 200
    hsv_background[:,:,2] = 200

    # Change all images back to bgr image
    background = cv2.cvtColor(hsv_background,cv2.COLOR_HSV2BGR)
    front = cv2.cvtColor(hsv_front1,cv2.COLOR_HSV2BGR)

    # Get the different between background image an front view image
    diff = cv2.subtract(background, front)

    # Convert different image to gray
    diff = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)

    # normalize 
    cv2.normalize(diff, diff, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)

    # Binary different image
    # Increase second params to reduce big salt and peppersize noise
    median = cv2.medianBlur(diff, 5)

    # Remove small object
    blur = cv2.GaussianBlur(median,(5,5),0) 

    # Apply the canny filter to the different
    edges = cv2.Canny(blur,0,40)

    # Dilate to close the gaps
    kernel = np.ones((5,5),np.uint8)
    dilation = cv2.dilate(edges,kernel,iterations = 1)

    # Floodfill the image by border
    

    # View the result
    while(1):
        cv2.imshow('image', dilation)
        k = cv2.waitKey(33)
        if k==27:    # Esc key to stop
            break

if __name__ == "__main__":
    main()
