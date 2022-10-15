import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Read an image
image = cv2.imread('..//Images_and_videos//oxfordlibrary.jpeg')

# Check the shape of an image
print(image.shape)

# Resize the image using the auto-scaling
image_resized = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LANCZOS4)

# Check teh shape of the resized image
print(image_resized.shape)

# Resize the image using the custom shape
image_resized = cv2.resize(image, (720, 500), interpolation=cv2.INTER_LANCZOS4)

# Check the shape of the resized image
print(image_resized.shape)

# Resize the image and make it larger
image_resized = cv2.resize(image, (1500, 1000), interpolation=cv2.INTER_LANCZOS4)

# Get width and height of the source image
height, width = image.shape[:2]

# Specify start and end image cropping points and crop the image
start_row, start_column = int(height * 0.25), int(width * 0.25)
end_row, end_column = int(height * 0.75), int(width * 0.75)
image_cropped = image.copy()[start_row:end_row, start_column:end_column]

# Draw a rectangle around the cropped area
image_cropped_rect = cv2.rectangle(image.copy(), (start_column, start_row), (end_column, end_row),
                                   (0, 255, 0), 3, cv2.LINE_8)

# Display the images
# show('Original image', image)
# show('Resized image', image_resized)
# show('Cropped image', image_cropped)
show('Cropped area', image_cropped_rect)