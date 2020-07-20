import numpy as np
from cv2 import cv2


def color_segmenter(frame):

    frame = np.array(frame)
    hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


    low_colors = [[90, 100,50], [40, 100, 50], [0,100,50],[0,0,0],[0,0,180],[0,5,125]]
    high_colors = [[120, 255,255], [60,255,255], [20, 255, 255],[180,255,20],[255,5,255],[255,255,150]]
    color_names = ["blue", "green", "red","black","white","gray"]

    #dont change value without consulting in group

    ans = ("UNK", 0)

    path = "color-cars/"

    red_low=[170,100,50]
    red_high=[180,255,255]
    for x in range(len(color_names)):
        if(x==2):
            mask1=cv2.inRange(hsv_frame,np.array(low_colors[x]),np.array(high_colors[x]))
            mask2=cv2.inRange(hsv_frame,np.array(red_low),np.array(red_high))
            color_mask=mask1+mask2
        else:
            color_mask=cv2.inRange(hsv_frame,np.array(low_colors[x]),np.array(high_colors[x]))
        #color_region=cv2.bitwise_and(frame,frame, mask=color_mask)     
        color_mask = np.array(color_mask)
        flatten_array = color_mask.flatten()
        ad = np.unique(flatten_array, return_counts=True)
        if(len(ad[1]) == 1):

            continue
        elif(ad[1][1] > ans[1]):
            ans = (color_names[x], ad[1][1])
        cv2.imwrite(path + str(color_names[x]) + str(".jpg"), color_mask)

    return(ans[0])



if __name__ == "__main__":
    path = "alpr-unconstrained/samples/only_cars/test_red.jpg"
    frame = cv2.imread(path)
    print(color_segmenter(frame))      
