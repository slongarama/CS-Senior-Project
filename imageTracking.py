from picamera import PiCamera
from picamera.array import PiRGBArray
import time
from captureAndBlur import *
import cv2

# Image resolution of captured frames
IMG_SIZE = 256

# Size of the surrounding region utilized when appying a Gaussian blur on frames
BLUR_REGION = 5

# Define camera settings and specify variable to store frame
camera = PiCamera()
camera.resolution = (IMG_SIZE, IMG_SIZE)
rgbFrame = PiRGBArray(camera, size = camera.resolution)

time.sleep(0.1)

frame1 = captureProcessFrame(camera, rgbFrame, BLUR_REGION)
#cv2.imshow("blurred", frame1)
#cv2.waitKey(0)
cv2.imwrite("blurred.png", frame1)
