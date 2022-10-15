import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
source_image = cv2.imread('..//Images_and_videos//tulips.jpg')

# Convert the image to RGB
image_rgb = cv2.cvtColor(source_image, cv2.COLOR_BGR2RGB)

# Convert the image to HSV
image_hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)

# Display the result
# show('RGB image', image_rgb)
# show('HSV image', image_hsv)
