import numpy as np
import cv2

img = cv2.imread('watch.png', cv2.IMREAD_COLOR)

#px = img[55,55] ##reference particular pixel
#print(px) #gives color value
#px = [0,0,0]# Change color Value
#print(px)


##Accesing part of Image
roi = img[500:1000,500:1000]
roi = [0,0,0]

##Coloring particular part of image
img[100:150,100:150] = [0,0,0]

##WE CAN ALSO COPY PARTS OF IMAGE AND PASTE ANYWHERE USING ARRAYS
img[0:500,0:500] = roi



cv2.imshow('roi',img)
cv2.waitKey(0)
cv2.destroyAllWindows()