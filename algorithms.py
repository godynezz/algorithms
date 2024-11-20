def getsmallest(arr):
    small = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i] < small:
            small = arr[i]
            index = i
    return index


def sort(arr):
    sorted = []
    for i in range(len(arr)):
        smallest = getsmallest(arr)
        sorted.append(arr.pop(smallest))
    return sorted


def binarysearch(arr,item):
    low  = 0
    high = len(arr) - 1
    while low <= high:
        mid  = int((low + high)/2)
        kick = arr[mid]

        if kick == item:
            return kick
        elif kick > item:
            high = mid
        else:
            low = mid

    return None


def fat(x):
    if x == 1:
        return 1
    else:
        return x * fat(x-1)

