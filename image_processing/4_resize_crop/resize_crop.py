import cv2

img = cv2.imread("Lenna.png", 0)    # 0: black&white
print("Image Size: ", img.shape)

cv2.imshow("Original", img)

# resize
resized_img = cv2.resize(img, (800, 800))
print("Resized Img Shape: ", resized_img.shape)
cv2.imshow("Resized Img", resized_img)

# crop
cropped_img = img[:200, 0:300]  # first 200 pixsels on the x-axis(height) and last 300 pixsels on the y-axis(width)
cv2.imshow("Cropped Image", cropped_img)