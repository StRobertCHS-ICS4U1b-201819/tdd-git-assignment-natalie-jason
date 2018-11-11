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

import math

def mean(myList):
    """ Calculate the mean value from a set of numbers.
       :param myList: (list) The list of numbers
       :return: (float) The mean value of the numbers in the list
    """

    # Check if there are numbers in the list, return -1 if there are none

    if len(myList) < 1:
        return -1

    else:

        # Find float value of sum of list
        total = float(sum(myList))

        # Find average
        avg = total/len(myList)

        # Round average to 3 decimal places
        return round(avg, 3)

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


def standardDeviation(myList):
    '''Given a list of numbers, return the standard deviation of that list

    :param myList: list of numbers
    :return: returns the standard deviation of a list of numbers
    '''

    # If there aren't any numbers in the list, return None
    if len(myList) == 0:
        return None

    # If the "list" given is not a list, raise a type error
    if type(myList) != list:
        raise TypeError("input must be a list")

    # If the list of numbers is a normal list or numbers, run the code to correctly calculate the standard deviation
    else:
        avg = sum(myList) / len(myList)
        total = 0
        for items in myList:
            total += (avg - items) * (avg - items)
        return round(math.sqrt(total / len(myList)), 4)

def variance(myList):
    '''Given a list of numbers, return the variance of that list

    :param myList: list of numbers
    :return: variance of a list of numbers
    '''

    if len(myList) == 0:
        return None

    if type(myList) != list:
        raise TypeError("input must be a list")

    else:
        avg = sum(myList) / len(myList)
        total = 0
        for items in myList:
            total += (avg - items) * (avg - items)
        return round((total / len(myList)), 4)

