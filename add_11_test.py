import unittest
from ad_11 import counter

class Ad11Case(unittest.TestCase):
    # def test_input_1(self):
    #     self.assertEqual(counter(["ne","ne","ne"]), 3)

    def test_input_2(self):
        self.assertEqual(counter(["ne","ne","sw","sw"]), 0)

    # def test_input_3(self):
    #     self.assertEqual(counter(["ne","ne","s","s"]), 2)
    
    # def test_input_4(self):
    #     self.assertEqual(counter(["se","sw","se","sw","sw"]), 3)

if __name__ == '__main__':
    unittest.main()