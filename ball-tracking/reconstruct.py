# import the necessary packages
from collections import deque
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time
import pickle

DEFAULT_BUFFER = 4096

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
help="path to the (optional) video file", required=True)
ap.add_argument("-b", "--buffer", type=int, default=DEFAULT_BUFFER,
help="max buffer size")
args = vars(ap.parse_args())

# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
    vs = VideoStream(src=0).start()
    # otherwise, grab a reference to the video file
else:
    vs = cv2.VideoCapture(args["video"])

# allow the camera or video file to warm up
time.sleep(2.0)

#reload object from file
load_file = open('path.pkl', 'rb')
pts = pickle.load(load_file)
load_file.close()

img = np.zeros((600,600,3), np.uint8)
val = 255

for i in range(1, len(pts)):

    # if either of the tracked points are None, ignore
    # them
    if pts[i - 1] is None or pts[i] is None:
        continue

    if val < 100: val = 255
    else: val -= 30

    # otherwise, compute the thickness of the line and
    # draw the connecting lines
    thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
    img = cv2.line(img, pts[i - 1], pts[i], (0, 0, val), thickness)

    # show the frame to our screen
    cv2.imshow("lines", img)

cv2.imwrite("reconstructed.jpg", img)


# for i in range(1, len(pts)):
#
#     # if either of the tracked points are None, ignore
#     # them
#     if pts[i - 1] is None or pts[i] is None:
#         continue
#
#         # otherwise, compute the thickness of the line and
#         # draw the connecting lines
#         thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
#         img = cv2.line(img, pts[i - 1], pts[i], (0, 0, 255), thickness)
#
#         # show the frame to our screen
#         cv2.imshow("lines", img)
#
# # keep looping
# while True:
#     # grab the current frame
#     frame = vs.read()
#
#     # handle the frame from VideoCapture or VideoStream
#     frame = frame[1] if args.get("video", False) else frame
#
#     # if we are viewing a video and we did not grab a frame,
#     # then we have reached the end of the video
#     if frame is None:
#         break
#
#         # resize the frame, blur it, and convert it to the HSV
#         # color space
#         frame = imutils.resize(frame, width=600)
#
#         # loop over the set of tracked points
#         for i in range(1, len(pts)):
#
#             # if either of the tracked points are None, ignore
#             # them
#             if pts[i - 1] is None or pts[i] is None:
#                 continue
#
#                 # otherwise, compute the thickness of the line and
#                 # draw the connecting lines
#                 thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
#                 cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
#
#                 # show the frame to our screen
#                 cv2.imshow("Frame", frame)
