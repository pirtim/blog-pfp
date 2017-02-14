import unittest
# import blog-pfp.flags
# from flags import Flag
from blog_pfp.flags import Flag


class FlagDigit(Flag):
    @classmethod
    def _check_good_state(cls, state):
        print(str(state), flush=True)
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
        self.f.set_state('test_flag_content')
        self.assertEqual(self.f.get_state(), 'test_flag_content')

    def test_set_state_None(self):
        self.f.set_state('test_flag_content')
        self.f.set_state(None)
        self.assertEqual(self.f.get_state(), None)

    def test_check_good_state(self):
        self.f.set_state('test_flag_content')
        self.assertTrue(self.f.check_good_state())        
        self.f.set_state(None)
        self.assertTrue(self.f.check_good_state())

    def test_check_good_state_create_checker(self):
        self.fd.set_state(None)
        self.assertTrue(self.fd.check_good_state())        
        self.fd.set_state(1)
        self.assertEqual(self.fd.get_state(), '1')
        self.assertTrue(self.fd.check_good_state())        
        self.assertRaises(AssertionError, self.fd.set_state, 'asd')

    def tearDown(self):
        self.f.set_state(None)
        self.fd.set_state(None)

if __name__ == '__main__':
    unittest.main()