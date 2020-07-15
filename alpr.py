import numpy as np
import cv2
import object_detection
import os


def run_alpr_unconstrained(path):
    os.system('make --directory alpr-unconstrained/darknet/')
    os.chdir('alpr-unconstrained/')
    os.system('bash run.sh -i ' + str(path) + ' -o /tmp/output -c /tmp/output/results.csv')

if __name__ == "__main__":
    path = "samples/test/"
    run_alpr_unconstrained(path)