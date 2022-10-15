import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
image = cv2.imread('..//Images_and_videos//liberty.jpeg')

# Resize the image
image = cv2.resize(image, None, fx=0.5, fy=0.5)

# Convert the image to grayscale
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create an empty matrix with the same shape as the original image
image_blank = np.ones(image_gray.shape, dtype='uint8') * 100
print(image_blank.dtype)

# Add the grayscale image and the blank image to increase brightness
image_gray_bright = cv2.add(image_gray, image_blank)

# Now add these two images manually and check the result
image_gray_bright_2 = image_gray + image_blank

# Subtract the images
image_gray_dark = cv2.subtract(image_gray, image_blank)

# Now subtract these two images manually and check the result
image_gray_dark_2 = image_gray - image_blank

# Create two binary images
image_rect = np.zeros((500, 500), dtype='uint8')
image_rect_1 = cv2.rectangle(image_rect.copy(), (100, 100), (420, 420), (255, 255, 255), -1)
image_rect_2 = cv2.rectangle(image_rect.copy(), (100, 100), (380, 380), (255, 255, 255), 30)

# Use bitwise operation to these two images and check the result
images_bitwise_and = cv2.bitwise_and(image_rect_1, image_rect_2, None)
images_bitwise_or = cv2.bitwise_or(image_rect_1, image_rect_2, None)
images_bitwise_not = cv2.bitwise_not(image_rect_1, image_rect_2, None)
images_bitwise_xor = cv2.bitwise_xor(image_rect_1, image_rect_2, None)

# Display the images
# show('Original image', image)
# show('Grayscale image', image_gray)
# show('Blank image', image_blank)
# show('Grayscale image, added values', image_gray_bright)
# show('Grayscale image, manually added values', image_gray_bright_2)
# show('Grayscale image, subtracted values', image_gray_dark)
# show('Grayscale image, manually subtracted values', image_gray_dark_2)
# show('Image, rectangle 1', image_rect_1)
# show('Image, rectangle 2', image_rect_2)
# show('Bitwise And', images_bitwise_and)
# show('Bitwise Or', images_bitwise_or)
# show('Bitwise Not', images_bitwise_not)
# show('Bitwise Xor', images_bitwise_xor)
