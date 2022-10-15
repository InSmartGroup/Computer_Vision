import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
source_image = cv2.imread('..//Images_and_videos//tulips.jpg')
print(source_image.shape)
print(source_image.dtype)

# Create a named window to display the image
# cv2.namedWindow('Source image', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Blue channel', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Green channel', cv2.WINDOW_NORMAL)
# cv2.namedWindow('Red channel', cv2.WINDOW_NORMAL)

# Separate color channels
blue, green, red = source_image[:, :, 0], source_image[:, :, 1], source_image[:, :, 2]

# Manually merge color channels in reversed order to get the RGB image
image_rgb_manual = np.ones_like(source_image)
image_rgb_manual[:, :, 0], image_rgb_manual[:, :, 1], image_rgb_manual[:, :, 2] = red, green, blue

# Merge an RGB image using OpenCV
colors = (red, green, blue)
image_rgb_opencv = cv2.merge(colors)

# Create the Ukrainian flag from scratch
image_UA_flag = np.zeros((300, 600, 3), dtype='uint8')
image_UA_flag[0:150, :, 0] = 255
image_UA_flag[150:300, :, 2] = 255
image_UA_flag[150:300, :, 1] = 255

# Create the Italian flag from scratch
image_IT_flag = np.zeros((300, 600, 3), dtype='uint8')
image_IT_flag[:, 0:200, 1] = 255
image_IT_flag[:, 200:400, :] = 255
image_IT_flag[:, 400:600, 2] = 255

# Create the German flag from scratch
image_GR_flag = np.ones((300, 600, 3), dtype='uint8')
image_GR_flag[0:100, :, :] = 0
image_GR_flag[100:200, :, 2] = 255
image_GR_flag[200:300, :, 1:3] = 255

# Display all 4 images at the same time
# cv2.imshow('Source image', source_image)
# cv2.imshow('Blue channel', blue)
# cv2.imshow('Green channel', green)
# cv2.imshow('Red channel', red)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# show('Manually merged RGB image', image_rgb_manual)
# show('OpenCV-merged RGB image', image_rgb_opencv)
show('Ukrainian flag', image_UA_flag)
show('Italian flag', image_IT_flag)
show('German flag', image_GR_flag)
