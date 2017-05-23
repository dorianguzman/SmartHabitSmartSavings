import os
import sys
import unittest
import numpy as np

sys.path.append('../plotting/')
import opt_habit

class accumulate_test(unittest.TestCase):

    def test_target_function(self):
        R = np.ones(96)
        C = np.ones(96)

        t = opt_habit.target_function(R, C)
        self.assertEqual(t, 0)

if __name__ == '__main__':
    unittest.main() 
