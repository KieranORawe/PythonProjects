import cv2
import time

camera = cv2.VideoCapture(0)
print("ready")
time.sleep(1)
_,base = camera.read()
print("captured")
time.sleep(5)
print("ready")
time.sleep(1)
_,cap = camera.read()
print("captured")

cv2.imshow("q",base)
time.sleep(1)
cv2.imshow("w",cap)
