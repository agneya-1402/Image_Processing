from PIL import Image, ImageFilter 
	

img1 = Image.open("ImageProcessing/SpatialDomainFilters/blur_img.jpg") 
	
# applying the unsharp mask 
img2 = img1.filter(ImageFilter.UnsharpMask(radius = 10, percent = 100, threshold = 0)) 
	
img1.show()    
img2.show()
