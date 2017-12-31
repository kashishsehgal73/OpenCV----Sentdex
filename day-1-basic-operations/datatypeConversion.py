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

# Read image
source = cv2.imread("sample.jpg",1)

scalingFactor = 1/255.0

# Convert unsigned int to float
source = np.float32(source)
source = source * scalingFactor

#Convert back to unsigned int
source = source * (1.0/scalingFactor)
source = np.uint8(source)

print ("Nothing to Display")
