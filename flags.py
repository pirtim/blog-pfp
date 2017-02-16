'''
Basic flagging through text files
'''
from pathlib import Path
from git import Repo

class Flag:
    '''
    File flag class. 
    Every object has related Path Object (self.path) and self.state.
    If self.state != None there exist hidden file under Path with self.name.
    File content is self.state.
    '''
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
            assert self.__class__._check_state(state, self), 'Wrong state'
        return state

    @state.setter
    def state(self, state):
        if state == None:
            if self.path.is_file():
                self.path.unlink()
        else:            
            state = str(state)
            assert self.__class__._check_state(state, self), 'Wrong state'
            self.path.write_text(state)

    @state.deleter
    def state(self):
        self.state = None
    
    def check_state(self):
        state = self._state()
        return state == None or self.__class__._check_state(state, self)
    
    @classmethod
    def _check_state(cls, state, self=None):
        '''
        Checked before state setter and after getter.
        Child-classes can implement this method.
        None is always a good state.
        '''
        return True

class BranchFlag(Flag):
    '''
    Flag child-class. 
    Every object has releted repo.
    Only allowed states: [None, #'name of related repo branch']
    '''
    def __init__(self, name, repo):
        super().__init__(name)
        assert isinstance(repo, Repo)
        self.repo = repo

    def get_heads_names(self):
        return [h.name for h in self.repo.heads]

    @classmethod
    def _check_state(cls, state, self):
        return state in self.get_heads_names()
