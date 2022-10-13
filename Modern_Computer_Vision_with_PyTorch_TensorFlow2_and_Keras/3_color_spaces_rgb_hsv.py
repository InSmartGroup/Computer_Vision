import cv2
import numpy as np

# Read the image
image = cv2.imread('..//Images_and_videos//castara.jpeg')


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Check the image shape and number of color channels
print(f"Image shape: {image.shape}")
print(f"Image color channels: {image.shape[2]}")

# Resize the image
image = cv2.resize(image, None, fx=0.5, fy=0.5)

# Split the image into separate color channels and check their shape
blue, green, red = cv2.split(image)
print(f"Blue channel: {blue.shape}")
print(f"Green channel: {green.shape}")
print(f"Red channel: {red.shape}")

# Check how each color channel looks like
image_zeros = np.zeros(image.shape[:2]).astype(np.uint8)
image_blue = cv2.merge((blue, image_zeros, image_zeros))
image_green = cv2.merge((image_zeros, green, image_zeros))
image_red = cv2.merge((image_zeros, image_zeros, red))

# Let's add some more values to separate color channels and see the result
image_blue_added = image_blue + 75
image_red_added = image_red + 50
image_green_added = image_red + 100

# Convert the source image to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Separate each color channel and see the result
hue, saturation, value = cv2.split(image_hsv)

# Display the images
# show('TEST_IMAGE', image)
# show('Blue_channel', image_blue)
# show('Green_channel', image_green)
# show('Red_channel', image_red)
# show('Blue channel boosted', image_blue_added)
# show('Green channel boosted', image_green_added)
# show('Red channel boosted', image_red_added)
show('Hue', hue)
show('Saturation', saturation)
show('Value', value)