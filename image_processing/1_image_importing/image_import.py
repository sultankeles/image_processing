import cv2

# image importing
img = cv2.imread("messi5.jpg", 0)

# visualization
cv2.imshow("first picture", img)

k = cv2.waitKey(0) & 0xFF

if k == 27: # wsc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("messi_gray.png", img)
    cv2.destroyAllWindows()