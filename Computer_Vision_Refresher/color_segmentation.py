import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image and convert it to HSV
source_image = cv2.imread('..//Images_and_videos//Emerald_Lakes_New_Zealand.jpg', 1)
image_hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)

# Define lower and upper bounds for each color channel
red_lower = np.array([165, 50, 40])
red_upper = np.array([180, 255, 255])
green_lower = np.array([25, 50, 40])
green_upper = np.array([85, 255, 255])
blue_lower = np.array([95, 50, 40])
blue_upper = np.array([125, 255, 255])

# Define a color mask for each channel
red_mask = cv2.inRange(image_hsv, red_lower, red_upper)
green_mask = cv2.inRange(image_hsv, green_lower, green_upper)
blue_mask = cv2.inRange(image_hsv, blue_lower, blue_upper)

# # Check image masks
# plt.imshow(red_mask, cmap='gray')
# plt.show()
# plt.imshow(green_mask, cmap='gray')
# plt.show()
# plt.imshow(blue_mask, cmap='gray')
# plt.show()

# Segment the colors
red_segmented = cv2.bitwise_and(src1=source_image, src2=source_image, mask=red_mask)
green_segmented = cv2.bitwise_and(src1=source_image, src2=source_image, mask=green_mask)
blue_segmented = cv2.bitwise_and(source_image, source_image, mask=blue_mask)

# Check the result
plt.imshow(red_segmented[:, :, ::-1])
plt.show()
plt.imshow(green_segmented[:, :, ::-1])
plt.show()
plt.imshow(blue_segmented[:, :, ::-1])
plt.show()
