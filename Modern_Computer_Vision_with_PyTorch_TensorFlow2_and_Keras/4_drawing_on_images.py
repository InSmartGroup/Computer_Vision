import cv2
import numpy as np


# Define a function to display images
def show(title, source=None):
    cv2.imshow(title, source)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Create two blank black images
image_blank_3_channels = np.zeros((600, 600, 3), dtype=np.uint8)
image_blank_binary = np.zeros((600, 600), dtype=np.uint8)

# Check the shape of these images
print(f"Blank image, 3 channels: {image_blank_3_channels.shape}")
print(f"Black image, binary: {image_blank_binary.shape}")

# Draw a line
image_3_channels_line = cv2.line(image_blank_3_channels.copy(), (0, 0),
                                 (600, 600), (200, 100, 0), 3, cv2.LINE_AA)

# Draw a rectangle
image_3_channels_rect = cv2.rectangle(image_blank_3_channels.copy(), (120, 100), (440, 350),
                                      (0, 255, 255), 5, cv2.LINE_8)

# Draw a filled rectangle
image_3_channels_rect_2 = cv2.rectangle(image_blank_3_channels.copy(), (120, 100), (440, 350),
                                        (200, 0, 100), -1, cv2.LINE_8)

# Find the center of the image and draw a circle
center_height = int(image_blank_3_channels.shape[0] / 2)
center_width = int(image_blank_3_channels.shape[1] / 2)
image_3_channels_circle = cv2.circle(image_blank_3_channels.copy(), (center_width, center_height),
                                     100, (100, 0, 200), 5, cv2.LINE_AA)

# Draw a filled circle
image_3_channels_circle_2 = cv2.circle(image_blank_3_channels.copy(), (center_width, center_height),
                                       200, (0, 100, 200), -1, cv2.LINE_AA)

# Make an array and draw polygons
poly_array = np.array([[20, 50], [80, 100], [135, 140], [175, 200], [270, 450]])
image_poly = cv2.polylines(image_blank_3_channels.copy(), [poly_array], True, (255, 0, 0), 5)

# Draw filled polygons
image_poly_filled = cv2.fillPoly(image_blank_3_channels.copy(), [poly_array], (255, 0, 255))

# Add text to an image
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
font_size = 2
color = (255, 255, 255)
thickness = 1
image_text = cv2.putText(image_blank_3_channels.copy(), 'This is some text', (60, 300),
                         font, font_size, color, thickness, cv2.LINE_AA)

# Display the images
# show('Blank, 3 channel', image_blank_3_channels)
# show('Blank, binary', image_blank_binary)
# show('Image, line', image_3_channels_line)
# show('Image, rectangle', image_3_channels_rect)
# show('Image, filled rectangle', image_3_channels_rect_2)
# show('Image, circle', image_3_channels_circle)
# show('Image, filled circle', image_3_channels_circle_2)
# show('Image, polygon', image_poly)
# show('Image, filled polygon', image_poly_filled)
# show('Image, text added', image_text)
