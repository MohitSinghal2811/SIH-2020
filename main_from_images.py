import object_detection
import alpr
import color_identifier
from cv2 import cv2
import os
import shutil


path = "alpr-unconstrained/samples/only_cars/3.png"
frame = cv2.imread(path)
tmp_path = "alpr-unconstrained/samples/cropped"
os.mkdir(tmp_path)

obj = object_detection.object_detect()
cropped_cars = obj.extract_car(frame)
print(len(cropped_cars))
counter = 1
for img in cropped_cars:
    color_identifier.color_segmenter(img)
    cv2.imwrite(tmp_path + "/car number " + str(counter) + ".jpg", img)
    counter+=1


tmp_path2 = "samples/cropped"
alpr.run_alpr_unconstrained(tmp_path2)
shutil.rmtree(tmp_path2)