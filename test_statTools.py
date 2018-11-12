import pytest
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
    assert(median([1, 4, 5]) == 4)

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


def testhighquart1():
    assert(upper_quartile([]) == -1)

# Basic Test Case #2 : Illegal Case - No Values


def testhighquart2():
    with pytest.raises(TypeError) as datamsg:
        upper_quartile("Billy Jean")
    assert ("Invalid input of a list" == str(datamsg.value))

# Basic Test Case #3 : Corner Case


def testhighquart3():
    assert(upper_quartile([1, 2, 6, 7]) == 6)

# Basic Test Case #4 : Exhaustive Case
# sorted list is [1, 11, 15, 19, 20, 24, 28, 34, 37, 44, 47, 50, 57]


def testhighquart4():
    assert(upper_quartile([34, 47, 1, 15, 99, 24, 20, 11, 19, 50, 28, 37, 44]) == 44)

# Basic Test Case #5 : Exhaustive Case 2


def testhighquart5():

    assert(upper_quartile([2, 5, 5, 6, 7, 7, 8, 9]) == 7.5)

#Basic Test Case #6 : One Value
def testhighquart6():

    print(upper_quartile([1]) == -1)


