import cv2
import numpy as np

# create image
img = np.zeros((512, 512, 3), np.uint8)   # black image

print(img. shape)

cv2.imshow("Black", img)

# line
# (image, starting point, endpoint, color, thickness);
cv2.line(img, (0,0), (512, 512), (0, 255, 0), 3)   # BGR = (0, 255, 0) -> for green
cv2.imshow("Line", img)

# rectangle
cv2.rectangle(img, (0, 0), (256, 256), (255, 0, 0), cv2.FILLED)
cv2.imshow("Rectangle", img)

# circle
cv2.circle(img, (300, 300), 45, (0, 0, 255))
# cv2.circle(img, (300, 300), 45, (0, 0, 255), cv2.FILLED))
cv2.imshow("Circle", img)

# text
# (image, starting point, font, font thickness, color(white));
cv2.putText(img, "Added Text", (350, 350), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.imshow("Text", img)