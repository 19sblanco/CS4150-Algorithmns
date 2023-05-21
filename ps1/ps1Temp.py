import random
import math

class Tests:

    def __init__():
        pass

    def ParitionTest1():
        array = [1, 6, 3, 9, 2, 7, 4, 1]
        parition = 3

        test = Partition(array, parition)
        print(test)

    def ParitionTest2():
        array = [1, 6, 3, 9, 2, 7, 4, 1, 4]
        parition = 4

        test = Partition(array, parition)
        print(test)


    def MedianTest2():
        array = [1, 6, 3, 9, 2, 7, 4, 1, 10]
        array.sort()
        print("sorted array", array)
        print("5th element of array", BruteForceGrabK(array, 5))

    def SplitTest1():
        array = [1, 6, 3, 9, 2, 7, 4, 1, 10]
        A = splitArrays(array, 4)
        print(A)

    def SplitTest2():
        array = [1, 6, 3, 9, 2, 7, 4, 1, 10]
        A = splitArrays(array, 5)
        print(A)

    def MomSelectTest1():
        array = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27)]
        midpoint = math.floor(len(array)/2)
        median = MomSelect(array, midpoint)
        print(median)

    def MomSelectTest2():
        array = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27)]
        random.shuffle(array)
        k = 26
        kthElement = MomSelect(array, k)
        print(str(k) + "th element", kthElement)


    def weightedMedianTest1():
        players = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24), (24, 25), (25, 26), (26, 27)]
        random.shuffle(players)
        refID = WeightedMedian(players)
        print(refID)




"""
get the kth element of an array
"""
def BruteForceGrabK(array, k):
    if len(array) == 0:
        return None

    array.sort()
    while array[k] == (-1, -1): # if K is a place holder value, iterate till its not
        k += 1

    return array[k]


"""
split a given array into arrays of size N contained within a container list (lst)
if the last list cannot be fully filled it will be filled with -1's
"""
def splitArrays(array, n):
    numberOfSubArrays = math.ceil(len(array) / n)

    lst = [0] * numberOfSubArrays
    for i in range(numberOfSubArrays):
        temp = [0] * n

        for j in range(n):
            id = i * n + j
            if id < len(array):
                temp[j] = array[id]
            else:
                temp[j] = (-1, -1) # place holder values
        lst[i] = temp
    
    return lst



"""
put all elements less than the parition left of it
and all the elements more than the paritiion right of it and return that arra
also return the index of the partition
"""
def Partition(players, partition):
    smallerArray = []
    partitionArray = []
    biggerArray = []
  
    for element in players: 
        if element[0] < partition[0]:
            smallerArray.append(element)
        elif element[0] > partition[0]:
            biggerArray.append(element)
        else:
            partitionArray.append(element)

    # return len(smallerArray) # this will give the position of the partition
    partitionIdx = len(smallerArray)
    players = smallerArray + partitionArray + biggerArray
    return (partitionIdx, players)

    
"""
basically quick select but we pick a good pivot with
the help of mom allowing for O(n) time :D
"""
def MomSelect(players, k):
    if len(players) <= 25:
        return BruteForceGrabK(players, k)
        
    else:
        arraysOfFive = splitArrays(players, 5)

        arrayOfMediansOfFive = []

        for array in arraysOfFive:
            medianOfFive = BruteForceGrabK(array, 2) # two is used because we want the median of an array of size 5
            arrayOfMediansOfFive.append(medianOfFive)
        
        midpoint = getMidPoint(arrayOfMediansOfFive)
        mom = MomSelect(arrayOfMediansOfFive, midpoint)

        temp = Partition(players, mom)
        partitionIndex = temp[0]
        players = temp[1]

        if k < partitionIndex:
            return MomSelect(players[:partitionIndex], k)
        elif k > partitionIndex:
            return MomSelect(players[partitionIndex + 1:], k - partitionIndex -1)
        else:
            return mom
        


"""
count the weights in a given array 
weights are numbers in the array
"""
def countWeights(players):
    sum = 0
    for player in players:
        weight = player[1]
        sum += weight
    
    return sum

def getMidPoint(array):
    return int(len(array) // 2)


def WeightedMedian(players):
    totalWeight = countWeights(players)
    threshold = totalWeight / 2
    return WeightedMedianRecursion(threshold, players, 0, 0)


def WeightedMedianRecursion(threshold, players, totalLeft, totalRight):
    midpoint = getMidPoint(players)
    copyArray = players[:]
    pivot = MomSelect(copyArray, midpoint) # note the pivot is the median of the current array/subarray we are working with
    
    temp = Partition(players, pivot)
    pivotIdx = temp[0]
    players = temp[1]

    leftArray = players[:pivotIdx]
    rightArray = players[pivotIdx +1:]

    weightLeftOfPiv = countWeights(leftArray) + totalLeft
    weightRightOfPiv = countWeights(rightArray) + totalRight

    if weightLeftOfPiv <= threshold and weightRightOfPiv <= threshold:
        return players[pivotIdx][0]
    elif weightLeftOfPiv > weightRightOfPiv:
        return WeightedMedianRecursion(threshold, leftArray, totalLeft, weightRightOfPiv + pivot[1])
    else:
        return WeightedMedianRecursion(threshold, rightArray, weightLeftOfPiv + pivot[1], totalRight)


def main():
    number_of_players = int(input())

    playerIds = [int(x) for x in input().split()]
    playerWeights = [int(x) for x in input().split()]

    # pair players with their weights
    players = []
    for i in range(number_of_players):
        id = playerIds[i]
        weight = playerWeights[i]
        players.append((id, weight))


    refID = WeightedMedian(players)

    print(refID)


main()

# t = Tests
# t.weightedMedianTest1()



