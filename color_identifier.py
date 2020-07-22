import numpy as np
from cv2 import cv2


def color_segmenter(frame, img_name):

    frame = np.array(frame)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    low_colors = [[0, 0, 193], [0, 0, 0], [94,80,2], [30,85,85], [0, 150, 50],[0,0,66]]
    high_colors = [[131, 30, 255], [255, 255, 25], [126, 255, 255], [10, 255, 255], [180, 255, 255],[255,33,230]]
    color_names = ["white", "black", "blue", "green", "red","grey"]

    ans = ("UNK", 0)

    path = "color-cars/"


    for x in range(len(color_names)):
        color_mask=cv2.inRange(hsv_frame,np.array(low_colors[x]),np.array(high_colors[x]))
        #color_region=cv2.bitwise_and(frame,frame, mask=color_mask)     
        color_mask = np.array(color_mask)
        flatten_array = color_mask.flatten()
        ad = np.unique(flatten_array, return_counts=True)
        if(len(ad[1]) == 1):

            continue
        elif(ad[1][1] > ans[1]):
            ans = (color_names[x], ad[1][1])
        cv2.imwrite(path + str(img_name) + "_" + str(color_names[x]) + str(".jpg"), color_mask)

    return(ans[0])



if __name__ == "__main__":
    path = "alpr-unconstrained/samples/Indian_vehicles/4.png"
    frame = cv2.imread(path)
    arr = path.split("/")
    print(color_segmenter(frame, arr[-1][:-4]))      
