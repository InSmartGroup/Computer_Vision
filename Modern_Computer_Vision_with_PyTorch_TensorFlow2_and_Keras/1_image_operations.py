import cv2
import numpy as np
import matplotlib.pyplot as plt

# Check OpenCV version
print(cv2.__version__)

# Read the image
image = cv2.imread('..//Images_and_videos//flowers.jpeg')

# Check the image shape and data type
print(image.shape)
print(image.dtype)

# Assign width, height, and color channels of the image
image_height = image.shape[0]
image_width = image.shape[1]
image_channels = image.shape[2]
print(f"Source image width: {image_width}")
print(f"Source image height: {image_height}")
print(f"Source image color channels: {image_channels}")

# Resize the image
image = cv2.resize(image, None, fx=0.7, fy=0.7)

# Display the image
cv2.imshow('IMAGE_TEST', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
