import cv2
import time

camera = cv2.VideoCapture(0)

while(1):
    _,cap = camera.read()
    cv2.imshow('res',cap)
    cv2.waitKey(1)
