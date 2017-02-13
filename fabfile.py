from fabric.api import local, run, hosts, env, cd
from pathlib import PurePosixPath, PureWindowsPath
import os

from settings import host, prod_path_tuple, dev_path_tuple

# settings outside git repo
env.hosts = host

# Fabric doesn't accepts os.PathLike, so this way it's more descriptive
rails_PATH = {
    'prod' : str(PurePosixPath(*prod_path_tuple)), 
    'dev'  : str(PurePosixPath( *dev_path_tuple))
}

flags_PATH = {
    'STAGED_TO_DEPLOY' : str(PureWindowsPath('.', '.STAGED_TO_DEPLOY')),    
    'READY_TO_DEPLOY'  : str(PureWindowsPath('.',  '.READY_TO_DEPLOY'))
}

def hello(name="world"):
    print("Hello %s!" % name)
  
def deploy():
    local('ls')



    with cd(rails_PATH['dev']):
        run('ls')