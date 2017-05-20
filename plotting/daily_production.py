import os
import sys
import time
import csv
import numpy as np
import matplotlib.pyplot as plt

sys.path.append('../io/')
import read_data 
import accumulate


def get_one_day(data, date, date_pos=0, data_pos=1, mult=1):
    """ Get one day of the data.

    Parameters
    ----------
    data : list
        one row is like [date, stuff, ...]
    date : string
        'dd.mm.yyyy'
    date_pos : int
        In what position of the row is the date? Default 0.
    data_pos : int
        In what position of the row is the data? Default 1.
    mult : int
        multiply data with a factor, e.g. 100 cause germany uses 'points'.

    Examples
    --------
    >>> data = read_data.read_csv("Netzeinspeisung_2013.csv", skip=5)
    >>> day_data = get_one_day(data, "01.01.2013", date_pos=0, data_pos=3)
    >>> day_data[0]
    12.361
    """
    nof_points = 96 # assuming data points for every 15 minutes.

    ret = np.zeros(nof_points)
    c = 0
    for row in data:
        if row[date_pos] == date:
            tmp = row[data_pos].replace(".","")
            ret[c] = float(tmp)
            c += 1
            if c == nof_points:
                break
    return ret

def plot_day(data):
    """ Plot data from one day.
    
    Notes
    -----
    Makes use of matplotlib.pyplot
    """
    plt.plot(data)


def production_data():
    """ This function plots a specific dataset:
    http://www.50hertz.com/en/Grid-Data/Photovoltaics/Archive-Photovoltaics

    Examples
    --------
    use with: <date> <Netzeinspeisung_2013> <Wind> <Solar>
    """
    # Netz
    data = read_data.read_csv(("/home/dutchman/Daten/2013_energy_feed_in/"
                               "Netzeinspeisung_2013.csv"),
                              skip=5)
    day_data = get_one_day(data, sys.argv[1], date_pos=0, data_pos=3,
                           mult=1000)

    day_data_set = []
    day_data_set.append(day_data)

    # Wind
    data = read_data.read_csv(("/home/dutchman/Daten/2013_energy_feed_in/"
                               "Windenergie_Hochrechnung_2013.csv"),
                               skip=5)
    day_data = get_one_day(data, sys.argv[1], date_pos=0, data_pos=3,
                           mult=1000)
    day_data_set.append(day_data)

    # Solar
    data = read_data.read_csv(("/home/dutchman/Daten/2013_energy_feed_in/"
                               "Solarenergie_Hochrechnung_2013.csv"),
                              skip=5)
    day_data = get_one_day(data, sys.argv[1], date_pos=0, data_pos=3)
    day_data_set.append(day_data)

    # Renewable
    day_data = day_data_set[1] + day_data_set[2]
    day_data_set.append(day_data)

    # plot data
    for d in day_data_set:
        plot_day(d)



def consumption_data(filename, nofhouseholds):
    """ This function plots a specific dataset:
    deb.org

    Notes
    -----
    Consumption data is in Watt, we need it in MWatt.
    That's why we multiply with 1000000.

    Examples
    --------
    use with: <date> <household>
    """
    data = filename

    consum = accumulate.accumulate_household(data)
    consum = consum / (1000000) * nofhouseholds

    plt.plot(consum)

    # plot devices
    devices = accumulate.accumulate_device(filename)
    for device_id in devices.keys():
        devices[device_id] =  devices[device_id] / (1000000) * nofhouseholds
        plt.plot(devices[device_id])


if __name__ == '__main__':
    # Plot production data
    production_data()

    # Plot consumption data
    consumption_data(("/home/dutchman/Daten/debs_challenge_2014/"
                      "debs_0_0.csv"), int(sys.argv[2]))

    plt.show()
