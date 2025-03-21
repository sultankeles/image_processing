import cv2
import numpy as np

img = cv2.imread("card.png")
cv2.imshow("Original", img)

width = 400
height = 500

# Create point
pts1 = np.float32([[203, 1], [1, 474], [540, 145], [340, 618]])
pts2 = np.float32([[0, 0], [0, height], [width, 0], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# final converted image
imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Converted Image", imgOutput)