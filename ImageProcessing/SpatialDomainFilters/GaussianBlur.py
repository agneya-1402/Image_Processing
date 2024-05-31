import cv2 
import numpy as np 
  
image = cv2.imread('ImageProcessing/SpatialDomainFilters/edgeDetect.jpg') 
  
# Applying the filter 
gaussian = cv2.GaussianBlur(image, (9, 9), 0) 

cv2.imshow('Original', image) 
cv2.imshow('Gaussian blur', gaussian) 
  
cv2.waitKey() 
cv2.destroyAllWindows() 