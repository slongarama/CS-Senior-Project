# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
from PIL import Image
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", help="name to save image as", default="test.png")
args = vars(ap.parse_args())
path = args["path"]

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)

# add delay if necessary
time.sleep(5)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image on screen and wait for a keypress
cv2.imwrite(path, image)

