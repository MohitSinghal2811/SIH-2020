from vehicle.src.alpr.vehicle_detection import extract_car
from vehicle.src.alpr.license_plate_detection import extract_lp
from vehicle.src.alpr.ocr2 import read_plate
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
        
