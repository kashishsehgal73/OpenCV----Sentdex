import numpy as np
import cv2

img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')

##add = img1+img2            #Superimposes Images
##add = cv2.add(img1,img2)    #Adds Color Intesity Values
##weighted = cv2.addWeighted(img1 ,0.6, img2, 0.4, 0) ##Last parameter is gamma  ## Different Weights to images
#cv2.imshow('add',weighted)

img2 = cv2.imread('mainlogo.png')
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

#Creating mask
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
## Less than 220 to 0 , more than 220 to 255
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV) ##min val, max val,Binary Threshold Inverted
#cv2.imshow('mask',mask)

mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_and(roi, roi, mask= mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst
#cv2.imshow('img2gray', img2gray)
#cv2.imshow('mask_inv', mask_inv)
#cv2.imshow('img1_bg', img1_bg)
#cv2.imshow('img2_fg', img2_fg)
cv2.imshow('rest', img1)


cv2.waitKey(0)
cv2.destroyAllWindows()