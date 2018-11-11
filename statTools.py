"""
-------------------------------------------------------------------------------
Name:		mean.py
Purpose:
To return the mean/average of the list of numbers back to the user

Author:		Tam.N

Created:		08/11/2018
------------------------------------------------------------------------------
"""


def mean(myList):

    if len(myList) < 1:
        return -1
    else:
        total = float(sum(myList))
        avg = total/len(myList)
        return round(avg, 3)


"""
-------------------------------------------------------------------------------
Name:		median.py
Purpose:		
To return the median of a list of numbers back to the user

Author:		Tam.N

Created:		09/11/2018
------------------------------------------------------------------------------
"""


def median(myList):
    myList.sort()
    first = 0
    last = len(myList) - 1
    mid = (first + last) // 2
    median = 0.0

    if len(myList) % 2 == 0:
        median = (myList[mid] + myList[mid + 1]) / 2.0
        return median

    else:
        median = (myList[mid])
        return float(median)


"""
-------------------------------------------------------------------------------
Name:		<filename>.py
Purpose:		
<a description of your program>

Author:		Tam.N

Created:		09/11/2018
------------------------------------------------------------------------------
"""


def lower_quartile(myList):
    # sort list
    # find the median,name that mid
    # find median of lower list

    myList.sort()
    first = 0
    mid = (first + (len(myList) - 1)) // 2
    median = 0.0

    newList = []
    newList = myList[:mid]
    lastNew = len(newList) - 1
    newMed = (first + lastNew) // 2

    if len(myList) == 0:
        return -1

    elif len(myList) == 4:
        return myList[0]

    elif len(myList) % 2 == 0:
        median = (newList[newMed] + newList[newMed + 1]) / 2.0
        return median

    else:
        median = (newList[newMed])
        return median


"""
-------------------------------------------------------------------------------
Name:		<filename>.py
Purpose:		
<a description of your program>

Author:		Tam.N

Created:		09/11/2018
------------------------------------------------------------------------------
"""


def upper_quartile (myList):
    myList.sort()

    first = 0
    mid = (first + (len(myList) - 1)) // 2
    newList = myList[mid:]
    median = 0.0

    if len(myList) == 0:
        return -1

    elif len(myList) == 4:
        return myList[2]

    elif len(myList) % 2 == 0:
        median = (newList[(first + len(newList)) // 2] + newList[((first + len(newList)) // 2) + 1]) / 2.0
        return median

    else:
        median = newList[(first + len(newList)) // 2]
        return median

def sorted(myList):
    myList.sort()
    return myList