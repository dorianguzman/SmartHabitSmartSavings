import os
import sys
import time
import csv
import math
import numpy as np

from matplotlib import pyplot as plt
import opt_habit

def analytics(nofhouseholds):
    """ Some simple middle school math to analyze our savings.
    """
    # household 0_0

#    dRegularRenewable = 38427.369411931846
#    dOptimizedRenewable = 37141.586356465545
#    dOptimizedDevices = 0

    dRegularRenewable = opt_habit.get_difference(nofhouseholds, 0)
    dOptimizedRenewable = opt_habit.get_difference(nofhouseholds, -12)
    dOptimizedDevices = 0

    one_percent  = dRegularRenewable / 100
    savings = abs(dOptimizedRenewable - dRegularRenewable) / one_percent

    return savings
    
    

if __name__ == '__main__':
    s = [100, 1000, 10000, 100000]
    a = [analytics(v) for v in s]

    print(a)
    sys.exit()

    plt.plot(s, a)
    plt.xlabel("Number of households")
    plt.ylabel("Percentage of savings")
    plt.title("Saving Potential by Number of Households.")
    plt.show()
