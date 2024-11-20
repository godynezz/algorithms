def get_smallest_number(arr):
    small = arr[0]
    index = 0
    for i in range(1,len(arr)):
        if arr[i] < small:
            small = arr[i]
            index = i
    return index


def selection_sort(arr):
    sorted = []
    for i in range(len(arr)):
        smallest = get_smallest_number(arr)
        sorted.append(arr.pop(smallest))
    return sorted


def binary_search(arr,item):
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


def factorial(x):
    if x == 0 or x == 1:
        return x
    else:
        return x * factorial(x-1)


def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left  = []
    right = []

    for n in arr[1:]:
        if n >= pivot:
            right.append(n)
        else:
            left.append(n)

    return quick_sort(left) + [pivot] + quick_sort(right)
