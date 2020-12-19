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


#config feature_extraction
config['feature_extraction'] = {}
config['feature_extraction']['alpha_op'] = 1.0
config['feature_extraction']['lomo'] = 0 #0: no lomo features, 1: lomo on whole body, 2: lomo on body parts obtained by pose estimation (openPose)
config['feature_extraction']['lomo_config'] = "lomo_config.json"


#config deep_sort
config['ds'] = {}
config['ds']['max_age'] = 50
config['ds']['n_init'] = 50
config['ds']['max_iou_distance'] = 0.7
config['ds']['min_confidence'] = 0.10
config['ds']['max_cosine_distance'] = 0.25
config['ds']['nn_budget'] = 100
config['ds']['alpha_ds'] = 0.0

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
        print("Detection Start, it will be stored in /detection/result_detection.txt")
        detection(config['path']+"data/" + config['vid_name'], config['path'] +"yolo-tiny.h5", config['n_frame'])



    elif arg == "fe":
        print("Features extraction from detection boxes "+("'and open pose data/'" if config['feature_extraction']['alpha_op'] > 0 else '')+"...")
        os.system("python3 "+config['path']+"deep_sort/tools/generate_detections.py \
        --model="+config['path']+"deep_sort/resources/networks/mars-small128.pb \
        --mot_dir="+config['path'] + "data/" + config['vid_name'] + "/ \
        --offset="+str(config['offset'])+" \
        --det_stage='det"+config['feature_extraction']['str']+"' \
        --openpose="+("'openpose/'" if config['feature_extraction']['alpha_op'] > 0 else '')+" \
        --lomo="+str(config['feature_extraction']['lomo'])+"\
        --alpha_op=" + str(config['feature_extraction']['alpha_op']) + "\
        --lomo_config=" + config['path'] + str(config['feature_extraction']['lomo_config'])+" \
        --output_dir='" + config['path'] + "data/" + config['vid_name'] + "/post-detection" + config['feature_extraction']['str']+"'")
        print("Detections + Features stored in "+ config['path'] + "data/" + config['vid_name'] + "/post-detection" + config['feature_extraction']['str']+"/result_detection.npy")



    elif arg == "ds":
        print("Running Deep Sort algorithm...")
        if not os.path.exists(config['path']+"data/"+config['vid_name']+"/det"+config['feature_extraction']['str']+("_pca"+config['pca']['str']+"" if config['pca']['active'] else '')+"_ds"+config['ds']['str']+"/"):
            os.mkdir(config['path']+"data/"+config['vid_name']+"/det"+config['feature_extraction']['str']+("_pca"+config['pca']['str']+"" if config['pca']['active'] else '')+"_ds"+config['ds']['str']+"/")
        os.system("python3 "+config['path']+"deep_sort/deep_sort_app.py \
        --sequence_dir="+config['path']+"data/"+config['vid_name']+"/ \
        --detection_file='"+ config['path'] + "data/" + config['vid_name'] + "/det" + config['feature_extraction']['str']+("_pca"+config['pca']['str']+"" if config['pca']['active'] else '')+"/det.npy' \
        --offset="+str(config['offset'])+" \
        --n_frames=" + str(config['n_frames']) + " \
        --max_iou_distance=" + str(config['ds']['max_iou_distance']) + " \
        --max_age=" + str(int(config['ds']['max_age'])) + " \
        --alpha_ds=" + str(config['ds']['alpha_ds']) + "\
        --n_init=" + str(int(config['ds']['n_init'])) + " \
        --min_confidence=" + str(config['ds']['min_confidence']) + " \
        --max_cosine_distance=" + str(config['ds']['max_cosine_distance']) + "\
        --nn_budget=" + str(int(config['ds']['nn_budget'])) + " \
        --output_file='"+config['path']+"data/"+config['vid_name']+"/post-detection"+config['feature_extraction']['str']+("_pca"+config['pca']['str']+"" if config['pca']['active'] else '')+"_ds"+config['ds']['str']+"/result_detection.npy' \
        --display=False")
        print("Deep Sort tracklets stored in "+config['path']+"data/"+config['vid_name']+"/post-detection"+config['feature_extraction']['str']+("_pca"+config['pca']['str']+"" if config['pca']['active'] else '')+"_ds"+config['ds']['str']+"/result_detection.npy")
        score_ds()
