#Testing file
import unittest
#now import either the working file OR function
#OR import main
import test_function

#create a class and name it whatever desired
class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = test_function.do_stuff(test_param)
    self.assertEqual(result, 15)

unittest.test_function()