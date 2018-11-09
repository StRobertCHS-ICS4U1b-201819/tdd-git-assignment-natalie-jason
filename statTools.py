def mean(myList):

    if(len(myList) < 1 ):
        return -1
    else:
        total = float(sum(myList))
        avg = total/len(myList)
        return (round(avg,3))


