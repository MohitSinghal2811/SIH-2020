from .models import Camera
from .src.alpr.vehicle_detection import extract_car
from .src.alpr.license_plate_detection import extract_lp
from .src.alpr.ocr2 import read_plate
from cv2 import cv2


def extract_attributes(frame):
    vehicles = extract_car(frame)
    for i in vehicles:
        lp = extract_lp(i)
        counter = 1
        # for j in lp:
        #     cv2.imwrite("src/test_output/image" + str(counter) + ".jpeg" , j)
        #     counter+=1
        x =  (read_plate(lp))
        print(x)
        return x
        
