import cv2
import numpy as np

video_cap = cv2.VideoCapture(1)
frame_width = video_cap.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
if video_cap.isOpened():
    print('Yes')
else:
    print('No')

codec = cv2.VideoWriter_fourcc(*'FMP4')
fps = 30

video_writer_1 = cv2.VideoWriter('Original_stream.mp4', codec, fps, (int(frame_width), int(frame_height)))
video_writer_2 = cv2.VideoWriter('GRAY.mp4', codec, fps, (int(frame_width), int(frame_height)))
video_writer_3 = cv2.VideoWriter('HSV.mp4', codec, fps, (int(frame_width), int(frame_height)))

while True:
    has_frame, frame = video_cap.read()
    if not has_frame:
        break

    frame = cv2.flip(frame, 1)

    # Grayscale frames
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray_EQ = cv2.equalizeHist(frame_gray)
    frame_gray_EQ = cv2.cvtColor(frame_gray_EQ, cv2.COLOR_GRAY2BGR)

    # HSV frames
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_hsv_EQ = frame_hsv.copy()
    frame_hsv_EQ[:, :, 2] = cv2.equalizeHist(frame_hsv_EQ[:, :, 2])
    frame_hsv_EQ_BGR = cv2.cvtColor(frame_hsv_EQ, cv2.COLOR_HSV2BGR)

    # Threshold
    retval, frame_thresh = cv2.threshold(frame_gray_EQ, 200, 255, cv2.THRESH_BINARY)

    # CLAHE histogram equalization
    clahe = cv2.createCLAHE(clipLimit=7.0, tileGridSize=(20, 20))
    frame_hsv[:, :, 2] = clahe.apply(frame_hsv_EQ[:, :, 2])
    frame_hsv_CLAHE = cv2.cvtColor(frame_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('Original', frame)
    cv2.imshow('Test', frame_gray_EQ)
    cv2.imshow('Test2', frame_hsv_CLAHE)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

    video_writer_1.write(frame)
    video_writer_2.write(frame_gray_EQ)
    video_writer_3.write(frame_hsv_CLAHE)

cv2.destroyAllWindows()
video_cap.release()
video_writer_1.release()
video_writer_2.release()
video_writer_3.release()
