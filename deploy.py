from fabric.contrib.files import append, exists, sed, put
from fabric.api import env, local, run, sudo
import random
import os
import json


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
REPO_URL = ""
PROJECT_NAME = "django_web"
REMOTE_HOST_SSH = ""
REMOTE_HOST = "35.239.104.137"
REMOTE_USER = "root"
REMOTE_PASSWORD = ""

