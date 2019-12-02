import numpy as np
import cv2
from matplotlib import pyplot as plt

imgL = cv2.imread('/home/pi/opencv/samples/data/aloeL.jpg', 0)
imgR = cv2.imread('/home/pi/opencv/samples/data/aloeR.jpg', 0)

stereo = cv2.StereoBM_create(numDisparities=16, blockSize=15)
disparity = stereo.compute(imgL, imgR)
plt.imshow(disparity, 'gray')
plt.imsave("map1.jpg", disparity)

disparity2 = cv2.convertScaleAbs(disparity, alpha=(255.0))
cv2.imwrite("map2.jpg", disparity2)

plt.show()
