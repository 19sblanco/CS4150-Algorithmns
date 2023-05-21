import math
# import random

# class Tests:
#     def __init__():
#         pass

#     def ParitionTest1():
#         array = [1, 6, 3, 9, 2, 7, 4, 1]
#         parition = 3

#         test = Partition(array, parition)
#         print(test)

#     def ParitionTest2():
#         array = [1, 6, 3, 9, 2, 7, 4, 1, 4]
#         parition = 4

#         test = Partition(array, parition)
#         print(test)

#     def MedianTest1():
#         array = [1, 6, 3, 9, 2, 7, 4, 1]
#         midpoint = math.floor(len(array)/2)
#         array.sort()
#         print("sorted array", array)
#         print("median of array", BruteForceGrabK(array, midpoint))

#     def MedianTest2():
#         array = [1, 6, 3, 9, 2, 7, 4, 1, 10]
#         array.sort()
#         print("sorted array", array)
#         print("5th element of array", BruteForceGrabK(array, 5))

#     def SplitTest1():
#         array = [1, 6, 3, 9, 2, 7, 4, 1, 10]
#         A = splitArrays(array, 4)
#         print(A)

#     def SplitTest2():
#         array = [1, 6, 3, 9, 2, 7, 4, 1, 10]
#         A = splitArrays(array, 5)
#         print(A)

#     def MomSelectTest1():
#         array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#         midpoint = math.floor(len(array)/2)
#         median = MomSelect(array, midpoint)
#         print(median)

#     def MomSelectTest2():
#         array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#         random.shuffle(array)
#         k = 26
#         kthElement = MomSelect(array, k)
#         print(str(k) + "th element", kthElement)

#     def MomSelectTest3():
#         array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27]
#         random.shuffle(array)
#         k = 16
#         kthElement = MomSelect(array, k)
#         print(str(k) + "th element", kthElement)




"""
get the kth element of an array
"""
def BruteForceGrabK(array, k):
    if len(array) == 0:
        return None

    array.sort()
    while array[k] == -1:
        k += 1

    return array[k]


"""
split a given array into arrays of size N contained within a container list (lst)
if the last list cannot be fully filled it will be filled with -1's
"""
def splitArrays(array, n):
    numberOfSubArrays = math.ceil(len(array) / n)

    lst = []
    for i in range(numberOfSubArrays):
        temp = []

        for j in range(n):
            id = i * n + j
            if id < len(array):
                temp.append(array[id])
            else:
                temp.append(-1) # just some place holder value
        lst.append(temp)

    return lst




"""
put all elements less than the parition left of it
and all the elements more than the paritiion right of it and return that arra
also return the index of the partition
"""
def Partition(arrayW, arrayS, partition):
    smallerArrayW = []
    biggerArrayW = []
    partitionArrayW = []

    smallerArrayS = []
    biggerArrayS = []
    partitionArrayS = []
    for element in arrayW: 
        if element < partition:
            smallerArrayW.append(element)
            smallerArrayS.append(element)
        elif element > partition:
            biggerArrayW.append(element)
            biggerArrayS.append(element)
        else:
            partitionArrayW.append(element)
            partitionArrayS.append(element)

    # return len(smallerArray) # this will give the position of the partition
    return (len(smallerArrayW), smallerArrayW + partitionArrayW + biggerArrayW, smallerArrayS + partitionArrayS + biggerArrayS)

    
"""
basically quick select but we pick a good pivot with
the help of mom allowing for O(n) time :D
"""
def MomSelect(arrayW, k, arrayS):
    copyArray = arrayW[:]
    if len(arrayW) <= 25:
        return BruteForceGrabK(copyArray, k)
        
    else:
        """
        split array into arrays of size 5, if not perfect cut, fill with -1's

        for each split array:
            calculate the median
            put into M
        mom = MomSelect(M, len(M) / 2)
        """
        arraysOfFive = splitArrays(copyArray, 5)

        arrayOfMediansOfFive = []

        for arrayW in arraysOfFive:
            medianOfFive = BruteForceGrabK(arrayW, 2) # two is used because we want the median of an array of size 5
            arrayOfMediansOfFive.append(medianOfFive)
        
        midpoint = math.floor(len(arrayOfMediansOfFive) / 2)
        mom = MomSelect(arrayOfMediansOfFive, midpoint)

        """
        r = parition(array, mom)

        if k < r:
            return momselect(array till r-1, k)
        elif if k > r
            return momselect(array after r+1, k-r)
        else
            return mom
        """
        temp = Partition(arrayW, mom, arrayS)
        partitionIdx = temp[0]
        partitionedArrayW = temp[1]
        partitionedArrayS = temp[2]

        if k < partitionIdx: # check this part for off by one errors
            return MomSelect(partitionedArrayW[:partitionIdx], k, partitionedArrayS[:partitionIdx])
        elif k > partitionIdx:
            return MomSelect(partitionedArrayW[partitionIdx +1:], k - partitionIdx -1, partitionedArrayW[partitionIdx +1:])
        else:
            return mom


"""
count the weights in a given array 
weights are numbers in the array
"""
def countWeights(array):
    sum = 0
    for num in array:
        sum += num
    
    return sum


def WeightedMedian(weightArray, idsArray):
    totalWeight = countWeights(weightArray)
    return WeightedMedianRecursion(totalWeight, weightArray, 0, 0, idsArray)

def getMidPoint(array):
    if len(array) == 2:
        return 0

    return math.floor(len(array) / 2)
    

def WeightedMedianRecursion(totalWeight, weightArray, totalLeft, totalRight, idsArray):
    midpoint = getMidPoint(weightArray)
    pivot = MomSelect(weightArray, midpoint, idsArray) # note the pivot is the median of the current array/subarray we are working with

    pivotIdx = weightArray.index(pivot)
    leftWArray = weightArray[:pivotIdx]
    rightWArray = weightArray[pivotIdx + 1:]
    leftIDArray = idsArray[:pivotIdx]
    rightIDArray = idsArray[pivotIdx + 1:]

    lweight = countWeights(leftWArray)
    rweight = countWeights(rightWArray)

    weightLeftOfPiv = totalLeft + lweight
    weightRightOfPiv = totalRight + rweight

    halfTotalWeight = totalWeight / 2

    if weightLeftOfPiv <= halfTotalWeight and weightRightOfPiv <= halfTotalWeight:
        return idsArray[pivotIdx]
    elif weightLeftOfPiv > weightRightOfPiv:
        return WeightedMedianRecursion(totalWeight, leftWArray, totalLeft, weightRightOfPiv + pivot, leftIDArray)
    else:
        return WeightedMedianRecursion(totalWeight, rightWArray, weightLeftOfPiv + pivot, totalRight, rightIDArray)


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
    
    # sort players by id, and sort weights accordingly
    
    """
    # find way to sort using parition and not sorted
    # ids left just need to be smaller, not sorted, same with right
    playersSorted = sorted(players)
    """
   

    # playersSortedById = []
    # playersSortedByWeight = []
    # for player in playersSorted:
    #     playersSortedById.append(player[0])
    #     playersSortedByWeight.append(player[1])

    refID = WeightedMedian(playerWeights, playerIds)

    print(refID)


main()
