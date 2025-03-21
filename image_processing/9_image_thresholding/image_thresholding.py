# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 20:54:38 2025

@author: Sultankeles17
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("img1.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # color tones in gray scale

plt.figure()
plt.imshow(img, cmap = "gray")  # changed color map
plt.axis("off")
plt.show()

# threshold
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 250, type = cv2.THRESH_BINARY)  # if thresh value > 60, they turn 0  /  gray scale: 0(black) - 250(white)
# _, thresh_img = cv2.threshold(img, thresh = 60, maxval = 250, type = cv2.THRESH_BINARY_INV)

plt.figure()
plt.imshow(thresh_img, cmap = "gray")
plt.axis("off")
plt.show()

# adaptive threshold
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8) # c constant: 8

plt.figure()
plt.imshow(thresh_img2, cmap = "gray")  # changed color map
plt.axis("off")
plt.show()