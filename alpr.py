import numpy as np
import cv2
import object_detection
import os

os.system('make --directory alpr-unconstrained/darknet/')
os.chdir('alpr-unconstrained/')
os.system('bash run.sh -i samples/test -o /tmp/output -c /tmp/output/results.csv')