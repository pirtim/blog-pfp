from fabric.api import local, run, hosts, env, cd
from pathlib import PurePosixPath, PureWindowsPath
from git import Repo
import os

from settings import host, prod_path_tuple, dev_path_tuple
from flags import BranchFlag

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
    repo = Repo('.')
    staged_flag = BranchFlag('STAGED_TO_DEPLOY', repo)
    # staged_flag.set_state_current_branch()

    local('ls')



    with cd(rails_PATH['dev']):
        run('ls')