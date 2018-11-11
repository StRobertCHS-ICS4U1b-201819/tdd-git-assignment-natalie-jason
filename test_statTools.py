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
    assert(standardDeviation([1, 2, 3, 4, 5, 6, 7, 8,9]) == 2.4495)

def test_standard_deviation2():
    assert(standardDeviation([0]) == 0)

def test_standard_deviation3():
    assert(standardDeviation([14, 72, 25, 73, 84, 34, 74, 16]) == 27.5318)

def test_standard_deviation4():
    assert(standardDeviation([]) == None)

# Test Variance

def test_variance1():
    assert(variance([1, 2, 3, 4, 5, 6, 7, 8,9]) == 6.0000)

def test_variance2():
    assert(variance([0]) == 0)

def test_variance3():
    assert(variance([14, 72, 25, 73, 84, 34, 74, 16]) == 758.0000)

def test_variance4():
    assert(variance([]) == None)


# Test Mode

def test_mode1():
    assert(mode([1, 2, 4, 5, 4, 6, 5, 6, 2, 5, 6, 3, 6]) == 6)

def test_mode2():
    assert(mode([]) == None)

def test_mode3():
    assert(mode([15, 763, 34, 2, 62, 73, 245, 763]) == 763)

def test_mode2():
    assert(mode([0]) == 0)