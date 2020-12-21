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
	virtualenv -p /usr/bin/python3 $(ENV_PATH)

# Install python requirements.
pip: virtualenv
	$(VENV) && cd $(APP_PATH) && pip3 install -r $(PROJECT_PATH)/requirements.txt;

# Global install.
install: pip

### Projet targets ###
