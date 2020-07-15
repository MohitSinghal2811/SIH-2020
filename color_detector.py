from coloranalysis.colors import colorAreas
from cv2 import cv2
import matplotlib.pyplot as plt

path = "alpr-unconstrained/samples/only_cars/3.png"
hexColours =  ["#FE0000", "#FD6400", "#FFFF02", "#008101", "#0000FE", "#4B0081", "#BC31FD"]
#HEX codes of red, orange, yellow, green, blue, purple and violet
diff = 100
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #converting the colorspace from BGR to RGB
plt.imshow(img)
c = colorAreas()
ratio = c.getArea(hexColours=hexColours,path=path,diff=diff)
print(ratio)