import pytest
from statTools import *

# Test Mean Function
    # Basic Test Case #1: Illegal Case
def testmean1 ():
    assert(mean([]) == -1)

def testmean2 ():
    assert(mean([0, 9, 3]) == 4)

def testmean3 ():
    assert(mean([1,4,5,8,6, 11]) == 5.833)


rangeList1 = [1,2,3,4,24,537,37,16, 4]
rangeList2 = [11,15,16,5,28,64,845,82,25]
rangeList3 = []

def test_range_1():
    assert(range(rangeList1) == 536)

def test_range_2():
    assert(range(rangeList2) == 840)

def test_range_3():
    with pytest.raises(ValueError) as valerror:
        range(rangeList3)
    assert ("No Data Provided" == str(valerror.value))

