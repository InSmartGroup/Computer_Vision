import cv2
import numpy as np

# Read the source image
source_image = cv2.imread('..//Images_and_videos//scanned-form.jpg')
print(f"Source image shape: {source_image.shape}")

# Resize the source image if it's too large
if source_image.shape[0] > 2000:
    source_image = cv2.resize(source_image, None, fx=0.3, fy=0.3)
elif source_image.shape[0] > 1000:
    source_image = cv2.resize(source_image, None, fx=0.5, fy=0.5)
elif source_image.shape[0] > 650:
    source_image = cv2.resize(source_image, None, fx=0.6, fy=0.6)

# Get the size of the source image
if len(source_image.shape) > 3:
    height, width, color_channels, alpha_channel = source_image.shape
elif len(source_image.shape) == 3:
    height, width, color_channels = source_image.shape
else:
    height, width = source_image.shape

# Convert the source image to grayscale
image_gray = cv2.cvtColor(source_image, cv2.COLOR_BGR2GRAY)

# Threshold the image
retval, image_thresh = cv2.threshold(image_gray, 200, 255, cv2.THRESH_BINARY)

# Find all image contours
contours, hierarchy = cv2.findContours(image_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# If no contours were detected
if contours is None:
    retval, image_thresh = cv2.threshold(image_gray, 180, 255, cv2.THRESH_BINARY)
    if contours is None:
        retval, image_thresh = cv2.threshold(image_gray, 160, 255, cv2.THRESH_BINARY)
        if contours is None:
            retval, image_thresh = cv2.threshold(image_gray, 140, 255, cv2.THRESH_BINARY)
            if contours is None:
                retval, image_thresh = cv2.threshold(image_gray, 100, 255, cv2.THRESH_BINARY)

# Retrieve only the largest contour
contour_largest = np.array([])
contour_filtered = []
max_area = 0
for i in contours:
    area = cv2.contourArea(i)
    if area > 5000:
        perimeter = cv2.arcLength(i, True)
        approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
        if area > max_area and len(approx) == 4:
            contour_largest = approx
            max_area = area
            contour_filtered.append(i)

# Draw the contour to mark the document
image_contours = cv2.drawContours(source_image.copy(), contour_filtered, -1,
                                  (0, 255, 255), 3, cv2.LINE_AA)

# Create a blank image and specify interest points for both images
image_blank = np.zeros_like(image_thresh).astype(np.uint8)
contour_points = np.float32(contour_largest)

try:
    destination_points = np.float32([[width - 1, 0],
                                     [0, 0],
                                     [0, height - 1],
                                     [width - 1, height - 1]])

except cv2.error:
    destination_points = np.float32([[0, 0],
                                     [width - 1, 0],
                                     [height - 1, width - 1],
                                     [0, height - 1]])

# Create a warp perspective matrix and warp the source image
matrix = cv2.getPerspectiveTransform(contour_points, destination_points)
image_warped = cv2.warpPerspective(source_image, matrix, (width, height))

# Create a typewriter-like image
image_scan = cv2.adaptiveThreshold(cv2.cvtColor(image_warped, cv2.COLOR_BGR2GRAY),
                                   255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 5)

# Convert all binary images to BGR
image_gray = cv2.cvtColor(image_gray, cv2.COLOR_GRAY2BGR)
image_thresh = cv2.cvtColor(image_thresh, cv2.COLOR_GRAY2BGR)
image_scan = cv2.cvtColor(image_scan, cv2.COLOR_GRAY2BGR)

# Concatenate image processing stages
images_row_1 = np.hstack([source_image, image_contours])
images_row_2 = np.hstack([image_warped, image_scan])
images_stacked = np.vstack([images_row_1, images_row_2])

# Resize the stacked image so it fits the screen
images_stacked = cv2.resize(images_stacked, None, fx=0.65, fy=0.65)

# Display the result
cv2.imshow('Document Scanner', images_stacked)

# Define keyboard input
key = cv2.waitKey(0)

if key == 27 or key == ord('q') or key == ord('Q'):
    cv2.destroyAllWindows()
elif key == ord('s') or key == ord('S'):
    cv2.imwrite('Scanned_Document.jpg', images_stacked)
