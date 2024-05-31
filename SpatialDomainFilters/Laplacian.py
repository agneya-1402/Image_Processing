import cv2
import matplotlib.pyplot as plt

image = cv2.imread("ImageProcessing/SpatialDomainFilters/edgeDetect.jpg", cv2.IMREAD_COLOR)

# adding gaussian blur
image = cv2.GaussianBlur(image, (9, 9), 0)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# applying filter
filtered_image = cv2.Laplacian(image_gray, cv2.CV_16S, ksize=1)

# Plotting the original and filtered images
plt.figure(figsize=(10, 5))

# original img
plt.subplot(121)
plt.imshow(image, cmap='gray')
plt.title('Original Image')

#filtered img
plt.subplot(122)
plt.imshow(filtered_image, cmap='gray')
plt.title('LoG Filtered Image')

plt.show()