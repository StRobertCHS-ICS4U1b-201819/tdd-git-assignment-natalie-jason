import pytest
import math
from statTools import *

def testmean1 ():
    assert(mean([]) == -1)

def testmean2 ():
    assert(mean([0, 9, 3]) == 4)

def testmean3 ():
    assert(mean([1,4,5,8,6, 11]) == 5.833)

def testmedian1 ():
    assert(median([]) == -1)

def testmedian2 ():
    assert(median([1,4,5]) == 4)

def testmedian3 ():
    assert(median([1, 6, 7, 9]) == 6.5)

def testlowquart1 ():
    assert(lower_quartile([]) == -1)

def testlowquart2 ():
    print(lower_quartile([6, 47, 49, 15, 43, 12]))