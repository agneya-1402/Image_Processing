import numpy as np
import cv2 
from matplotlib import pyplot as plt
 
img = cv2.imread('ImageProcessing/HistogramEqualisation/img2.jpeg', cv2.IMREAD_GRAYSCALE)

#Equalisating the histogram using equalizeHist function
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #side by side imgs

cv2.imshow('Original img',img)
cv2.imshow('Output img',res)

if cv2.waitKey(0) & 0xff == 27: 
	cv2.destroyAllWindows() 