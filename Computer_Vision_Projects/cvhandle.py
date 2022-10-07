"""
This script contains useful functions to works with the OpenCV library.
It is being constantly revised and updated alongside with the workflow.
"""
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import cvzone


def img_show(name, image, scale_x=None, scale_y=None):
    """Syntax: (name, image, scale_x, scale_y)
    name is the desired name displayed in the window
    image is the source input image
    scale_x is the image width scaling factor
    scale_y is the image height scaling factor"""

    if scale_x is not None and scale_y is not None:
        image = cv2.resize(image, None, fx=scale_x, fy=scale_y)

    cv2.imshow(name, image)
    key = cv2.waitKey(0)

    if key == 27 or key == ord('q') or key == ord('Q'):
        cv2.destroyAllWindows()


def img_convert(image, in_color=None, out_color=None):
    """Syntax: (image, in_color, out_color)
    image is the source input image
    in_color is the color space of the input image
    out_color is the desired color space of the output image"""

    if in_color == 'bgr' and out_color == 'rgb':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    elif in_color == 'bgr' and out_color == 'rgba':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

    elif in_color == 'bgr' and out_color == 'bgra':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)

    elif in_color == 'bgra' and out_color == 'rgb':
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)

    elif in_color == 'bgra' and out_color == 'rgba':
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2RGBA)

    elif in_color == 'rgb' and out_color == 'bgr':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    elif in_color == 'rgb' and out_color == 'rgba':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)

    elif in_color == 'rgb' and out_color == 'bgra':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGRA)

    elif in_color == 'rgba' and out_color == 'bgr':
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)

    elif in_color == 'rgba' and out_color == 'bgra':
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGRA)

    elif in_color == 'hsv' and out_color == 'rgb':
        image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)

    elif in_color == 'hsv' and out_color == 'gray':
        image = cv2.cvtColor(image, cv2.COLOR_HSV2RGB)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    elif in_color == 'hsv' and out_color == 'bgr':
        image = cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

    elif in_color == 'rgb' and out_color == 'hsv':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

    elif in_color == 'bgr' and out_color == 'hsv':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    elif in_color == 'bgr' and out_color == 'gray':
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    elif in_color == 'bgra' and out_color == 'gray':
        image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)

    elif in_color == 'rgb' and out_color == 'gray':
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

    elif in_color == 'rgba' and out_color == 'gray':
        image = cv2.cvtColor(image, cv2.COLOR_RGBA2GRAY)

    elif in_color == 'gray' and out_color == 'rgb':
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)

    elif in_color == 'gray' and out_color == 'rgba':
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGBA)

    elif in_color == 'gray' and out_color == 'bgr':
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    elif in_color == 'gray' and out_color == 'bgra':
        image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGRA)

    return image


def img_transform(image, operation=None, param1=None, param2=None, param3=None, param4=None):
    """Syntax: (image, operation, param1, param2, param3, param4)
    image is the source input image
    operation is the desired operation name
    Available operations: 'threshold', 'adaptive_threshold', 'resize', 'flip'
    Pass each argument in the same order as if using the needed OpenCV function"""

    if operation == 'threshold' and param3 == 'binary':
        retval, image = cv2.threshold(image, param1, param2, cv2.THRESH_BINARY)

    elif operation == 'threshold' and param3 == 'binary_inv':
        retval, image = cv2.threshold(image, param1, param2, cv2.THRESH_BINARY_INV)

    elif operation == 'adaptive_threshold' and param2 == 'binary':
        image = cv2.adaptiveThreshold(image, param1, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY, param3, param4)

    elif operation == 'adaptive_threshold' and param2 == 'binary_inv':
        image = cv2.adaptiveThreshold(image, param1, cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY_INV, param3, param4)

    elif operation == 'resize':
        image = cv2.resize(image, None, fx=param1, fy=param2)

    elif operation == 'flip':
        image = cv2.flip(image, param1)

    return image


def img_getinfo(image):
    """Prints out general information about the input image"""

    print(f"Image width: {image.shape[1]}")
    print(f"Image height: {image.shape[0]}")

    if len(image.shape) >= 3:
        print(f"Color channels: {image.shape[2]}")
    elif len(image.shape) < 3:
        print("The image is binary.")

    print(f"Image data type: {image.dtype}")
    print()


def img_bitwise(image1, image2, operation=None, mask=None):
    """Syntax: (image1, image2, operation, mask)
    image1 is the first input image
    image2 is the second input image
    operation is the desired operation name
    mask is the image mask
    Available operations: 'and', 'or', 'not', 'xor'"""

    if operation == 'and':
        result = cv2.bitwise_and(image1, image2, mask=mask)

    elif operation == 'or':
        result = cv2.bitwise_or(image1, image2, mask=mask)

    elif operation == 'not':
        result = cv2.bitwise_not(image1, image2, mask=mask)

    elif operation == 'xor':
        result = cv2.bitwise_xor(image1, image2, mask=mask)

    return result


def img_morph(image, operation=None, param1=None, param2=None, param3=None):
    """Syntax: (image, operation, param1, param2, param3)"""

    pass
