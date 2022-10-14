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


def img_operation(image, operation=None, param1=None, param2=None, param3=None, param4=None):
    """Syntax: (image, operation, param1, param2, param3, param4)
    image is the source input image
    operation is the desired operation name
    Available operations: 'threshold', 'adaptive_threshold', 'median_blur', 'gaussian_blur' 'resize', 'flip'
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

    elif operation == 'median_blur':
        image = cv2.medianBlur(image, param1)

    elif operation == 'gaussian_blur':
        image = cv2.GaussianBlur(image, param1, param2, param3)

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
        print(f"Channel 1 maximum pixel intensity: {image[:, :, 0].max()}")
        print(f"Channel 2 maximum pixel intensity: {image[:, :, 1].max()}")
        print(f"Channel 3 maximum pixel intensity: {image[:, :, 2].max()}")
    elif len(image.shape) < 3:
        print("Binary image")
        print(f"Maximum pixel intensity: {image.max()}")

    print(f"Image data type: {image.dtype}")
    print()


def img_gray3channel(image):
    """Apply this function to turn a binary grayscale image into a 3-channel image."""
    image = cv2.merge((image, image, image))
    return image


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


def img_edges(image, operation=None, param1=None, param2=None, param3=None, param4=None):
    """Syntax: (image, operation, param1, param2, param3, param4)
    image is the source input image
    operation is the desired operation name
    Available operations: 'canny', 'sobel_x', 'sobel_y', 'sobel'
    It's also possible to pass 'normalize' as a 3rd argument when using all Sobel functions
    Pass each argument in the same order as if using the needed OpenCV function"""
    if operation == 'canny':
        image = cv2.Canny(image, threshold1=param1, threshold2=param2,
                          edges=param3, apertureSize=param4)

    elif operation == 'sobel_x':
        image = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=param1)

        if param2 == 'normalize':
            image = image - image.min()
            image = image / image.max()
            image = (image * 255).astype(np.uint8)

    elif operation == 'sobel_y':
        image = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=param1)

        if param2 == 'normalize':
            image = image - image.min()
            image = image / image.max()
            image = (image * 255).astype(np.uint8)

    elif operation == 'sobel':
        image = cv2.Sobel(image, ddepth=cv2.CV_32F, dx=1, dy=1, ksize=param1)

        if param2 == 'normalize':
            image = image - image.min()
            image = image / image.max()
            image = (image * 255).astype(np.uint8)

    return image


def img2transparent(source, min_thresh=125):
    """Converts a 3-channel image to 4-channel transparent.
    Syntax: (source, min_thresh)
    source is the source input 3-channel image
    min_thresh is the minimum threshold value"""
    image_gray = cv2.cvtColor(source, cv2.COLOR_BGR2GRAY)
    retval, mask = cv2.threshold(image_gray, min_thresh, 255, cv2.THRESH_BINARY_INV)
    blue, green, red = cv2.split(source)
    blue = cv2.bitwise_and(blue, mask)
    green = cv2.bitwise_and(green, mask)
    red = cv2.bitwise_and(red, mask)
    result = cv2.merge((blue, green, red, mask))
    return result


def img_draw_grid(source, grid_shape=(5, 5), color=(0, 255, 0), thickness=1):
    """Syntax: (source, grid_shape, color, thickness)
    source is the source input image
    grid_shape is the desired shape of a grid
    color is the desired color of a grid
    thickness is the desired grid line thickness
    Note: pass white color for binary images
    Note: this function changes the input image"""
    if len(source.shape) > 2:
        height, width, _ = source.shape
    else:
        height, width = source.shape

    rows, columns = grid_shape
    dy, dx = int(height / rows), int(width / columns)

    # Vertical lines
    for x in np.linspace(start=dx, stop=width - dx, num=columns - 1):
        x = int(round(x))
        cv2.line(source, (x, 0), (x, height), color=color, thickness=thickness)

    # Horizontal lines
    for y in np.linspace(start=dy, stop=height - dy, num=rows - 1):
        y = int(round(y))
        cv2.line(source, (0, y), (width, y), color=color, thickness=thickness)

    return source


def img_morph(image, operation=None, param1=None, param2=None, param3=None):
    """Syntax: (image, operation, param1, param2, param3)"""

    pass


def img_kernel(operation=None, ksize=None):
    """Syntax: (operation, ksize)
    operation is the operation name for which the kernel should be used
    ksize is the desired size of a kernel
    Available operations: 'sharpening', 'sepia' or 'vintage'
    Available kernel sizes: 'small', 'medium', 'large'"""
    if operation == 'sharpening' and ksize == 'small':
        kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],
                           [0, -1, 0]])

    elif operation == 'sharpening' and ksize == 'medium':
        kernel = np.array([[0, -2, 0],
                           [-2, 9, -2],
                           [0, -2, 0]])

    elif operation == 'sharpening' and ksize == 'large':
        kernel = np.array([[0, -4, 0],
                           [-4, 17, -4],
                           [0, -4, 0]])

    elif operation == 'sepia' or operation == 'vintage':
        kernel = np.matrix([[0.393, 0.769, 0.189],
                            [0.349, 0.686, 0.168],
                            [0.272, 0.534, 0.131]])

    return kernel
