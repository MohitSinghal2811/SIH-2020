import numpy as np
from cv2 import cv2
import main_from_images


path = "C:/Users/Dell/Documents/GitHub/SIH-2020/src/surveillance_video1.mp4"
cap=cv2.VideoCapture(path)    
target = 10
counter = 1

writer=None
(W,H)=(None,None)


while True:
    print("counter" + str(counter))
    grabbed,frame=cap.read()

    if not grabbed:
        break

    if W is None or H is None:
        (H,W)=frame.shape[:2]

    if writer is None:
        fourcc=cv2.VideoWriter_fourcc(*"MJPG")
        writer=cv2.VideoWriter("C:/Users/Dell/Documents/GitHub/SIH-2020/src/testing_videos/bb_video.avi",fourcc,30,(W,H),True)

    if(counter%20==0):
        main_from_images.image_attr(frame, counter,writer)
        
    counter += 1
