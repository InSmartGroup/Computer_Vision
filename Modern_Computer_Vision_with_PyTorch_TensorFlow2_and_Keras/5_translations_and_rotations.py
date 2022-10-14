import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
image = cv2.imread('..//Images_and_videos//Volleyball.jpeg')

# Print the shape of an image
print(image.shape)

# Resize the image
image = cv2.resize(image, None, fx=0.7, fy=0.7)

# Get width and height of the image
width = image.shape[1]
height = image.shape[0]

# Specify the image shift parameters
width_shift = int(width / 8)
height_shift = int(height / 8)

# Create a shift kernel
shift_kernel = np.array([[1, 0, width_shift], [0, 1, height_shift]]).astype(np.float32)

# Shift the image
image_shifted = cv2.warpAffine(image, shift_kernel, (width, height))

# Identify the width and height center of the image
width_center = int(image.shape[1] / 2)
height_center = int(image.shape[0] / 2)

# Create an image rotation kernel
rotation_kernel = cv2.getRotationMatrix2D((width_center, height_center), 42, 1)

# Rotate the image
image_rotated = cv2.warpAffine(image, rotation_kernel, (width, height))

# Flip the image
image_flipped_horiz = cv2.flip(image, 1)
image_flipped_vert = cv2.flip(image, 0)

# Display the images
# show('Original image', image)
# show('Image shifted', image_shifted)
# show('Image rotated', image_rotated)
show('Image, flipped horizontally', image_flipped_horiz)
show('Image, flipped vertically', image_flipped_vert)
