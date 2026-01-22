# COLOR DETECTION 

import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()

    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  
    lower = np.array([20,100,100])
    upper = np.array([35,255,255])

    mask = cv2.inRange(hsvFrame, lower, upper)
    result = cv2.bitwise_and(frame,frame,mask=mask) 

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
       if cv2.contourArea(cnt) > 500:
           x, y, w, h = cv2.boundingRect(cnt)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
           cv2.putText(frame,"Yellow Found",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    cv2.imshow('camera',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()
