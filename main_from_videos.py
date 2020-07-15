import numpy as np
from cv2 import cv2
import object_detection
#import color_detection
#import model_detection
#import alpr
cap=cv2.VideoCapture(0)     #path of video

while True:
    ret,frame=cap.read()
    if ret==True:
        obj_detector=object_detection.object_detect()
        cropped_car=obj_detector.extract_car(frame)

        color_detector=color_detection.major_color()
        # insert this color in db
        color=color_detector.max_color(cropped_car)

        #license plate

        


    else:
        break
    cv2.imshow("Frame",frame)
    key=cv2.waitKey(1)
    if key==27:                      #press esc to force stop the loop before ending of video
        break