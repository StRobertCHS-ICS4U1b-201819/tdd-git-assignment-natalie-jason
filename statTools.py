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
    rangeList.sort()
    return rangeList[len(rangeList) - 1] - rangeList[0]
