import cv2
 
img = cv2.imread("demo.jpg")

newImg = cv2.resize(img, (0,0), fx=0.75, fy=0.75)
 
cv2.imshow('Resized Image', newImg)
 
cv2.waitKey(0)

