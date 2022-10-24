import cv2
import numpy as np

# Read the images
destination_image = cv2.imread('../Images_and_videos/times-square.jpg')
source_image = cv2.imread('../Images_and_videos/Apollo-8-Launch.jpg')

# Specify window name
window_name = 'Destination Image'


# Define a mouse callback function
def mouse_points(event, x, y, flags, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Render yellow circles in the destination image
        cv2.circle(data['image'], (x, y), radius=5, color=(0, 255, 255), thickness=-1, lineType=cv2.LINE_AA)
        cv2.imshow(window_name, data['image'])

        # Add at least 4 ROI points to the dictionary
        if len(data['points']) < 4:
            data['points'].append([x, y])


# Define a function for retrieving ROI points in the destination image
def get_roi_points(image):
    # Set up data to send to mouse handler function
    data = {'image': image.copy(), 'points': []}

    # Set the callback function for any mouse event
    cv2.imshow(window_name, image)
    cv2.setMouseCallback(window_name, mouse_points, data)
    cv2.waitKey(0)

    # Convert the list of 2D points to an array
    roi_points = np.vstack(data['points']).astype(float)

    return roi_points


# Compute the coordinates for the four corners of the source image
size = source_image.shape
source_points = np.array([[0, 0], [size[1] - 1, 0], [size[1] - 1, size[0] - 1], [0, size[0] - 1]], dtype=float)

# Get four corners of the billboard
print('Click on four corners of a billboard and then press ENTER')

# Retrieve the ROI points from the user mouse clicks
destination_roi = get_roi_points(destination_image)

# Compute the homography
homography, status = cv2.findHomography(source_points, destination_roi)

# Warp source image onto the destination image
warped_image = cv2.warpPerspective(source_image, homography,
                                   (destination_image.shape[1], destination_image.shape[0]))

# Black out polygonal area in the destination image
cv2.fillConvexPoly(destination_image, destination_roi.astype(int), 0, 16)

# Add the warped image to the destination image
destination_image = destination_image + warped_image

# Display the updated image with the virtual billboard
cv2.imshow(window_name, destination_image)
cv2.waitKey(0)

cv2.destroyAllWindows()
