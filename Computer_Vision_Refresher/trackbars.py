import cv2
import numpy as np
import matplotlib.pyplot as plt


# Define a display convenience function
def show(img, size=(5, 5)):
    plt.figure(figsize=size)
    if len(img.shape) <= 2:
        plt.imshow(img, cmap='gray')
    elif img.shape[2] == 3:
        plt.imshow(img[:, :, ::-1])
    elif img.shape[2] > 3:
        plt.imshow(img[:, :, [2, 1, 0, 3]])
    else:
        print("Check the shape of the image.")
    plt.show()

