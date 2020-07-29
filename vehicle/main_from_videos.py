import numpy as np
from cv2 import cv2
from .main_from_images import extract_attributes
from .video_process import write_frame

path=""


def process_video(path):
    cap=cv2.VideoCapture(path)    
    target = 200
    counter = 1

    writer=None
    (W,H)=(None,None)

    ans = []
    while True:
        print("counter" + str(counter))
        grabbed,frame=cap.read()

        if not grabbed:
            break

        if W is None or H is None:
            (H,W)=frame.shape[:2]

        if writer is None:
            fourcc=cv2.VideoWriter_fourcc(*"MJPG")
            writer=cv2.VideoWriter("src/test_videos/output_video.avi",fourcc,30,(W,H),True)

        
        write_frame(frame,writer)
        #lp, color = extract_attributes(frame,writer)
        if(lp is not None and color is not None):
            ans.append([lp, color])
        counter += 1

    return ans
