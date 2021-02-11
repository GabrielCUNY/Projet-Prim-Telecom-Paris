### Configure paths. ###
PROJECT_PATH := $(CURDIR)
ENV_PATH := $(CURDIR)/python_env
PYTHON := $(ENV_PATH)/bin/python3
DEEPSORT_PATH := $(CURDIR)/deep_sort
PATH_TO_PY3 := /usr/bin/python3
### Globall installation ###


# Shortcut to set env command before each python cmd.
VENV = source $(ENV_PATH)/bin/activate

# Config is based on two environment files, initalized here.
virtualenv: $(ENV_PATH)/bin/activate

# Virtualenv file containing python libraries.
ifneq ("$(wildcard $(PATH_TO_PY3))","")
$(ENV_PATH)/bin/activate:
	python -m virtualenv -p $(PATH_TO_PY3) $(ENV_PATH)
else
$(ENV_PATH)/bin/activate:
	python -m virtualenv -p /usr/local/bin/python3 $(ENV_PATH)
endif

#downloader drive weight
DOWNLOAD = $(PYTHON) $(PROJECT_PATH)/download_drive.py --deep_sort_path=$(DEEPSORT_PATH)
# Install python requirements.
directory : 
	mkdir -p $(PROJECT_PATH)/data/video/det/img1 && mkdir -p $(DEEPSORT_PATH)/resources/detections/MOT16_POI_train && mkdir -p $(DEEPSORT_PATH)/resources/detections/MOT16_POI_test && mkdir -p $(DEEPSORT_PATH)/resources/networks
download_dr:
	$(VENV) && $(DOWNLOAD);
pip: virtualenv
	$(VENV) && cd $(APP_PATH) && pip3 install -r $(PROJECT_PATH)/requirements.txt;

# Global install.
install: pip directory download_dr

#projet target#
GENERATION_NPY = $(PYTHON) $(DEEPSORT_PATH)/tools/generate_detections.py --model=$(DEEPSORT_PATH)/resources/networks/mars-small128.pb --mot_dir=$(PROJECT_PATH)/data/video --output_dir=$(DEEPSORT_PATH)/custom/detections

DEEPSORT = $(PYTHON) $(DEEPSORT_PATH)/deep_sort_app.py --sequence_dir=$(PROJECT_PATH)/data/video/det --detection_file=$(DEEPSORT_PATH)/custom/detections/det.npy --output_file=$(PROJECT_PATH)/resultat_deep_sort/result.txt --min_confidence=0.3 --nn_budget=100 --display=True

DETECT = $(PYTHON) $(PROJECT_PATH)/detection/detection.py --project_path=$(PROJECT_PATH) --video_name=video --n_frame=500

download:
	$(VENV) && $(DOWNLOAD)

#execute from detection to tracking with the video cut frame by frame provided
all:
	$(VENV) && $(DETECT) && rm $(DEEPSORT_PATH)/custom/detections/det.npy && $(GENERATION_NPY) && $(DEEPSORT)

#Execute all the tracking with the detection already done but without the .npy file.
all_deep_sort:
	$(VENV) && rm $(DEEPSORT_PATH)/custom/detections/det.npy && $(GENERATION_NPY) && $(DEEPSORT)

#perform the detection alone
detect:
	$(VENV) && $(DETECT)

#execute the generation of the npy file
generate_detections:
	$(VENV) && $(GENERATION_NPY)

#execute only deep_sort (you already have the npy file corresponding to your detection)
deeps:
	$(VENV) && $(DEEPSORT)

#Execute all with a new video not cut frame by fram
all_new:
	$(VENV) && rm -R data/video/img1 && mkdir data/video/img1 && $(PYTHON) $(PROJECT_PATH)/convert_to_frames/main.py $(video_path) $(n_frame) && $(DETECT) && rm $(DEEPSORT_PATH)/custom/detections/det.npy && $(GENERATION_NPY) && $(DEEPSORT)

#Découper une vidéo image par image
add_new:
	$(VENV) && $(PYTHON) $(PROJECT_PATH)/convert_to_frames/main.py $(video_path) $(n_frame)

video: 
	$(VENV) && $(PYTHON) $(DEEPSORT_PATH)/generate_videos.py --mot_dir=$(PROJECT_PATH)/data/video --result_dir=$(DEEPSORT_PATH)/result_moteval --output_dir=$(PROJECT_PATH)/resultat_deep_sort --update_ms=40 

moteval: 
	$(VENV) && $(PYTHON) $(DEEPSORT_PATH)/evaluate_motchallenge.py --mot_dir=$(PROJECT_PATH)/data/video --detection_dir=$(DEEPSORT_PATH)/custom/detections --output_dir=$(DEEPSORT_PATH)/result_moteval