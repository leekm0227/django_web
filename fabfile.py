from fabric.api import env, run

env.user = "leekm0227"
env.hosts = ["35.239.104.137"]
env.password = "0000"
PROJECT_NAME = "django_web"
PROJECT_DIR = '/home/{}/{}'.format(env.user, PROJECT_NAME)


def deploy():
    run('date')
    #run('uwsgi --stop ' + PROJECT_DIR + '/uwsgi.pid')
    run('git --git-dir=' + PROJECT_DIR + '/.git pull')
    #run('uwsgi --ini ' + PROJECT_DIR + '/uwsgi.ini')
