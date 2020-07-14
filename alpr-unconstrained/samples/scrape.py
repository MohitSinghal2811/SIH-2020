import requests
import cv2
import os
import csv
import sys
             

prop_file = open('Book1.csv', 'r')
csv_reader = csv.reader(prop_file)
counter = 0
for row in csv_reader:
    try:
            coded_url = row[0]
            r = requests.get(coded_url)
            with open("Book1/" + str(counter) + ".png",'wb') as f: 
                f.write(r.content)
            print( str(counter) + " Vehicles Downloaded ", end = "\r")
            counter = counter + 1
    except Exception as e:
            print(e)
            print("Failed to download url number :-", end = " ")
            print(counter)

print()


