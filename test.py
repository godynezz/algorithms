import algorithms

# testing for selection sort
arr = [3, 3, 1, 3, 4, 5]
expected = [1, 3, 3, 3, 4, 5]
sorted = algorithms.selection_sort(arr)

if sorted == expected:
    print("selection sort - Ok ->", sorted)
else:
    print("selection sort - Err ->", sorted)

# testing for quick sort
arr = [5, 3, 3, 1, 3, 4, 5]
expected = [1, 3, 3, 3, 4, 5, 5]
sorted = algorithms.quick_sort(arr)

if sorted == expected:
    print("quick sort - Ok ->", sorted)
else:
    print("quick sort - Err ->", sorted)


# testing for linear search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
index = algorithms.linear_search(arr, 10)

if arr[index] == 10:
    print("linear search - Ok -> 10 is at Index:", index)
else:
    print("linear search - Err -> unexpected index:", index)

# testing for binary search
index = algorithms.binary_search(sorted, 1)
if sorted[index] == 1:
    print("binary search - Ok -> [", index, "]")
else:
    print("binary search - Err -> [", index, "]")

# testing for factorial
zerobang = algorithms.factorial(0)
onebang = algorithms.factorial(1)
threebang = algorithms.factorial(3)

if zerobang == 0:
    print("factorial - Ok ->", zerobang)
else:
    print("factorial - Err ->", zerobang)

if onebang == 1:
    print("factorial - Ok ->", onebang)
else:
    print("factorial - Err ->", onebang)

if threebang == 6:
    print("factorial - Ok ->", threebang)
else:
    print("factorial - Err ->", threebang)

# testing two sum
arr = [1, 1, 1, 7, 4, 6, 9, 4, 5, 9, 2, 3, 5, 7]
expected = [5, 6]
found = algorithms.two_sum(arr, 15)

if found == expected:
    print("two sum - Ok -> found|expected :", found, "==", expected)
else:
    print("two sum - Err -> found|expected :", found, "!=", expected)
