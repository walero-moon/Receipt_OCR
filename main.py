import cv2
img_file = "./receipt.jpg"
img = cv2.imread(img_file)
cv2.imshow("Original Image", img)
cv2.waitKey(10000)