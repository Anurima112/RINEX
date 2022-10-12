#STEP 1: IMPORT LIBRARY
import cv2 as cv
import numpy as np

#STEP 2: IMPORT IMAGE
img=cv.imread('C://Users//HP//Desktop//RINEX//girl.jpg',)

#STEP 3: CONVERT THE IMAGE INTO GRAYSCALE
gray_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#STEP 4: CONTRAST IMAGE
contrast_img=cv.addWeighted(img,2.5,np.zeros(img.shape,img.dtype),0,0)

#STEP 5: BINARY CONVERSION
ret,gray=cv.threshold(img,127,256,cv.THRESH_BINARY)

#STEP 6: DISPLAY THE IMAGE
cv.imshow("ORIGINAL_IMAGE",img) #original image
cv.imshow("GRAY_IMAGE",gray_img)#convert into gray image
cv.imshow("CONTRAST_IMAGE",contrast_img)#contrast image
cv.imshow("BINARY_IMAGE",gray)#convert into binary image
cv.waitKey()
cv.destroyAllWindows()
