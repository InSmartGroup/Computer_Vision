import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image as grayscale
source_image = cv2.imread('..//Images_and_videos//albert-einstein_gray.jpg', cv2.IMREAD_GRAYSCALE)

# Check the shape and type of the image
print(source_image.shape)
print(source_image.dtype)
print(type(source_image))

# Create a window and display the image
cv2.namedWindow('Images', cv2.WINDOW_NORMAL)

# Replace eyes with white rectangles
image = source_image.copy()
image[330:440, 300:400] = 255
image[330:440, 430:520] = 255

# Display the result
# show('Images', source_image)
# show('Original image', source_image)
# show('Eyes replaced', image)
