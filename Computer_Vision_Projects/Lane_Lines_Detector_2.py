import cv2
import numpy as np
from itertools import chain

video = '..//Images_and_videos//lane1-straight.mp4'

video_capture = cv2.VideoCapture(video)
if video_capture.isOpened():
    print('Success.')
else:
    print('Failed to open the video file.')

frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

video_writer = cv2.VideoWriter('Lane_Lines_Detector.mp4', cv2.VideoWriter_fourcc(*'FMP4'),
                              20, (frame_width, frame_height))

# frame width: 960
# frame height: 540
# channels: 3
while True:
    has_frames, frame = video_capture.read()
    if not has_frames:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, frame_thresh = cv2.threshold(frame_gray, 190, 255, cv2.THRESH_BINARY)

    roi_points_1 = np.array([[[80, 540],
                              [420, 330],
                              [470, 330],
                              [160, 540]]])

    roi_points_2 = np.array([[[800, 540],
                              [880, 540],
                              [550, 330],
                              [500, 330]]])

    image_blank_left = np.zeros_like(frame_thresh)
    image_blank_right = np.zeros_like(frame_thresh)

    ignore_mask_color = (255, 255, 255)

    frame_poly_left = cv2.fillPoly(image_blank_left, roi_points_1, ignore_mask_color)
    frame_poly_right = cv2.fillPoly(image_blank_right, roi_points_2, ignore_mask_color)

    frame_masked_left = cv2.bitwise_and(frame_thresh, frame_poly_left)
    frame_masked_right = cv2.bitwise_and(frame_thresh, frame_poly_right)

    lines_left = cv2.HoughLinesP(frame_masked_left, 1, np.pi / 180, 5, 100)
    lines_right = cv2.HoughLinesP(frame_masked_right, 1, np.pi / 180, 5, 100)

    frame_lines = np.zeros((frame.shape[0], frame.shape[1], 3), dtype='uint8')

    for line_L in lines_left:
        for line_R in lines_right:
            for xl1, yl1, xl2, yl2 in line_L:
                for xr1, yr1, xr2, yr2 in line_R:
                    roi_points_3 = np.array([[[xl1, yl1],
                                              [xl2, yl2],
                                              [xr2, yr2],
                                              [xr1, yr1]]])
                    cv2.fillPoly(frame_lines, roi_points_3, (255, 255, 0))

    for line in lines_left:
        for xl1, yl1, xl2, yl2 in line:
            cv2.line(frame_lines, (xl1, yl1), (xl2, yl2), (0, 255, 255), 10, cv2.LINE_8)

    for line in lines_right:
        for xr1, yr1, xr2, yr2 in line:
            cv2.line(frame_lines, (xr1, yr1), (xr2, yr2), (0, 255, 255), 10, cv2.LINE_8)

    frame_blank = np.zeros((frame.shape[0], frame.shape[1], 3), dtype='uint8')

    key = cv2.waitKey(10)

    if key == 27 or key == ord('q'):
        break

    frame_combined = cv2.addWeighted(frame, 1, frame_lines, 0.3, 0)

    cv2.imshow('Lane_Lines_Detector', frame_combined)

    video_writer.write(frame_combined)

cv2.destroyAllWindows()
video_capture.release()
video_writer.release()