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
    """ Calculate the mean value from a set of numbers.
       :param myList: (list) The list of numbers
       :return: (float) The mean value of the numbers in the list

    """

    # Check if there are numbers in the list, return -1 if there are none

    if len(myList) < 1:
        return -1

    # Raises an error if the input is not a list

    elif type(myList) != list:
        raise TypeError("Invalid input of a list")

    else:
        # Find float value of sum of list
        total = float(sum(myList))
        # Find average
        avg = total/len(myList)
        # Round average to 3 decimal places
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

    """ Finds the median from a list of numbers
       :param myList: (list) List of numbers
       :return: (float) The median value from the list of numbers
    """

    # Raises an error if the input is not a list
    if type(myList) != list:
        raise TypeError("Invalid input of a list")

    # Sort list from smallest to largest
    myList.sort()
    first = 0
    last = len(myList) - 1
    # Find median position
    mid = (first + last) // 2
    median = 0.0

    # Case where there are 2 medians, and an average must be calculated

    if len(myList) % 2 == 0:
        median = (myList[mid] + myList[mid + 1]) / 2.0
        return median

    # Case where this is only 1 median
    else:
        median = (myList[mid])
        return float(median)


"""
-------------------------------------------------------------------------------
Name:		lower_quartile.py
Purpose:		
To find the lower quartile value from a list of numbers
Author:		Tam.N

Created:		09/11/2018
------------------------------------------------------------------------------
"""


def lower_quartile(myList):
    """ To determine the lower quartile value from a list of numbers
       :param myList: (list) The numbers in a list
       :return: (float) The lower quartile value from a list of numbers, the median
       of the lower half set of the data set
    """

    # Raises an error if the input is not a list
    if type(myList) != list:
        raise TypeError("Invalid input of a list")

    # Sort list from smallest to largest
    myList.sort()
    first = 0
    # Find position of the middle of the list
    mid = (first + (len(myList) - 1)) // 2
    median = 0.0

    # Create lower half set of the data set
    newList = myList[:mid]
    lastNew = len(newList) - 1
    newMed = (first + lastNew) // 2

    # Handling case with less than 4 values
    if len(myList) < 4:
        return -1

    # Case where there are only 4 values
    elif len(myList) == 4:
        return myList[0]

    # Case for even list
    elif len(myList) % 2 == 0:
        median = (newList[newMed] + newList[newMed + 1]) / 2.0
        return median

    # Case for odd list
    else:
        median = (newList[newMed])
        return median


"""
-------------------------------------------------------------------------------
Name:		upper_quartile.py
Purpose:		
To find the upper quartile value from a list of numbers
Author:		Tam.N

Created:		10/11/2018
------------------------------------------------------------------------------
"""


def upper_quartile (myList):
    """ To determine the upper quartile value from a list of numbers
       :param myList: (list) The numbers in a list
       :return: (float) The higher quartile value from a list of numbers, the median
       of the upper half set of the data set
    """

    # Raises an error if the input is not a list

    if type(myList) != list:
        raise TypeError("Invalid input of a list")

    # Sort list from smallest to largest value
    myList.sort()

    # Create variables for positions in the list
    first = 0
    mid = (first + (len(myList) - 1)) // 2
    newList = myList[mid:]
    median = 0.0

    # Handling case when there are less than 4 values, return -1
    if len(myList) < 4:
        return -1

    # Handling case when there are 4 values, return the 3rd number in the list
    elif len(myList) == 4:
        return myList[2]

    # Handling case when there are an even amount of values in the list
    elif len(myList) % 2 == 0:
        median = (newList[(first + len(newList)) // 2] + newList[((first + len(newList)) // 2) + 1]) / 2.0
        return median

    # Handling case when there are an odd number of values in the list
    else:
        median = newList[(first + len(newList)) // 2]
        return median
