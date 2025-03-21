import cv2
import matplotlib.pyplot as plt

# blending
img1 = cv2.imread("img1.jpg")   # When loading Opencv colors, it loads them in BGR scale by default, not RGB.
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.imread("img2.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)


img1 = cv2.resize(img1, (1000, 600))
print(img1.shape)

img2 = cv2.resize(img2, (1000, 600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# blended image = alpha * img1 + beta * img2
blended_img = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0)

plt.figure()
plt.imshow(blended_img)