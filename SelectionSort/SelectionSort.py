'''Function to RETURN index of the Smallest element in an array'''
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallestIndex = i
    return smallestIndex

'''Function to RETURN index of the Largest element in an array'''
def findLargest(arr):
    largest = arr[0]
    largestIndex = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largestIndex = i
    return largestIndex

'''Selection Sort Functions'''
def selectionSortAsc(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

def selectionSortDsc(arr):
    newArr = []
    for i in range(len(arr)):
        largest = findLargest(arr)
        newArr.append(arr.pop(largest))
    return newArr

'''Testing Sorting Functions'''
nums = [36, 99, 7, 1, 1001, 88, 1_718_320_918]
smallestNumIndex = findSmallest(nums)
smallestNum = nums[findSmallest(nums)]
small2Large = selectionSortAsc(nums)

nums = [36, 99, 7, 1, 1001, 88, 1_718_320_918]
largestNumIndex = findLargest(nums)
largestNum = nums[findLargest(nums)]
large2Small = selectionSortDsc(nums)

nums = [36, 99, 7, 1, 1001, 88, 1_718_320_918]



