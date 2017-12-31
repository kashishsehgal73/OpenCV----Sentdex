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

# Read the file "image.jpg".
# This file "image.jpg" should be in the project folder.
# Else provide full path: "D:/images/image.jpg"
imageName = "sample.jpg"

# LOAD image
image = cv2.imread(imageName, cv2.IMREAD_COLOR)

if image is None:  # Check for invalid input
    print("Could not open or find the image")

# convert color image to gray
grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# DISPLAY image
# Create a window for display.
cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE)
cv2.namedWindow("gray image", cv2.WINDOW_NORMAL)

# Show our image inside it.
cv2.imshow("image", image)
cv2.imshow("gray image", grayImage)
# Both images are displayed but gray image on top of original image
# Move gray image window to see original image

# SAVE image
cv2.imwrite("result.jpg", image)  # it will store the image with name "result.jpg"
cv2.imwrite("result_gray.jpg", grayImage)  # it will store the gray image with name "result_gray.jpg"

cv2.waitKey(0)  # Wait for a keystroke in the window

cv2.destroyAllWindows()
