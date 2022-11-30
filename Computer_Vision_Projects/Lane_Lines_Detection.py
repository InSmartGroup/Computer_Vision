import cv2
import numpy as np

# Path to a video file
video_path = '..//Images_and_videos//lane1-straight.mp4'

# Video capture object
video_capture = cv2.VideoCapture(video_path)

# Video open test
if video_capture.isOpened():
    print('Success.')
else:
    print('Unable to load the video.')

# Video file properties
video_frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
video_frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_codec = cv2.VideoWriter_fourcc(*'FMP4')
video_fps = int(video_capture.get(cv2.CAP_PROP_FPS))

# Frame size
frame_size = (video_frame_width, video_frame_height)

# Video writer object
video_writer = cv2.VideoWriter('Lane_Lines_Detection.mp4', video_codec, video_fps, frame_size)


while True:

    has_frames, frame = video_capture.read()
    if has_frames is None:
        break

    frame_copy = frame.copy()

    # Process the frame
    frame_gray = cv2.cvtColor(frame_copy, cv2.COLOR_BGR2GRAY)  # grayscale
    retval, frame_thresh = cv2.threshold(frame_gray, 190, 255, cv2.THRESH_BINARY)  # threshold from grayscale

    # Create a lane lines ROI and the mask
    mask = np.zeros_like(frame_thresh)
    roi_points = np.array([[[100, 540],
                            [440, 330],
                            [540, 330],
                            [900, 540]]])
    ignore_mask_color = 255
    frame_poly = cv2.fillPoly(mask, roi_points, ignore_mask_color)
    frame_mask = cv2.bitwise_and(frame_poly, frame_thresh)

    # Find and draw contours
    contours, hierarchy = cv2.findContours(frame_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        cv2.drawContours(frame_copy, contour, -1, color=(0, 255, 255), thickness=5, lineType=cv2.LINE_AA)

    # Resize the frames for better performance
    frame_copy = cv2.resize(frame_copy, None, fx=1, fy=1)
    frame_mask = cv2.resize(frame_mask, None, fx=0.65, fy=0.65)
    frame_thresh = cv2.resize(frame_thresh, None, fx=0.65, fy=0.65)

    # Display the processed stream
    cv2.imshow("Lane_Line_Detection", frame_copy)
    cv2.imshow("Threshold", frame_thresh)
    cv2.imshow("Mask", frame_mask)

    # Keyboard control
    key = cv2.waitKey(5)

    if key == ord('Q') or key == ord('q') or key == 27:
        break

    # Save the processed video
    video_writer.write(frame)

# Release the data
cv2.destroyAllWindows()
video_capture.release()
video_writer.release()