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

    # raises an error if the list doesn't have any values
    if len(rangeList) == 0:
        raise ValueError("No Data Provided")

    # sorts the list in order of increasing value, find range by subtracting the last value to the first value (larges # - smallest #)
    try:
        rangeList.sort()
        realRange = rangeList[len(rangeList) - 1] - rangeList[0]
        return round(realRange, 2)

    # excepts error in an invalid list is given
    except TypeError:
        raise TypeError("Invalid List Provided")
