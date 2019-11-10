# References GestureOS project: https://github.com/CLiu13/GestureOS/blob/master/src/tools/captureProcessFrame.py

import cv2

# Captures a frame via PiCamera and processes frame to eliminate unnecessary noise
def captureProcessFrame(camera, rgbFrame, blurRegion):

    camera.capture(rgbFrame, format = "bgr", use_video_port = True)
    rawFrame = rgbFrame.array

    grayFrame = cv2.cvtColor(rawFrame, cv2.COLOR_BGR2GRAY)
    blurFrame = cv2.GaussianBlur(grayFrame, (blurRegion, blurRegion), 0)

    rgbFrame.truncate(0)

    return blurFrame
