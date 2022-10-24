import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
image_bgr = cv2.imread('..//Images_and_videos//tulips.jpg', 1)
image_gray = cv2.imread('..//Images_and_videos//albert-einstein_gray.jpg', 0)

# Check image shapes
print(f"BGR source image shape: {image_bgr.shape}")
print(f"Grayscale source image shape: {image_gray.shape}")

# Resize the images and make them 2 times smaller
image_bgr_small = cv2.resize(image_bgr, dsize=None, fx=0.5, fy=0.5)
image_gray_small = cv2.resize(image_gray, fx=0.5, fy=0.5, dsize=None)
print(f"BGR image shape, small: {image_bgr_small.shape}")
print(f"Grayscale image shape, small: {image_gray_small.shape}")

# Resize the images and make them 25% larger
image_bgr_large = cv2.resize(image_bgr, fx=1.25, fy=1.25, dsize=None)
image_gray_large = cv2.resize(image_gray, None, fx=1.25, fy=1.25)
print(f"BGR image shape, large: {image_bgr_large.shape}")
print(f"Grayscale image shape, large: {image_gray_large.shape}")

# Resize the images using custom dimension size matrix
image_gray_custom = cv2.resize(image_gray, (200, 400), interpolation=cv2.INTER_LANCZOS4)
image_bgr_custom = cv2.resize(image_bgr, (300, 500), interpolation=cv2.INTER_CUBIC)
print(f"BGR image, custom shape: {image_bgr_custom.shape}")
print(f"Grayscale image, custom shape: {image_gray_custom.shape}")

# Display the images
# show('Grayscale source image', image_gray)
# show('BGR source image', image_bgr)
# show('Grayscale image, small', image_gray_small)
# show('BGR image, small', image_bgr_small)
# show('Grayscale image, large', image_gray_large)
# show('BGR image, large', image_bgr_large)
# show('Grayscale image, custom resize', image_gray_custom)
# show('BGR image, custom resize', image_bgr_custom)
