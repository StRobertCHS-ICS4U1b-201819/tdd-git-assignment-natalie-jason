"""
------------------------------------------------------------------------------------------------------------------------
Name: statTools.py
Purpose:
    Collection of functions calculating the central tendencies and spread of a set of numerical data
    - mean, median, mode - range, upper quartile, lower quartile, variance, standard deviation
Authors: Ng.J, Tam.N
Created: 11/09/2018
------------------------------------------------------------------------------------------------------------------------
"""

def range(rangeList):
    ''' Given a list, returns the range of the list

    :param rangeList: list of numbers
    :return: Range of the list
    '''

    if len(rangeList) == 0:
        raise ValueError("No Data Provided")
    try:
        rangeList.sort()
        realRange = rangeList[len(rangeList) - 1] - rangeList[0]
        return round(realRange, 2)
    except TypeError:
        raise TypeError("Invalid List Provided")
