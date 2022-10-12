import cv2
import numpy as np


def draw_lines(image):
    """Function to draw the lines"""
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), (0, 0, 255), 3, cv2.LINE_AA)
    return image


def separate_lines(lines):
    """Function for separating left and right lines depending on the slope"""
    left_lines = []
    right_lines = []
    for line in lines:
        for x1, y1, x2, y2 in line:
            if y1 > y2:
                left_lines.append([x1, y1, x2, y2])
            elif y1 < y2:
                right_lines.append([x1, y1, x2, y2])
    return left_lines, right_lines


def calculate_average(values):
    """Function to calculate average which will be used in extrapolating lines"""
    if len(values) > 0:
        n = len(values)
    else:
        n = 1
    return sum(values) / n



video = '..//Images_and_videos//lane1-straight.mp4'

video_capture = cv2.VideoCapture(video)

while True:
    has_frames, frame = video_capture.read()
    if not has_frames:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval, frame_thresh = cv2.threshold(frame_gray, 180, 255, cv2.THRESH_BINARY)

    frame_blank = np.zeros((frame.shape[0], frame.shape[1]), dtype='uint8')
    roi_points = np.array([[[100, 540],
                            [440, 330],
                            [540, 330],
                            [900, 540]]])
    ignore_mask_color = 255
    frame_poly = cv2.fillPoly(frame_blank, roi_points, (255, 255, 255))
    frame_masked = cv2.bitwise_and(frame_poly, frame_thresh, ignore_mask_color)
    frame_edges = cv2.Canny(frame_masked, 50, 100)
    frame_blurred = cv2.GaussianBlur(frame_edges, (3, 3), 0)
    lines = cv2.HoughLinesP(frame_blurred, 1, np.pi / 180, 10, 30)

    frame_blank2 = np.zeros((frame.shape[0], frame.shape[1], 3), dtype='uint8')



    key = cv2.waitKey(0)

    if key == 27 or key == ord('q'):
        break

    cv2.imshow('test', frame_blank2)
    key = cv2.waitKey(1)
    cv2.imshow('test2', frame_blurred)

cv2.destroyAllWindows()
video_capture.release()
