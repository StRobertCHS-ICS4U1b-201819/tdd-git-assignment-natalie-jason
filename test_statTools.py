import pytest
from statTools import *

# Test Mean Function

def testmean1():
    assert(mean([]) == -1)

def testmean2():
    assert(mean([0, 9, 3]) == 4)

def testmean3():
    assert(mean([1,4,5,8,6, 11]) == 5.833)

# Test Range Function

def test_range_1():
    assert(range([1,2,3,4,24,537,37,16, 4]) == 536)

def test_range_2():
    assert(range([11,15,16,5,28,64,845,82,25]) == 840)

def test_range_3():
    with pytest.raises(ValueError) as valerror:
        range([])
    assert ("No Data Provided" == str(valerror.value))

# Test Standard Deviation Function

def test_standard_deviation1():
    assert(standardDeviation(1,2,3,4,5,6,7,8,9) == 2.2913)

def test_standard_deviation2():
    assert(standardDeviation([0]) == 0)

def test_standard_deviation3():
    assert(standardDeviation([14,72,25,73,84,34,74,16]) == 27.5454)