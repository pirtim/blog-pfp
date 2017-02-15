'''
Basic flagging through text files
'''
from pathlib import Path
from git import Repo

class Flag:
    def __init__(self, name):
        assert name == name.upper(), 'Only upper flags names are allowed'        
        self.name = name
        self.path = Path('.', '.' + name)
        assert not self.path.is_dir(), 'Flag file cannot be a directory'
        assert self.check_state(), 'Wrong Flag file starting state'

    def _state(self):
        'Gets state without checking it.'
        if self.path.is_file():
            return self.path.read_text()
        else:
            return None
    
    @property
    def state(self):
        state = self._state()
        if state != None:
            assert self.__class__._check_state(state), 'Wrong state'
        return state

    @state.setter
    def state(self, state):
        if state == None:
            if self.path.is_file():
                self.path.unlink()
        else:            
            state = str(state)
            assert self.__class__._check_state(state), 'Wrong state'
            self.path.write_text(state)
    
    def check_state(self):
        state = self._state()
        return state == None or self.__class__._check_state(state)

    @classmethod
    def _check_state(cls, state):
        '''
        Checked before state setter and after getter.
        Child-classes can implement this method.
        None is always a good state.
        '''
        return True

# class BranchFlag(Flag):    
#     def __init__(self, name, repo):
#         super().__init__(name)
#         self.repo = repo

#     @classmethod
#     def _check_state(cls, state):
#         git



