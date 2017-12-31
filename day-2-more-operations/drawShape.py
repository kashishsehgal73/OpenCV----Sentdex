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

image = cv2.imread('mark.jpg')

# Draw a line
imageLine = image.copy()
cv2.line(imageLine, (322, 179), (400, 183), (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("imageLine", imageLine)
cv2.imwrite("imageLine.jpg", imageLine)

# Draw a circle
imageCircle = image.copy()
cv2.circle(imageCircle, (350, 200), 150, (0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("imageCircle", imageCircle)
cv2.imwrite("imageCircle.jpg", imageCircle)

# Draw an ellipse
# IMP Note: Ellipse Centers and Axis lengths must be integers
imageEllipse = image.copy()
cv2.ellipse(imageEllipse, (360, 200), (100, 170), 45, 0, 360, (255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
cv2.ellipse(imageEllipse, (360, 200), (100, 170), 135, 0, 360, (0, 0, 255), thickness=2, lineType=cv2.LINE_AA)
cv2.imshow("ellipse", imageEllipse)
cv2.imwrite("imageEllipse.jpg", imageEllipse)

# Draw a rectangle (thickness is a positive integer)
imageRectangle = image.copy()
cv2.rectangle(imageRectangle, (208, 55), (450, 355), (0, 255, 0), thickness=2, lineType=cv2.LINE_8)
cv2.imshow("rectangle", imageRectangle)
cv2.imwrite("imageRectangle.jpg", imageRectangle)

# Put text into image
imageText = image.copy()
cv2.putText(imageText, "Mark Zuckerberg", (205, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("text", imageText)
cv2.imwrite("imageText.jpg", imageText)

cv2.waitKey(0)
cv2.destroyAllWindows()