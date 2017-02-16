import unittest, time
from tempfile import TemporaryDirectory, gettempdir
from git import Repo
from pathlib import Path
from flags import Flag, BranchFlag

def unlink_if_file(path):
    if path.is_file():
        path.unlink()

class Test_Flag(unittest.TestCase):
    def setUp(self):
        # creating Repo
        self.tdir = TemporaryDirectory()        
        self.tpath = Path(self.tdir.name)
        self.repo = Repo.init(str(self.tpath))
        filenames_master = ['test1', 'test2', 'test3']
        for path, content in zip(filenames_master, ['con1', 'con2', 'con3']):
            (self.tpath / path).write_text(content)
        self.repo.index.add(filenames_master)
        self.repo.index.commit("initial commit")
        second_branch = self.repo.create_head('second', 'HEAD')
        second_branch.checkout()
        filenames_second = ['test1s','test2s','test3s'] 
        self.files = filenames_master + filenames_second
        for path, content in zip(filenames_second, ['con1s', 'con2s', 'con3s']):
            (self.tpath / path).write_text(content)
            print(self.tpath / path)
        self.repo.index.add(filenames_second)
        self.repo.index.commit("second commit")
        self.repo_heads_names = [h.name for h in self.repo.heads]
        self.assertListEqual(self.repo_heads_names, ['master', 'second'])

        self.flag = BranchFlag('TEST_FLAG', self.repo)

    def test_init(self):
        isinstance(self.flag.repo, Repo)
        self.assertEqual(self.flag.repo.head.ref, self.flag.repo.heads['second'])        
        for filename in self.files:
            self.assertTrue((Path(self.repo.working_tree_dir) / filename).is_file())

    def test_check_branches_state(self):
        for branch in self.repo_heads_names:        
            self.flag.state = branch
            self.assertTrue(self.flag.check_state())
        self.assertRaises(AssertionError, setattr, self.flag, "state", "niemaster")
        self.assertEqual(self.flag.state, "second")
        self.flag.state = None
        self.assertEqual(self.flag.state, None)
        self.assertTrue(self.flag.check_state())

    def test_del_state(self):
        self.flag.state = "second"
        delattr(self.flag, "state")
        self.assertEqual(self.flag.state, None)
        self.assertFalse(self.flag.path.is_file())

    def tearDown(self):
        # https://github.com/gitpython-developers/GitPython/issues/553
        self.repo.git.clear_cache()
        self.tdir.cleanup()

if __name__ == '__main__':
    unittest.main()