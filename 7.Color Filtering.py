import numpy as np
import cv2
img = cv2.imread('bookpage.jpg')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    #Hue, Saturation, Value
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ##Play with the HSV values to filter out
    lower_red= np.array([60,0,0])
    upper_red= np.array([160,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    ##Blurring
    #kernel = np.ones((15,15), np.float32)/225
    #smoothed = cv2.filter2D(res,-1,kernel)
    #cv2.imshow('smoothed', smoothed)

    ##Gaussian Blur
    #blur = cv2.GaussianBlur(res, (15,15), 0)
    #cv2.imshow('blur', blur)

    ##Median BLur
    #median = cv2.medianBlur(res, 15)
    #cv2.imshow('median', median)

    ##Bilateral Blur
    #bilateral = cv2.bilateralFilter(res, 15, 75, 75)
    #cv2.imshow('bilateral', bilateral)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break



cv2.destroyAllWindows()
cap.release()