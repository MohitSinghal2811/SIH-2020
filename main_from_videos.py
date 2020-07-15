import numpy as np
from cv2 import cv2
import main_from_images


path = "Video1.mp4"
cap=cv2.VideoCapture(path)    
target = 10
counter = 0


while True:
    print("counter" + str(counter))
    ret,frame=cap.read()
    if(counter > 400 and counter % target == 0):    
        if ret==True:
            main_from_images.image_attr(frame, counter)
        else:
            break
    counter += 1
