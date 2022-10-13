import cv2
import numpy as np

# image = np.arange(0, 256).astype(np.uint8)
# image = image[np.newaxis, :]
# image = np.repeat(image, 255, axis=0)
#
# print(image.shape)
# print(type(image))
# print(image.dtype)
########################################################################################################################
PATH = '..//Images_and_videos//albert-einstein_gray.jpg'

image = cv2.imread(PATH)

cv2.imshow('test', image)
cv2.waitKey(0)
cv2.destroyAllWindows()