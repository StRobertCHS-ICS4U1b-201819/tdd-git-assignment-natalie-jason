
import pytest
from statTools import *

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

