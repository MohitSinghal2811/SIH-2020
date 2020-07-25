# 3 files required -> coco.names,yolov3.weigths,yolov3.cfg and a sample image .. 
# link to files https://drive.google.com/drive/folders/1SJ084lQ7ACXnjnrG8Q8tkfvhm4oAma16?usp=sharing
# change the paths accordingly
# change the cv2_imshow function if running on laptop,on colab it will work fine



import numpy as np
import argparse
import time
from cv2 import cv2
import os




def extract_car(frame):
  path="yolo-coco/coco.names"
  labelsPath = path
  LABELS = open(labelsPath).read().strip().split("\n")

  np.random.seed(42)
  COLORS = np.random.randint(0, 255, size=(len(LABELS), 3),
    dtype="uint8")

  weightsPath="yolo-coco/yolov3.weights"
  configPath ="yolo-coco/yolov3.cfg"
  
  print("[INFO] loading YOLO from disk...")
  net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)



#This is not the path of the image
#it is after cv2 has read the image


  image=frame																
  (H, W) = image.shape[:2]


  ln = net.getLayerNames()
  ln = [ln[i[0] - 1] for i in net.getUnconnectedOutLayers()]


  blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (416, 416),
    swapRB=True, crop=False)
  net.setInput(blob)
  start = time.time()
  layerOutputs = net.forward(ln)
  end = time.time()


  print("[INFO] YOLO took {:.6f} seconds".format(end - start))

  boxes = []
  confidences = []
  classIDs = []
  keylist=['car', 'bus', 'truck']        # Needs some changes
  dict_boundingbox = {key:[] for key in keylist}
  dict_confidence={key:[] for key in keylist}

  for output in layerOutputs:

    for detection in output:
      
      scores = detection[5:]
      classID = np.argmax(scores)
      confidence = scores[classID]

      
      if confidence > 0.5:
        
        box = detection[0:4] * np.array([W, H, W, H])
        (centerX, centerY, width, height) = box.astype("int")

        
        x = int(centerX - (width / 2))
        y = int(centerY - (height / 2))

        if LABELS[classID] in keylist:
          dict_boundingbox[LABELS[classID]].append([x, y, int(width), int(height)])
          dict_confidence[LABELS[classID]].append(float(confidence))
        

        confidences.append(float(confidence))
        boxes.append([x, y, int(width), int(height)])
  
        classIDs.append(classID)

      #for printing bounding boxes etc on image


  idxs = cv2.dnn.NMSBoxes(boxes, confidences, 0.5,0.3)

  if len(idxs) > 0:

    for i in idxs.flatten():
    
      (x, y) = (boxes[i][0], boxes[i][1])
      (w, h) = (boxes[i][2], boxes[i][3])

      
      color = [int(c) for c in COLORS[classIDs[i]]]
      cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
      text = "{}: {:.4f}".format(LABELS[classIDs[i]], confidences[i])
      cv2.putText(image, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, color, 2)

  cv2.imwrite("detected-cars/demo_yolo3.jpg",image)
  print(dict_boundingbox)
  print(dict_confidence)
  cropped_images = []
  for key in keylist:
    for bbox in dict_boundingbox[key]:
    #   print(bbox)


      x=bbox[0]
      y=bbox[1]
      w=bbox[2]
      h=bbox[3]

      cropped_image=image[y:y+h,x:x+w]
      #cv2.imshow(cropped_image)
      cropped_images.append(cropped_image)

  return cropped_images


if __name__ == "__main__":
    #obj = object_detect()
    path = "C:\\Users\\Dell\\Desktop\\sih\\Audi500\\"
    for imgPath in os.listdir(path):

      frame = cv2.imread(path+imgPath)
      counter = 1
      for x in extract_car(frame):
        print(couter)
        cv2.imwrite("Audi500_cropped/audi" + str(counter) + ".jpg", x)
        counter = counter + 1
