from fabric.contrib.files import append, exists, sed, put
from fabric.api import env, local, run, sudo
import os


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_DIR)
REPO_URL = ""
PROJECT_NAME = "django_web"
REMOTE_HOST_SSH = "35.239.104.137"
REMOTE_HOST = "35.239.104.137"
REMOTE_USER = "leekm0227"
REMOTE_PASSWORD = "0000"

env.user = REMOTE_USER
env.hosts = [REMOTE_HOST_SSH]
env.password = REMOTE_PASSWORD

project_folder = '/home/data/{}'.format(PROJECT_NAME)

def start():
    pass


def _update_virtualenv():
    virtualenv_folder = project_folder + '/../.virtualenvs/{}'.format(PROJECT_NAME)
    if not exists(virtualenv_folder + '/bin/pip'):
        run('cd /home/%s/.virtualenvs && virtualenv %s' % (env.user, PROJECT_NAME))
    run('%s/bin/pip install -r %s/requirements.txt' % (
        virtualenv_folder, project_folder
    ))