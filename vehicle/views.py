from django.shortcuts import render, HttpResponse

# Create your views here.
from .models import CarSurveillance
from .main_from_videos import process_video
from cv2 import cv2
from datetime import datetime
from vehicle.src.alpr.vehicle_detection import extract_car
from vehicle.src.alpr.license_plate_detection import extract_lp
from vehicle.src.alpr.ocr2 import read_plate
from vehicle.src.color_identifier import color_segmenter
import sys
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def save_to_database(request):
    # path = "src/test_videos/new_videos/9.mp4"
    # ans = process_video(path)

    
    
    # for x in ans:
    #     c = CarSurveillance(CameraID = "2820010001", Brand = "Tata", PlateNumber = x[0], CarModel = "Nano", Color = x[1], FirstSeen = datetime.now(), LastSeen = datetime.now())
    #     c.save()
    # path = "src/test_output/scene00051.png"
    # frame = cv2.imread(path)

    # vehicles, img = extract_car(frame)
    # cv2.imwrite("temp3.jpg", vehicles[0])
    # for i in vehicles:
    #     cv2.imwrite("temp2.jpg", img)
    #     cv2.imwrite("temp1.jpg", i)
    #     maj_color=color_segmenter(i)
    #     print(maj_color)
    #     lp = extract_lp(i)
    #     x =  (read_plate(lp))
    #     print(x)
    return render(request, "vehicle/homeLogin.html")


def queryfromimage(request):

    print("Mohit Singhal")
    print(request)
    if request.method == 'POST' and request.FILES['filename']:
        print("HO HO HO")
        myfile = request.FILES['filename']
        print(myfile.name)
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        path = "media/" + myfile.name
        frame = cv2.imread(path)

        vehicles, img = extract_car(frame)
        for i in vehicles:
            maj_color=color_segmenter(i)
            print(maj_color)
            lp = extract_lp(i)
            x =  (read_plate(lp))
            print(x)
            context = {"major_color": maj_color, "number_plate": x}

    return render(request, "vehicle/submitted.html", context)




# if __name__ == "__main__":
#     img_path = "src/test_images/Indian_vehicles/0.png"
#     frame = cv2.imread(img_path)
#     extract_attributes(frame)