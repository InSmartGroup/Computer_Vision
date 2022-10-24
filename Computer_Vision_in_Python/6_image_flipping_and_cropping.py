import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read the image
image_gray = cv2.imread('..//Images_and_videos//albert-einstein_gray.jpg', 0)

# Check the shape of the image
print(f"Image shape: {image_gray.shape}")

# Crop an image by half
image_cropped = image_gray[0:int(image_gray.shape[0] / 2), :]
print(f"Cropped image shape: {image_cropped.shape}")

# Flip the image
image_flipped_horiz = cv2.flip(image_gray, 1)
image_flipped_vert = cv2.flip(image_gray, 0)
image_flipped_both = cv2.flip(image_gray, -1)

# Create a black image and iterate though each pixel
image_blank = np.zeros((255, 255), dtype=np.uint8)
for height in range(image_blank.shape[1]):
    for width in range(image_blank.shape[0]):
        image_blank[height, width] = height

# Display the result
# show('Cropped image', image_cropped)
# show('Vertical flip', image_flipped_vert)
# show('Horizontal flip', image_flipped_horiz)
# show('Both sides flip', image_flipped_both)
show('Gradient', image_blank)
