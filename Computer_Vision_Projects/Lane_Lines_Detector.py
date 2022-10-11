import cv2
import numpy as np
from cvhandle import *

PATH = 'C://Users//gostapenko//NEW_Pycharm_Projects//MY_CV_NOTEBOOKS//OpenCV Course Notebooks//lane1-straight.mp4'

# Create a video capture object
video_capture = cv2.VideoCapture(PATH)

# Check if it has opened properly
if video_capture.isOpened():
    print('Success.')
else:
    print('Failed to open the video file.')

# Get the video file properties
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)
fps = 20

# Create a video writer object
video_writer = cv2.VideoWriter('Lane_lines_detector.mp4', cv2.VideoWriter_fourcc(*'FMP4'), fps, frame_size)

# Process the loop
while True:
    # Read the video file
    has_frames, frame = video_capture.read()
    if not has_frames:
        break

    # Process the frames
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, frame_thresh = cv2.threshold(frame_gray, 190, 255, cv2.THRESH_BINARY)

    # Create a lane lines ROI and the mask
    mask = np.zeros_like(frame_thresh)
    roi_points = np.array([[[100, 540],
                            [420, 340],
                            [600, 340],
                            [900, 540]]])
    ignore_mask_color = (255, 255, 255)
    frame_poly = cv2.fillPoly(mask, roi_points, ignore_mask_color)
    frame_mask = cv2.bitwise_and(frame_poly, frame_thresh)

    # frame_lines = np.zeros((frame_mask.shape[0], frame_mask.shape[1], 3), dtype='uint8')
    # lines = cv2.HoughLinesP(frame_mask, 1, np.pi / 180, 50)
    # for line in lines:
    #     for x1, y1, x2, y2 in line:
    #         cv2.line(frame_lines, (x1, y1), (x2, y2), (0, 255, 255), 3, lineType=cv2.LINE_AA)

    # Find and draw lines
    contours, hierarchy = cv2.findContours(frame_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    # frame_contours = np.zeros((frame_mask.shape[0], frame_mask.shape[1], 3), dtype='uint8')
    for contour in contours:
        cv2.drawContours(frame, contour, -1, (0, 255, 255), 5, cv2.LINE_AA)

    # Specify keyboard input
    key = cv2.waitKey(5)

    # Terminate
    if key == 27 or key == ord('Q') or key == ord('q'):
        break

    # Display the video file
    cv2.imshow('Lane_lines_detector', frame)

    # Write the video file
    video_writer.write(frame)

cv2.destroyAllWindows()
video_capture.release()
video_writer.release()
