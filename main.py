import os
import numpy as np
import pandas as pd
from detection.detection import detection
import json
import sys

config = {}
config['path'] = "/Users/gabrielcuny/Documents/Etude/Projet IA/PRIM/Projet-Prim-Telecom-Paris/"
config['vid_name'] = "video"
config['n_frame'] = 500



for arg in sys.argv[:2]:
    print(arg)
    if arg == "detection":
        print("Detection Start, it will be stored in /detection/result_detection.txt")
        detection(config['path']+"data/" + config['vid_name'], config['path'] +"yolo-tiny.h5", config['n_frame'])
    elif arg == "deep_sort":
        print("deep_sort")
