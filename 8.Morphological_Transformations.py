import numpy as np
import cv2
img = cv2.imread('bookpage.jpg')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #Hue, Saturation, Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ##Play with the HSV values to filter out
    lower_red= np.array([60,90,0])
    upper_red= np.array([100,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    ##Erosion
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)
    cv2.imshow('erosion', erosion)

    ##Dilation
    dilations = cv2.dilate(mask, kernel, iterations=1)
    cv2.imshow('dilations', dilations)

    ##Opening and Closing    ##False positives and Negatives
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cv2.imshow('opening',opening)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('closing', closing)



    cv2.imshow('frame', frame)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break



cv2.destroyAllWindows()
cap.release()