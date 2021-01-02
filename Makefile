### Configure paths. ###
PROJECT_PATH := $(CURDIR)
ENV_PATH := $(CURDIR)/python_env
PYTHON := $(ENV_PATH)/bin/python3
DEEPSORT_PATH := $(CURDIR)/deep_sort

### Globall installation ###

# Shortcut to set env command before each python cmd.
VENV = source $(ENV_PATH)/bin/activate

# Config is based on two environment files, initalized here.
virtualenv: $(ENV_PATH)/bin/activate

# Virtualenv file containing python libraries.
$(ENV_PATH)/bin/activate:
	virtualenv -p /usr/local/bin/python3 $(ENV_PATH)

# Install python requirements.
pip: virtualenv
	$(VENV) && cd $(APP_PATH) && pip3 install -r $(PROJECT_PATH)/requirements.txt && mkdir $(PROJECT_PATH)/data/video/det/img1;

# Global install.
install: pip

### Projet targets ###

detect:
	$(VENV) && $(PYTHON) $(PROJECT_PATH)/main.py det

ds:
	$(VENV) && rm $(DEEPSORT_PATH)/custom/detection/det.npy && $(PYTHON) $(DEEPSORT_PATH)/tools/generate_detections.py --model=$(DEEPSORT_PATH)/resources/networks/mars-small128.pb --mot_dir=$(PROJECT_PATH)/data/video --output_dir=$(DEEPSORT_PATH)/custom/detections && $(PYTHON) $(DEEPSORT_PATH)/deep_sort_app.py --sequence_dir=$(PROJECT_PATH)data/video --detection_file= $(DEEPSORT_PATH)/custom/detections/det.npy --min_confidence=0.3 --nn_budget=100 --display=True
