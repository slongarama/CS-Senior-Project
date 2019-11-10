# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(0.1)

print('STARTING PHOTOS')
time.sleep(2)
print('------------------------------')

# grab an image from the camera
for i in range(15):
    print('TAKING PHOTO ', i)
    time.sleep(3)
    camera.capture('images/Pi3_Calibration/image{0:02d}.jpg'.format(i))
#  camera.capture(rawCapture, format="bgr")
#    image = rawCapture.array

    # display the image on screen and wait for a keypress
 #   cv2.imwrite("calibrationImages/Pi3/image{0:02d}.jpg".format(i), image)

