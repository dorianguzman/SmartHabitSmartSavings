import os
import sys
import time
import csv
import numpy as np

def time_to_slot(hh,mm):
    """ Split the time steps within one day into 96 different slots.

    Parameters
    ----------
    hh : hour
    mm : minute

    Notes
    -----
    The time taken for a slot is 15' step
    """
    hour_slot = hh*4
    minute_slot = 0
    if mm <= 14:
        minute_slot = 1
    elif mm <= 29 and mm >=15:
        minute_slot = 2
    elif mm <= 44 and mm >=30:
        minute_slot = 3
    elif mm >= 45 and mm <=60:
        minute_slot = 4
    else:
        print("Minute value incorrect, please check it")

    timeslot = hour_slot + minute_slot
    return timeslot
        
if __name__ == '__main__':
    times = time_to_slot( 2, 15)
    print(times)
