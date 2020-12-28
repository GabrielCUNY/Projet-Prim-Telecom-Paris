### Configure paths. ###
PROJECT_PATH := $(CURDIR)
ENV_PATH := $(CURDIR)/python_env
PYTHON := $(ENV_PATH)/bin/python3

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
	$(VENV) && cd $(APP_PATH) && pip3 install -r $(PROJECT_PATH)/requirements.txt;

# Global install.
install: pip

### Projet targets ###

detect:
	python3 main.py det

ds:
	rm deep_sort/custom/detections/det.npy && python3 deep_sort/tools/generate_detections.py --model=deep_sort/resources/networks/mars-small128.pb --mot_dir=data/video --output_dir=deep_sort/custom/detections && python3 deep_sort/deep_sort_app.py --sequence_dir=data/video --detection_file=deep_sort/custom/detections/custom_video.npy --min_confidence=0.3 --nn_budget=100 --display=True
