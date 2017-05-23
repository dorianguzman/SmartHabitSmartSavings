import os
import sys
import time
import csv
import numpy as np
#from matplotlib import pyplot as plt

def read_csv(filename, skip=0, delimiter=';'):
    """ Read csv file and returns list.

    Parameters
    ----------
    filename : string
    skip : int
        how many header files shall be skipped. Default 0

    Examples
    --------
    >>> data = read_csv("Netzeinspeisung_2013.csv", skip=5)
    >>> data[0]
    [01.01.2013', '00:00', '00:15', '12.361', '']
    """
    c = 0
    ret = []
    with open(filename,'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        for row in reader:
            if c < skip:
                c += 1
                continue
            ret.append(row)
    return ret

def epoch_to_datetime(seconds):
    """ Returns time object.

        Examples
        --------
        >>> import read_data
        >>> d = read_data.epoch_to_datetime(1379879533)
        >>> d.tm_year
        2013
        >>> d.tm_mon
        9
        >>> d.tm_mday
        22
        >>> d.tm_hour
        19
        >>> d.tm_min
        52
        >>> d.tm_sec
        13
    """
    return time.gmtime(seconds)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("__main__ reads csv file. (fow now =) )")
        sys.exit()
    data = read_csv(sys.argv[1], delimiter=",")

    wf = open('tdebs.csv', 'w')
    writer = csv.writer(wf, delimiter=",")
    for row in data:
        tt = epoch_to_datetime(int(row[1]))
        row[1] = "%d.%d.%d.%d.%d"%(tt.tm_mon, tt.tm_mday, tt.tm_hour,
                                tt.tm_min, tt.tm_min)
        writer.writerow(row)

