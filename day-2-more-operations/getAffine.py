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
import numpy as np 

# Input triangle
inp = np.float32([[50, 50], [100, 100], [200, 150]])
# Output triangle
output = np.float32([[72, 51], [142, 101], [272, 136]])
# Another output triangle
output2 = np.float32([[77, 76], [152, 151], [287, 236]])

# Get the tranformation matrices
warpMat = cv2.getAffineTransform(inp, output)
warpMat2 = cv2.getAffineTransform(inp, output2)

# Display the matrices
print ("Warp Matrix 1 : \n {} \n".format(warpMat))
print ("Warp Matrix 2 : \n {} \n".format(warpMat2))