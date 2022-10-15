import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
source_image = cv2.imread('..//Images_and_videos//imageTransformation.png')
print(source_image.shape)

# Convert an image to .png
cv2.imwrite('imageTransformation.jpg', source_image)

# Read and display the converted image
source_image = cv2.imread('imageTransformation.jpg')
print(source_image.shape)
# show('JPG image', source_image)

# Read the same image as grayscale
source_image = cv2.imread('imageTransformation.jpg', cv2.IMREAD_GRAYSCALE)
print(source_image.shape)
# show('Grayscale image', source_image)
