import numpy as np
import cv2
img = cv2.imread('watch.png', cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,0,0), 15)#BGR #last argument is line_width
cv2.rectangle(img, (15,25), (400,400), (0,0,255), 5)
cv2.circle(img, (100,63), 55, (0,255,0), -1) # -1 line_width fills the circle

pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,0,0), 3)# If you wanna connect Final Points

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV Tuts', (800,780), font, 5, (20,20,20), 5, cv2.LINE_AA) ## image,text,starting point, font, fontsize, color, Thickness, AntiAliasing

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()