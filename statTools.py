def mean(myList):

    if(len(myList) < 1 ):
        return -1
    else:
        total = float(sum(myList))
        avg = total/len(myList)
        return (round(avg,3))

def median(myList):
    myList.sort()
    first = 0
    last = len(myList) -1
    mid = (first + last) // 2
    median = 0.0

    if len(myList) % 2 == 0:
        median = (myList[mid] + myList[mid + 1]) / 2.0
        return median




