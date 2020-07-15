import object_detection
import alpr
import color_identifier
from cv2 import cv2
import os
import shutil

def image_attr(frame, counter2):
    tmp_path = "alpr-unconstrained/samples/cropped/cropped" + str(counter2)
    os.mkdir(tmp_path)
    tmp_path2 = "samples/cropped/cropped" + str(counter2)

    obj = object_detection.object_detect()
    cropped_cars = obj.extract_car(frame)
    print(len(cropped_cars))
    counter = 1
    for img in cropped_cars:
        try:
            color_identifier.color_segmenter(img)
            cv2.imwrite(tmp_path + "/car number " + str(counter) + ".jpg", img)
            counter+=1
        except Exception as e:
            print(e)

    if(len(cropped_cars) != 0):
        alpr.run_alpr_unconstrained(tmp_path2)
    #shutil.rmtree(tmp_path)

if __name__ == "__main__":
    path = "alpr-unconstrained/samples/test/har4.jpeg"
    frame = cv2.imread(path)
    image_attr(frame, 3)