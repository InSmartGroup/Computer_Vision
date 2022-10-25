import cv2
import numpy as np

# Read the source image
source_image = cv2.imread('Images_and_videos//scanned-form.jpg')

# Get the source image shape
if len(source_image.shape) >= 3:
    height, width, color_channels = source_image.shape
elif len(source_image.shape) == 2:
    height, width = source_image.shape

# Resize the source image if it's too large
if source_image.shape[0] > 2000:
    source_image = cv2.resize(source_image, None, fx=0.3, fy=0.3)
elif source_image.shape[0] > 1000:
    source_image = cv2.resize(source_image, None, fx=0.5, fy=0.5)
elif source_image.shape[0] > 650:
    source_image = cv2.resize(source_image, None, fx=0.8, fy=0.8)

while True:
    image_blank = np.zeros((width, height, 3), dtype=np.uint8)

    # Convert the image to grayscale
    image_gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

    # Add some Gaussian blur
    image_gray_blurred = cv2.GaussianBlur(image_gray, (5, 5), 1)

    # Create trackbars
    trackbar_name = 'Trackbars'
    cv2.namedWindow(trackbar_name)
    cv2.resizeWindow(trackbar_name, 360, 240)
    cv2.createTrackbar('Threshold_1', trackbar_name, 200, 255, None)
    cv2.createTrackbar('Threshold_2', trackbar_name, 200, 255, None)

    # Detect edges
    image_edges = cv2.Canny(image_gray_blurred, )


