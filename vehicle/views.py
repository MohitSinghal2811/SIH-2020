from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import CarSurveillance
from .test import extract_attributes
from cv2 import cv2
from datetime import datetime

def save_to_database(request):
    img_path = "src/test_images/Indian_vehicles/0.png"
    frame = cv2.imread(img_path)
    cv2.imwrite("image.png", frame)
    lp = extract_attributes(frame)
    print(lp)
    c = CarSurveillance(CameraID = "2820010001", Brand = "Tata", PlateNumber = lp, CarModel = "Nano", Color = "Red", FirstSeen = datetime.now(), LastSeen = datetime.now())
    c.save()

    return HttpResponse("HI")




# if __name__ == "__main__":
#     img_path = "src/test_images/Indian_vehicles/0.png"
#     frame = cv2.imread(img_path)
#     extract_attributes(frame)