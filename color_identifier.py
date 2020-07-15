import numpy as np
from cv2 import cv2


path = "alpr-unconstrained/samples/only_cars/5.png"
frame = cv2.imread(path)
frame = np.array(frame)

hsv_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)


low_colors = [[0, 0, 220], [0, 0, 0], [180, 150, 150], [90, 150, 150], [0, 0, 0]]
high_colors = [[255, 30, 255], [255, 255, 30], [250, 255, 255], [120, 255, 255], [10, 255, 255]]
color_names = ["white", "black", "blue", "green", "red"]

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
    cv2.imwrite(path + str(color_names[x]) + str(".jpg"), color_mask)

print(ans[0])