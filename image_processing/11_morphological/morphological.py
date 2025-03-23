import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("img.jpg", 0)

plt.figure()
plt.imshow(img, cmap = "gray")
plt.axis("off")
plt.title("Original Image")


# Erosion
kernel = np.ones((5, 5))
result = cv2.erode(img, kernel, iterations = 1)

plt.figure()
plt.imshow(result, cmap = "gray")
plt.axis("off")
plt.title("Erosion")

# Dilation
result2 = cv2.dilate(img, kernel, iterations = 1)

plt.figure()
plt.imshow(result2, cmap = "gray")
plt.axis("off")
plt.title("Dilation")

# White Noise
wht_noise = np.random.randint(0,2, size = img.shape[:2])
wht_noise = wht_noise * 255

noisy_img = wht_noise + img

plt.figure()
plt.imshow(noisy_img, cmap = "gray")
plt.axis("off")
plt.title("Added White Noise")

# Opening
opening = cv2.morphologyEx(noisy_img.astype(np.float32), cv2.MORPH_OPEN, kernel)

plt.figure()
plt.imshow(opening, cmap = "gray")
plt.axis("off")
plt.title("Opening")

# Black Noise
black_noise = np.random.randint(0,2, size = img.shape[:2])
black_noise = black_noise * -255

black_noise_img = black_noise + img
black_noise_img[black_noise_img <= -245] = 0

plt.figure()
plt.imshow(black_noise_img, cmap = "gray")
plt.axis("off")
plt.title("Black Noise Image")

# Closing
closing = cv2.morphologyEx(black_noise_img.astype(np.float32), cv2.MORPH_CLOSE, kernel)

plt.figure()
plt.imshow(closing, cmap = "gray")
plt.axis("off")
plt.title("Closing")


# Gradiant
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

plt.figure()
plt.imshow(gradient, cmap = "gray")
plt.axis("off")
plt.title("Gradient")