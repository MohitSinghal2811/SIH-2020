from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import CarSurveillance
from .main_from_videos import process_video
from cv2 import cv2
from datetime import datetime

def save_to_database(request):
    
    path="C:/Users/Dell/Desktop/sih/mohitvideo1.mp4"
    ans = process_video(path)
    
    for x in ans:
        c = CarSurveillance(CameraID = "2820010001", Brand = "Tata", PlateNumber = x[0], CarModel = "Nano", Color = x[1], FirstSeen = datetime.now(), LastSeen = datetime.now())
        c.save()

    return HttpResponse("HI")




# if __name__ == "__main__":
#     img_path = "src/test_images/Indian_vehicles/0.png"
#     frame = cv2.imread(img_path)
#     extract_attributes(frame)