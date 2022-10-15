import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
source_image = cv2.imread('..//Images_and_videos//tulips.jpg')

# Convert the image to HSV
image_hsv = cv2.cvtColor(source_image, cv2.COLOR_BGR2HSV)

# Display the source image
# show('Source image', source_image)

# Detect only red tulips
lower_red_1 = np.array((0, 100, 70))
upper_red_1 = np.array((10, 255, 255))
image_mask_1 = cv2.inRange(image_hsv, lower_red_1, upper_red_1)

lower_red_2 = np.array((160, 100, 70))
upper_red_2 = np.array((180, 255, 255))
image_mask_2 = cv2.inRange(image_hsv, lower_red_2, upper_red_2)

image_mask = image_mask_1 | image_mask_2
image_result = cv2.bitwise_and(image_hsv, image_hsv, mask=image_mask)

# Convert the image to BGR
image_result = cv2.cvtColor(image_result, cv2.COLOR_HSV2BGR)

# Display the result
show('Red color segmented', image_result)

# Now detect only yellow tulips
lower_yellow = np.array((20, 100, 100))
upper_yellow = np.array((30, 255, 255))
mask = cv2.inRange(image_hsv, lower_yellow, upper_yellow)
image_result = cv2.bitwise_and(image_hsv, image_hsv, mask=mask)

# Convert the image to BGR
image_result = cv2.cvtColor(image_result, cv2.COLOR_HSV2BGR)

# Display the result
show('Yellow color segmented', image_result)
