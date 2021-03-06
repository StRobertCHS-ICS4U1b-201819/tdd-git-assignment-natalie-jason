"""
------------------------------------------------------------------------------------------------------------------------
Name: test_statTools.py
Purpose:
    Test the functionality of the functions calculating the central tendencies and spread of a set of numerical data
    - mean, median, mode, range, upper quartile, lower quartile, variance, standard deviation
Authors: Ng.J, Tam.N
Created: 09/11/2018
------------------------------------------------------------------------------------------------------------------------
"""

import pytest
import math
from statTools import *

# Test Mean Function
# Basic Test Case #1: Just pass


def testmean1():
    assert(mean([0, 9, 3]) == 4)

# Basic Test Case #2: Decimal value


def testmean2 ():
    assert (mean([2, 6.5, -7.3, 23, -1.2, 8.6, -3]) == 4.086)

# Basic Test Case #3 : Illegal Case


def testmean3 ():
    assert(mean([]) == -1)

# Basic Test Case #4 : Wrong data type


def testmean4 ():
    with pytest.raises(TypeError) as datamsg:
        mean("Hello")
    assert ("Invalid input of a list" == str(datamsg.value))

# Basic Test #5 : Corner Case
def testmean5 ():
    assert (mean([6.8]) == 6.8)

    # Test Median Function
# Basic Test Case #1: Illegal Case


def testmedian1 ():
    assert(median([]) == -1)

# Basic Test Case #2: Just pass


def testmedian2 ():
    assert(median([1,4,5]) == 4)

# Basic Test Case #3: Decimal value/ Exhaustive Case


def testmedian3 ():
    assert(median([1, 6, 7, 9, 34, 23, 67, 96, 45, 23, 78, 334]) == 28.5)

# Basic Test Case #4: Corner Case

def testmedian4 ():
    assert (median([5.4]) == 5.4)

# Basic Test Case #5 : Wrong data type


def testmedian5 ():
    with pytest.raises(TypeError) as datamsg:
        median("Hello")
    assert ("Invalid input of a list" == str(datamsg.value))

    # Test Lower Quartile Function
# Basic Test Case #1: Illegal Case - No values in list

# Test Mode

def test_mode1():
    assert(mode([1, 2, 4, 5, 4, 6, 5, 6, 2, 5, 6, 3, 6]) == 6)

def test_mode2():
    assert(mode([]) == None)

def test_mode3():
    assert(mode([15, 763, 34, 2, 62, 73, 245, 763]) == 763)

def test_mode4():
    assert(mode([0]) == 0)

# Test Range Function

def test_range_1():
    assert(range([1,2,3,4,24,537,37,16, 4]) == 536)

def test_range_2():
    assert(range([11,15,16,5,28,64,845,82,25]) == 840)

def test_range_3():
    with pytest.raises(ValueError) as valerror:
        range([])
    assert ("No Data Provided" == str(valerror.value))

#Test lower quartile

def testlowquart1 ():
    assert(lower_quartile([]) == -1)

# Basic Test Case #2 : Illegal Case - Wrong data type


def testlowquart2 ():
    with pytest.raises(TypeError) as datamsg:
        lower_quartile("23")
    assert ("Invalid input of a list" == str(datamsg.value))

# Basic Test Case #3 : Just Pass


def testlowquart3 ():
    assert(lower_quartile([5, 15, 23, 25, 27, 28, 40]) == 15)

# Basic Test Case #4 : Exhaustive Case


def testlowquart4 ():
    assert(lower_quartile([6, 47, 49, 15, 43, 41, 7, 39, 43, 41, 36]) == 15)

# Basic Test Case #5 : Corner Case

def testlowquart5 ():
    assert(lower_quartile([1, 2, 5, 8]) == 2)

    # Test Higher Quartile Function
# Basic Test Case #1 : Illegal Case - No Values


def testhighquart1 ():
    assert(upper_quartile([]) == -1)

# Basic Test Case #2 : Illegal Case - No Values


def testhighquart2 ():
    with pytest.raises(TypeError) as datamsg:
        upper_quartile("23")
    assert ("Invalid input of a list" == str(datamsg.value))

# Basic Test Case #3 : Corner Case


def testhighquart3 ():
    assert(upper_quartile([1, 2, 6, 7]) == 6)

# Basic Test Case #4 : Exhaustive Case
# sorted list is [1, 11, 15, 19, 20, 24, 28, 34, 37, 44, 47, 50, 57]


def testhighquart4 ():
    assert(upper_quartile([34, 47, 1, 15, 99, 24, 20, 11, 19, 50, 28, 37, 44]) == 44)

# Basic Test Case #5 : Exhaustive Case 2

def testhighquart5 ():


    assert(upper_quartile([2, 5, 5, 6, 7, 7, 8, 9]) == 7.5)


# Test Variance

def test_variance1():
    assert(variance([1, 2, 3, 4, 5, 6, 7, 8,9]) == 6.0000)

def test_variance2():
    assert(variance([0]) == 0)

def test_variance3():
    assert(variance([14, 72, 25, 73, 84, 34, 74, 16]) == 758.0000)

def test_variance4():
    assert(variance([]) == None)


# Test Standard Deviation Function


def test_standard_deviation1():
    assert(standardDeviation([1, 2, 3, 4, 5, 6, 7, 8,9]) == 2.4495)

def test_standard_deviation2():
    assert(standardDeviation([0]) == 0)

def test_standard_deviation3():
    assert(standardDeviation([14, 72, 25, 73, 84, 34, 74, 16]) == 27.5318)

def test_standard_deviation4():
    assert(standardDeviation([]) == None)
