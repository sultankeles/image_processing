import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

# Blurring
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off")
plt.title("Original")
plt.show()


# Average Blurring
dst2 = cv2.blur(img, ksize = (3, 3))

plt.figure()
plt.imshow(dst2)
plt.axis("off")
plt.title("Average Blur")
plt.show()


# Gaussian Blurring
gb = cv2.GaussianBlur(img, ksize = (3, 3), sigmaX = 7)

plt.figure()
plt.imshow(gb)
plt.axis("off")
plt.title("Gaussian Blur")
plt.show()


# Median Blurring
mb = cv2.medianBlur(img, ksize = 3)

plt.figure()
plt.imshow(mb)
plt.axis("off")
plt.title("Median Blur")
plt.show()


def gaussianNoise(image):
    row, col, ch = image.shape    # ch: whether the image is rgb(3) or grayscale(1)
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    return noisy

# import and normalization
img = cv2.imread("NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255

gn = gaussianNoise(img)

plt.figure()
plt.imshow(gn)
plt.axis("off")
plt.title("Gauss Noisy")
plt.show()

# Gauss Blurring
gb2 = cv2.GaussianBlur(gn, ksize = (3, 3), sigmaX = 7)

plt.figure()
plt.imshow(gb2)
plt.axis("off")
plt.title("Gaussian Noise w/Gaussian Blur")
plt.show()


def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
  
    return noisy

sp_img = saltPepperNoise(img)

plt.figure()
plt.imshow(sp_img)
plt.axis("off")
plt.title("SP Img")
plt.show()


# Median Blurring
mb2 = cv2.medianBlur(sp_img.astype(np.float32), ksize = 3)

plt.figure()
plt.imshow(mb2)
plt.axis("off")
plt.title("Salt Pepper Noise w/Median Blur")
plt.show()
