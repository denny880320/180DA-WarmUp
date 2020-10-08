#http://tsaith.github.io/record-video-with-python-3-opencv-3-on-osx.html for mac OS captures

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('Task2.mp4',fourcc, 20.0, (width, height))

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret==True:
        frame = cv2.flip(frame,0)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(frame,frame, mask= mask)
        out.write(res)
        
        cv2.namedWindow('frame')
        cv2.namedWindow('mask')
        cv2.namedWindow('res')

        cv2.imshow('frame',frame)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
