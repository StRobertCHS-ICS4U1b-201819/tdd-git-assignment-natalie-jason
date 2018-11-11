import pytest
import math
from statTools import *

    # Test Mean Function
    # Basic Test Case #1: Illegal Case
def testmean1 ():
    assert(mean([]) == -1)

def testmean2 ():
    assert(mean([0, 9, 3]) == 4)

def testmean3 ():
    assert(mean([1,4,5,8,6, 11]) == 5.833)

    # Test Median Function
    # Basic Test Case #1: Illegal Case
def testmedian1 ():
    assert(median([]) == -1)

def testmedian2 ():
    assert(median([1,4,5]) == 4)

def testmedian3 ():
    assert(median([1, 6, 7, 9]) == 6.5)

    # Test Higher Quartile Function
    # test for illegal case
def testlowquart1 ():
    assert(lower_quartile([]) == -1)

def testlowquart2 ():
    assert(lower_quartile([6, 12, 15, 43, 47, 49]) == 9)

def testlowquart3 ():
    assert(lower_quartile([5, 15, 23, 25, 27, 28, 40]) == 15)

def testlowquart4 ():
    assert(lower_quartile([6, 47, 49, 15, 43, 41, 7, 39, 43, 41, 36]) == 15)

def testlowquart5 ():
    assert(lower_quartile([34, 47, 1, 15, 57, 24, 20, 11, 19, 50, 28, 37]) == 17)

def testlowquart6 ():
    assert(lower_quartile([1, 2, 5, 8]) == 2)

    # test cases for higher quartile function
    # test for illegal case
def testhighquart1 ():
    assert(upper_quartile([]) == -1)

def testhighquart2 ():
    assert(upper_quartile([1,2,6,7]) == 6)

# sorted list is [1, 11, 15, 19, 20, 24, 28, 34, 37, 44, 47, 50, 57]
def testhighquart3 ():
    assert(upper_quartile([34, 47, 1, 15, 57, 24, 20, 11, 19, 50, 28, 37, 44]) == 44)

def testhighquart4 ():
    assert(upper_quartile([2, 4, 4, 5, 6, 7, 8]) == 7)

def testhighquart5 ():
    assert(upper_quartile([2, 5, 5, 6, 7, 7, 8, 9]) == 7.5)

def testdkjkd ():
    print(sorted([34, 47, 1, 15, 57, 24, 20, 11, 19, 50, 28, 37, 44]))

