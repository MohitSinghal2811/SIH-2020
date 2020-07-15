import numpy as np
import cv2
import object_detection
#import color_detection
#import model_detection
#import alpr
cap=cv2.VideoCapture(0)     #path of video
cap.set(cv2.cv.CV_CAP_PROP_FPS, 60)   #frames per second (can be lowered)
fps=60
count_frames=1
while True:
    frame_present,frame=cap.read()
s
    # insert time_stamp in db
    time_stamp=count_frames/fps
    if frame_present==True:
        obj_detector=object_detection.object_detect()
        cropped_car=obj_detector.extract_car(frame)

        color_detector=color_detection.major_color()
        # insert this color in db
        color=color_detector.max_color(cropped_car)
        
        #license plate

        


    else:
        break


    cv2.imshow("Frame",frame)
    count_frames+=1
    key=cv2.waitKey(1)
    if key==27:                      #press esc to force stop the loop before ending of video
        break