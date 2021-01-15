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
	virtualenv -p $(PATH_TO_PY3) $(ENV_PATH)
else
$(ENV_PATH)/bin/activate:
	virtualenv -p /usr/local/bin/python3 $(ENV_PATH)
endif

# Install python requirements.
pip: virtualenv
	$(VENV) && cd $(APP_PATH) && pip3 install -r $(PROJECT_PATH)/requirements.txt && mkdir $(PROJECT_PATH)/data/video/det/img1;

# Global install.
install: pip

### Projet targets ###
GEN = $(PYTHON) $(DEEPSORT_PATH)/tools/generate_detections.py --model=$(DEEPSORT_PATH)/resources/networks/mars-small128.pb --mot_dir=$(PROJECT_PATH)/data/video --output_dir=$(DEEPSORT_PATH)/custom/detections

DS = $(PYTHON) $(DEEPSORT_PATH)/deep_sort_app.py --sequence_dir=$(PROJECT_PATH)/data/video/det --detection_file=$(DEEPSORT_PATH)/custom/detections/det.npy --output_file=$(PROJECT_PATH)/resultat_deep_sort/result.txt --min_confidence=0.3 --nn_budget=100 --display=True

DETECT = $(PYTHON) $(PROJECT_PATH)/detection/detection.py --project_path=$(PROJECT_PATH) --video_name=video --n_frame=500



all:
	$(VENV) && $(DETECT) && rm $(DEEPSORT_PATH)/custom/detections/det.npy && $(GEN) && $(DS)

all_ds:
	$(VENV) && rm $(DEEPSORT_PATH)/custom/detections/det.npy && $(GEN) && $(DS)

detect:
	$(VENV) && $(DETECT)

generate_detections:
	$(VENV) && $(GEN)

deep_sort:
	$(VENV) && $(DS)

all_new:
	$(VENV) && rm -R data/video/img1 && mkdir data/video/img1 && $(PYTHON) $(PROJECT_PATH)/convert_to_frames/main.py $(video_path) $(n_frame) && $(DETECT) && rm $(DEEPSORT_PATH)/custom/detections/det.npy && $(GEN) && $(DS)

add_new:
	$(VENV) && $(PYTHON) $(PROJECT_PATH)/convert_to_frames/main.py $(video_path) $(n_frame)
