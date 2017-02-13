'''
Basic flagging through text files
'''
import os#, git
from pathlib import Path

class Flag:
    def __init__(self, name):
        assert name == name.upper(), 'Only upper flags names are allowed'        
        self.name = name
        self.path = Path('.', '.' + name)
        assert not self.path.is_dir(), 'Flag file cannot be a directory'
        assert self.check_good_state(), 'Wrong Flag file starting state'
    
    def _get_state(self):
        if self.path.is_file():
            with self.path.open('r') as f:
                return f.read()
        else:
            return None

    def get_state(self):
        state = self._get_state()
        assert Flag._check_good_state(state)
        return state

    def set_state(self, state):
        assert Flag._check_good_state(state)
        if state == None:
            self.path.unlink()
        else:
            with self.path.open('w') as f:
                f.write(str(state))
    
    def check_good_state(self):
        return Flag._check_good_state(self._get_state())

    @classmethod
    def _check_good_state(cls, state):
        '''
        Checked before state assigment and reading.
        Child-classes can iplement this method.
        '''
        return True

# class BranchFlag(Flag):    
#     def __init__(self, name, repo):
#         super().__init__(name)
#         self.repo = repo

#     @classmethod
#     def _check_good_state(cls, state):
#         git



