import cv2
import numpy as np

# Video capture object
video_capture = cv2.VideoCapture(0)

if video_capture.isOpened():
    print('Success.')
else:
    print('Error accessing the web camera.')

# Constants for image processing
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10, 10))
red_color = (0, 0, 255)
yellow_color = (0, 255, 255)
blue_color = (255, 0, 0)

# Background subtractor object
background_subtractor = cv2.createBackgroundSubtractorKNN(history=1)

# Frame parameters
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_fps = int(video_capture.get(cv2.CAP_PROP_FPS))
frame_codec = video_capture.get(cv2.CAP_PROP_FOURCC)
frame_size = (frame_width, frame_height)
new_frame_size = (int(frame_width * 2), int(frame_height))

# Video writer object
video_writer = cv2.VideoWriter('Motion_Detector.mp4', cv2.VideoWriter_fourcc(*'FMP4'), 30, new_frame_size)

# Main loop
while True:
    # Read the webcam stream
    has_frame, frame = video_capture.read()

    if not has_frame:
        break

    # Mirror the frame
    frame = cv2.flip(frame, 1)

    # Keyboard input
    key = cv2.waitKey(1)

    if key == 27 or key == ord('q') or key == ord('Q'):
        break

    # Subtract the background and erode the frame
    foreground_mask = background_subtractor.apply(frame)
    foreground_mask_eroded = cv2.erode(foreground_mask, kernel)
    motion_area = cv2.findNonZero(foreground_mask_eroded)

    # Calculate the bounding box parameters
    x, y, w, h = cv2.boundingRect(motion_area)

    if motion_area is not None:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=3, lineType=cv2.LINE_AA)

    # Stack the output frames
    frame_foreground_mask_eroded = cv2.cvtColor(foreground_mask_eroded, cv2.COLOR_GRAY2BGR)
    frame_composite = np.hstack([frame_foreground_mask_eroded, frame])

    cv2.putText(frame_composite, 'KNN Background Subtraction & Motion Detection', (10, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

    # Display the result
    cv2.imshow('Motion_Detector', frame_composite)

    # Write the processed stream
    video_writer.write(frame_composite)

cv2.destroyAllWindows()
video_capture.release()
video_writer.release()
