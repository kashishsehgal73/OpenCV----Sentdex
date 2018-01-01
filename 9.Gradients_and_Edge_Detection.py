import numpy as np
import cv2
img = cv2.imread('bookpage.jpg')

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame, cv2.CV_64F)

    cv2.imshow('laplacian', laplacian)

    ## X - Gradient
    #sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    #cv2.imshow('sobelx', sobelx)

    ## Y - Gradient
    #sobely = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    #cv2.imshow('sobely', sobely)

    ##Canny Edge Detection
    edges = cv2.Canny(frame, 100, 200)  ##Experiment and change these values
    cv2.imshow('edges', edges)


    cv2.imshow('frame', frame)
    k = cv2.waitKey(5) & 0xFF
    if k==27:
        break



cv2.destroyAllWindows()
cap.release()