'''
Basic flagging through text files
'''
from pathlib import Path
from git import Repo

class Flag:
    # rewrite state as @property https://docs.python.org/3.6/library/functions.html#property
    def __init__(self, name):
        assert name == name.upper(), 'Only upper flags names are allowed'        
        self.name = name
        self.path = Path('.', '.' + name)
        assert not self.path.is_dir(), 'Flag file cannot be a directory'
        # assert self.check_good_state(), 'Wrong Flag file starting state'
    
    def _get_state(self):
        if self.path.is_file():
            with self.path.open('r') as f:
                return f.read()
        else:
            return None

    def get_state(self):
        state = self._get_state()
        if state != None:
            assert self.__class__._check_good_state(state), 'Wrong state'
        return state

    def set_state(self, state):
        if state == None:
            if self.path.is_file():
                self.path.unlink()
        else:            
            state = str(state)
            assert self.__class__._check_good_state(state), 'Wrong state'
            with self.path.open('w') as f:
                f.write(state)
    
    def check_good_state(self):
        state = self._get_state()
        return state == None or self.__class__._check_good_state(state)

    @classmethod
    def _check_good_state(cls, state):
        '''
        Checked before state assigment and reading.
        Child-classes can iplement this method.
        None is always good.
        '''
        return True

# class BranchFlag(Flag):    
#     def __init__(self, name, repo):
#         super().__init__(name)
#         self.repo = repo

#     @classmethod
#     def _check_good_state(cls, state):
#         git



