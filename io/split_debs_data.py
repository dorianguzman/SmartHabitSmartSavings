import os
import sys
import time
import csv
import numpy as np

def split_data(filename, house_id, household_id,
               skip=0, delimiter=','):
    """ Split debs dataset into 'workable' chunks.

    Parameters
    ----------
    filename : string
    house_id : int
    household_id : int

    Notes
    -----
    Information about the data is available at
    debs.org/?p=75
    """

    c = 0
    ret = []

    write_file = open("debs_%d_%d.csv", "wb")
    writer = csv.writer(write_file, delimiter=";")

    with open(filename,'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=delimiter)
        for row in reader:
            rid = row[0]
            rtimestamp = row[1]
            rvalue = row[2]
            rproperty = row[3]
            rplug_id = row[4]
            rhousehold_id = row[5]
            rhouse_id = row[6]

            if (rhouse_id == house_id and
               rhousehold_id == household_id):
                writer.writerow(row)

if __name__ == '__main__':
    split_data(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))
