import numpy as np
from cv2 import cv2


red = np.uint8([[[0, 0, 0 ]]])
hsv_red = cv2.cvtColor(red,cv2.COLOR_BGR2HSV)
print( hsv_red )