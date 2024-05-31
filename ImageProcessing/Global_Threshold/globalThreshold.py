import cv2 
import numpy as np 

image1 = cv2.imread('ImageProcessing/Global_Threshold/img1.jpeg') 

# convert to grayscale 
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY) 

# threshold value
# all pixels value above 'threshold_value' will be set to 255 
threshold_value=120
ret, thresh1 = cv2.threshold(img, threshold_value, 255, cv2.THRESH_BINARY) 

cv2.imshow('Original Image', image1)
cv2.imshow('Binary Threshold', thresh1) 


if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 
