import object_detection
import alpr
import color_identifier

from cv2 import cv2
import os
import shutil

def image_attr(frame, counter,writer):
    outputPath="src/testing_videos/output"
    cropped_cars = object_detection.extract_car(frame,writer)
    print(len(cropped_cars))
    
    for img in cropped_cars:
        try:
            print("frame number:- ",counter)
            maj_color=color_identifier.color_segmenter(img)
            cv2.imwrite( outputPath+ "/car number " + str(counter) + ".jpg", img)
            print("color:- ",maj_color)
            license_plate=alpr.license_plate_detection.extract_lp(img)
            #ocr lagao
            cv2.imwrite( outputPath+ "/lp number " + str(counter) + ".jpg", license_plate)


            counter+=1
        except Exception as e:
            print(e)

  

if __name__ == "__main__":
    path = "alpr-unconstrained/samples/test/har4.jpeg"
    frame = cv2.imread(path)
    image_attr(frame, 4)