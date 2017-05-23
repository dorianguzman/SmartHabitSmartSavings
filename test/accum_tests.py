import os
import sys
import unittest
import numpy as np

sys.path.append('../plotting/')
import accumulate

class accumulate_test(unittest.TestCase):

    def test_total_consumption(self):
        consumption = np.ones(96)
        t = accumulate.total_consumption(consumption)

        self.assertEqual(t, 96)

if __name__ == '__main__':
    unittest.main() 
