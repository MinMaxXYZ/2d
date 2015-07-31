# Silhouette detection 

## Dependencies
- Numpy
- OpenCV

## Main steps
- Read 2 images (background, front / side)
- Subtract 2 images, generate the diff_image
- Convert to grayscale and normalize
- Apply gaussian blur and Canny edge detector
- Dilate to close gaps
- Flood fill the image from borders
- Erode to account for previous dilation
- Find largest contour
- Mask original image
- Apply the freeman 8 connected chain codes

## How to run it
- Go to silhouette-detection folder
- Run this file directly by python: python silhouette.py
