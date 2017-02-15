import unittest
# import blog-pfp.flags
# from flags import Flag
from blog_pfp.flags import Flag

def unlink_if_file(path):
    if path.is_file():
        path.unlink()

class FlagDigit(Flag):
    @classmethod
    def _check_state(cls, state):
        # print(str(state), flush=True)
        return str.isdigit(state)

class Test_Flag(unittest.TestCase):
    def setUp(self):
        self.f  = Flag('TEST_FLAG')
        self.fd = FlagDigit('TEST_FLAG_DIGIT')

    def test_init(self):
        self.assertRaises(AssertionError, Flag, 'a')
        f = Flag('A')
        self.assertRaises(OSError, Flag, '***@$#%^&*(A_FDVFYJ3676VBBV')

    def test_set_state(self):
        self.f.state = 'test_flag_content'
        self.assertEqual(self.f.state, 'test_flag_content')

    def test_set_state_None(self):
        self.f.state = 'test_flag_content'
        self.f.state = None
        self.assertEqual(self.f.state, None)

    def test_check_state(self):
        self.f.state = 'test_flag_content'
        self.assertTrue(self.f.check_state())      
        self.f.state = None
        self.assertTrue(self.f.check_state())

    def test_check_state_create_checker(self): 
        self.fd.state = None
        self.assertTrue(self.fd.check_state())        
        self.fd.state = 1
        self.assertEqual(self.fd.state, '1')
        self.assertTrue(self.fd.check_state())        
        self.assertRaises(AssertionError, setattr, self.fd , 'state', 'asd')

    def tearDown(self):
        self.f.state = None
        unlink_if_file(self.f.path)
        self.fd.state = None
        unlink_if_file(self.fd.path)

if __name__ == '__main__':
    unittest.main()