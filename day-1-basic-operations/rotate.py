# Copyright 2017 BIG VISION LLC ALL RIGHTS RESERVED
# 
# This code is made available to the students of 
# the online course titled "OpenCV for Beginners" 
# by Satya Mallick for personal non-commercial use. 
#
# Sharing this code is strictly prohibited without written
# permission from Big Vision LLC. 
#
# For licensing and other inquiries, please email 
# spmallick@bigvisionllc.com 
#

import cv2

source = cv2.imread("sample.jpg",1)

# Getting the dimesnions of the image
dim = source.shape

rotationAngle = -30
scaleFactor = 1

# Rotating the image by 90 degrees about the center
# dim[0] stores the no of rows and dim[1] no of columns
rotationMatrix = cv2.getRotationMatrix2D((dim[1]/2,dim[0]/2),rotationAngle, scaleFactor)
print(rotationMatrix)

result = cv2.warpAffine(source, rotationMatrix, (dim[1],dim[0]))

cv2.imshow("Original", source)
cv2.imshow("Rotated Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

