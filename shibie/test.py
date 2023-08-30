import numpy as np
import cv2
import time
import datetime

cap = cv2.VideoCapture("")

fgbg = cv2.createBackgroundSubtractorMOG()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    fgmask, contours, hierarchy = cv2.findContours(cv2.EXTERNAL, cv2.CHAIN_SIMPLE)

    count = 0
    for cont in contours:
        Area = cv2.contourArea()
        if Area < 300:
            continue

        print("{}-prospect:{}".format(count), end="  ")

        rect = cv2.boundingRect(cont)

        print("x:{} y:{}".format(rect[0], rect[1]))

        y = 10 if rect[1] < 10 else rect[1]

    print("----------------------------")

    cv2.namedWindow("frame", 0);
    cv2.resizeWindow("frame", 480, 420);
    cv2.imshow('frame', frame)

    cv2.namedWindow("frame2", 0);
    cv2.resizeWindow("frame2", 480, 420);
    cv2.imshow('frame2', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

"""
    maxArea = 0
    for c in contours:
        Area = cv2.contourArea(c) 
        if Area < maxArea:
            #if cv2.contourArea(c) < 500:
            (x, y, w, h) = (0, 0, 0, 0)
            continue
        else:
            if Area < 1000:
                (x, y, w, h) = (0, 0, 0, 0)
                continue
            else:
                maxArea = Area
                m = c
                (x, y, w, h) = cv2.boundingRect(m)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        #out.write(frame)
"""