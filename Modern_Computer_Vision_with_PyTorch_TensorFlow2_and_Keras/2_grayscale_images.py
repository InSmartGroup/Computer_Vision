import cv2
import numpy as np

# Read an image
image = cv2.imread('..//Images_and_videos//castara.jpeg')

# Check the image shape
print(f"Image width: {image.shape[1]}")
print(f"Image height: {image.shape[0]}")
print(f"Image color channels: {image.shape[2]}")


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Resize and image
image = cv2.resize(image, None, fx=0.5, fy=0.5)

# Convert the image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the image using the new function
show('Image', image_gray)
