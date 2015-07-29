# Silhouette detection 

## Dependencies
- Numpy
- OpenCV

## Main steps
- Read 2 images (background, front / side)
- Subtract 2 images, generate the diff_image
- Threshold diff_image (Ostu or adaptive threshold)
- Apply the Canny filter
- Apply the freeman 8 connected chain codes

## How to run it
- Go to silhouette-detection folder
- Run this file directly by python: python silhouette.py
