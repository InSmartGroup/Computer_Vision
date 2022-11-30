import cv2
import numpy as np
import matplotlib.pyplot as plt

# # Black image histogram
# image = np.zeros((200, 200, 1))
#
# image_flat = image.flatten()
#
# plt.figure(figsize=(10, 4))
# plt.subplot(121)
# plt.imshow(image, cmap='gray')
# plt.title("Black square image")
# plt.subplot(122)
# plt.hist(image_flat, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.title("Black square image histogram")
# plt.show()


# # Binary image histogram
# image = cv2.imread('..//Images_and_videos//checkerboard_18x18.png', 0)
#
# image_flat = image.ravel()
#
# plt.figure(figsize=(12, 4))
# plt.subplot(131)
# plt.title('Binary image')
# plt.imshow(image, cmap='gray')
# plt.subplot(132)
# plt.title("Binary image histogram, 3 bins")
# plt.hist(image_flat, bins=3, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.subplot(133)
# plt.title("Binary image histogram, 10 bins")
# plt.hist(image_flat, bins=10, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.show()


# # Binary image histogram
# image = cv2.imread("..//Images_and_videos//MNIST_3_18x18.png", 0)
#
# image_flat = image.flatten()
#
# plt.figure(figsize=(12, 4))
# plt.subplot(131)
# plt.title('Binary image')
# plt.imshow(image, cmap='gray')
# plt.subplot(132)
# plt.title("Binary image histogram, 10 bins")
# plt.hist(image_flat, bins=10, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.subplot(133)
# plt.title("Binary image histogram, 100 bins")
# plt.hist(image_flat, bins=100, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.show()


# # Grayscale image histogram
# image = cv2.imread('..//Images_and_videos//Apollo-8-Launch.jpg', 0)
#
# image_flat = image.flatten()
#
# plt.figure(figsize=(12, 4))
# plt.subplot(131)
# plt.title('Grayscale image')
# plt.imshow(image, cmap='gray')
# plt.subplot(132)
# plt.title("Grayscale image histogram, 50 bins")
# plt.hist(image_flat, bins=50, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.subplot(133)
# plt.title("Grayscale image histogram, 256 bins")
# plt.hist(image_flat, bins=256, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.show()


# # 'plt.hist()' and 'cv2.calcHist()' histogram comparison
# image = cv2.imread('..//Images_and_videos//Apollo-8-Launch.jpg', 0)
#
# image_flat = image.flatten()
#
# hist = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
#
# plt.figure(figsize=(12, 4))
# plt.subplot(131)
# plt.title('Original image')
# plt.imshow(image, cmap='gray')
# plt.subplot(132)
# plt.title('plt.hist()')
# plt.hist(image_flat, bins=256, range=[0, 256])
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.subplot(133)
# plt.title('cv2.calcHist()')
# plt.plot(hist)
# plt.ylabel('Number of pixels')
# plt.xlabel('Pixel intensity')
# plt.show()


# # 'cv2.calcHist()' with color images
# image = cv2.imread('..//Images_and_videos//flowers.jpeg', 1)
#
# hist_b = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 255])
# hist_g = cv2.calcHist([image], channels=[1], mask=None, histSize=[256], ranges=[0, 255])
# hist_r = cv2.calcHist([image], channels=[2], mask=None, histSize=[256], ranges=[0, 255])
#
# plt.figure(figsize=(14, 7))
# plt.subplot(221)
# plt.title("Original image")
# plt.imshow(image[:, :, ::-1])
# plt.subplot(222)
# plt.title('cv2.calcHist, Blue channel')
# plt.plot(hist_b, 'blue')
# plt.subplot(223)
# plt.title("cv2.calcHist, Green channel")
# plt.plot(hist_g, 'green')
# plt.subplot(224)
# plt.title('cv2.calcHist, Red channel')
# plt.plot(hist_r, 'red')
# plt.show()


# # Color histograms
# image = cv2.imread('..//Images_and_videos//Emerald_Lakes_New_Zealand.jpg', 1)
#
# hist_b = cv2.calcHist([image], [0], None, [255], [0, 256])
# hist_g = cv2.calcHist([image], channels=[1], mask=None, histSize=[255], ranges=[0, 256])
# hist_r = cv2.calcHist([image], [2], None, [255], [0, 256])
#
# plt.figure(figsize=(12, 4))
# plt.subplot(121)
# plt.title('Original image')
# plt.imshow(image[:, :, [2, 1, 0]])
# plt.subplot(122)
# plt.title('Color channels histogram')
# plt.plot(hist_b, 'blue')
# plt.plot(hist_g, 'green')
# plt.plot(hist_r, 'red')
# plt.ylim((0, 400000))
# plt.xlim((0, 256))
# plt.show()


# # Grayscale images histogram equalization
# image = cv2.imread('..//Images_and_videos//parrot.jpg', 0)
# hist = image.flatten()
#
# image_eq = cv2.equalizeHist(image)
# hist_eq = image_eq.flatten()
#
# plt.figure(figsize=(14, 7))
# plt.subplot(221)
# plt.title('Source image')
# plt.imshow(image, cmap='gray')
# plt.subplot(222)
# plt.title('Source image histogram')
# plt.hist(hist, bins=256, range=[0, 256])
# plt.subplot(223)
# plt.title('Equalized image')
# plt.imshow(image_eq, cmap='gray')
# plt.subplot(224)
# plt.title('EQ image histogram')
# plt.hist(hist_eq, bins=256, range=[0, 256])
# plt.show()


# # Color images histogram equalization
# image = cv2.imread('..//Images_and_videos//parrot.jpg', 1)
#
# image_eq = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# image_eq[:, :, 2] = cv2.equalizeHist(image_eq[:, :, 2])
# image_eq = cv2.cvtColor(image_eq, cv2.COLOR_HSV2BGR)
#
# hist = image.flatten()
# hist_eq = image_eq.flatten()
#
# plt.figure(figsize=(14, 7))
# plt.subplot(221)
# plt.title('Original image')
# plt.imshow(image[:, :, ::-1])
# plt.subplot(222)
# plt.title('Equalized histogram')
# plt.imshow(image_eq[:, :, ::-1])
# plt.subplot(223)
# plt.title('Source image histogram')
# plt.hist(hist, bins=256, range=[0, 256])
# plt.subplot(224)
# plt.title('EQ image histogram')
# plt.hist(hist_eq, bins=256, range=[0, 256])
# plt.show()
