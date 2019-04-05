import cv2

img = cv2.imread("demo.jpg")

height, width = img.shape[0:2]

rotationMatrix = cv2.getRotationMatrix2D((width/2, height/2), 90, .5)

rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))

cv2.imshow('Rotated Image', rotatedImage)

cv2.waitKey(0)
