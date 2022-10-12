import cv2

PATH = '..//Images_and_videos//iloveyouticket.jpg'

image = cv2.imread(PATH)


def img2transparent(source, min_thresh=125):
    image_gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    retval, mask = cv2.threshold(image_gray, min_thresh, 255, cv2.THRESH_BINARY_INV)
    blue, green, red = cv2.split(source)
    blue = cv2.bitwise_and(blue, mask)
    green = cv2.bitwise_and(green, mask)
    red = cv2.bitwise_and(red, mask)
    result = cv2.merge((blue, green, red, mask))
    return result

image = img2transparent(image, min_thresh=150)
cv2.imshow('image', image)
cv2.imwrite('test.png', image)
key = cv2.waitKey(0)
if key == 27 or key == ord('q'):
    cv2.destroyAllWindows()
