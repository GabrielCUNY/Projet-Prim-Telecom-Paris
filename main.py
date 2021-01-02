import os
import numpy as np
import pandas as pd
from detection.detection import detection
import json
import sys


configs = {}
with open('configs.json') as json_file:
    configs = json.load(json_file)


#config start
config = {}
config['path'] = "/Users/gabrielcuny/Documents/Etude/ProjetIA/PRIM/Projet-Prim-Telecom-Paris/"
config['vid_name'] = "video"
config['n_frame'] = 500
config['offset'] = 0


def conf_id(config):
    for k,v in configs.items():
        if v==config:
            return k
    id = 0 if len(configs)==0 else np.max(np.array(list(configs.keys())).astype(int))+1
    id = int(id)
    configs[id] = config.copy()
    with open('configs.json', 'w') as outfile:
        json.dump(configs, outfile)
    return id

def update_config(config):
    for key,c in config.items():
        if isinstance(c, dict):
            c['sub_config'] = key
            if 'str' in c.keys():
                del c['str']
            c['str'] = "_"+str(conf_id(c))
    return config

update_config(config)

for arg in sys.argv[:2]:



    if arg == "det":
        print("Detection Start, it will be stored in /data/det/det.txt")
        detection(config['path']+"data/" + config['vid_name'], config['path'] +"yolo-tiny.h5", config['n_frame'])
