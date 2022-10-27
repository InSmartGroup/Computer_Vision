import cv2
import numpy as np

# Create a video capture object
video_capture = cv2.VideoCapture(0)
has_frame, frame = video_capture.read()

# Create a video writer object and define its properties
codec = cv2.VideoWriter_fourcc(*'FMP4')
frame_size = (int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 30
video_writer = cv2.VideoWriter('Document_Scanner.mp4', codec, fps, frame_size)

# Main
while True:
    # Read the webcam
    has_frame, frame = video_capture.read()

    if not has_frame:
        break

    # Resize the source frame
    frame = cv2.resize(frame, None, fx=0.8, fy=0.8)

    # Get the size of the source image
    if len(frame.shape) > 3:
        height, width, color_channels, alpha_channel = frame.shape
    elif len(frame.shape) == 3:
        height, width, color_channels = frame.shape
    else:
        height, width = frame.shape

    # Convert the source image to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    retval, frame_thresh = cv2.threshold(frame_gray, 200, 255, cv2.THRESH_BINARY)

    # Concatenate image processing stages
    frames_row_1 = np.hstack([frame, frame])
    frames_row_2 = np.hstack([frame, frame])
    frames_stacked = np.vstack([frames_row_1, frames_row_2])

    # Find all image contours
    contours, hierarchy = cv2.findContours(frame_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # If no contours were detected
    if not contours:
        retval, frame_thresh = cv2.threshold(frame_gray, 180, 255, cv2.THRESH_BINARY)
        if not contours:
            retval, frame_thresh = cv2.threshold(frame_gray, 170, 255, cv2.THRESH_BINARY)
            if not contours:
                retval, frame_thresh = cv2.threshold(frame_gray, 160, 255, cv2.THRESH_BINARY)

    # If any contours were detected
    if contours is not None:
        # Retrieve only the largest contour
        contour_largest = np.array([])
        contour_filtered = []
        max_area = 0
        destination_points = np.float32([[0, 0],
                                         [0, height - 1],
                                         [width - 1, height - 1],
                                         [width - 1, 0]])

        # Create a blank image and specify interest points for both images
        image_blank = np.zeros_like(frame_thresh).astype(np.uint8)

        for i in contours:
            area = cv2.contourArea(i)
            if area > 5000:
                perimeter = cv2.arcLength(i, True)
                approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
                if area > max_area and len(approx) == 4:
                    contour_largest = approx
                    max_area = area
                    contour_filtered.append(i)
                    contour_points = np.float32(contour_largest)

                    # Create a warp perspective matrix and warp the source image
                    matrix = cv2.getPerspectiveTransform(contour_points, destination_points)

                    # Draw the contour to mark the document
                    frame_contours = cv2.drawContours(frame.copy(), contour_filtered, -1,
                                                      (0, 255, 255), 3, cv2.LINE_AA)
                    frame_warped = cv2.warpPerspective(frame, matrix, (width, height))

                    # Create a scan-like image
                    frame_scan = cv2.adaptiveThreshold(cv2.cvtColor(frame_warped, cv2.COLOR_BGR2GRAY),
                                                       255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
                    frame_scan = cv2.cvtColor(frame_scan, cv2.COLOR_GRAY2BGR)
                    frames_row_1 = np.hstack([frame, frame_contours])
                    frames_row_2 = np.hstack([frame_warped, frame_scan])
                    frames_stacked = np.vstack([frames_row_1, frames_row_2])
    else:
        frame_warped = frame.copy()
        frame_scan = frame.copy()

    # Convert all binary images to BGR
    frame_gray = cv2.cvtColor(frame_gray, cv2.COLOR_GRAY2BGR)
    frame_thresh = cv2.cvtColor(frame_thresh, cv2.COLOR_GRAY2BGR)

    # Resize the stacked image so it fits the screen
    # frames_stacked = cv2.resize(frames_stacked, None, fx=0.8, fy=0.8)

    # Display the result
    cv2.imshow('Document Scanner', frames_stacked)

    # Define keyboard keys
    key = cv2.waitKey(1)

    if key == 27 or key == ord('q') or key == ord('Q'):
        break

cv2.destroyAllWindows()
video_capture.release()
video_writer.release()
