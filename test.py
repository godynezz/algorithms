import algorithms

#testing for selection sort
arr      = [3,3,1,3,4,5]
expected = [1,3,3,3,4,5]
sorted   = algorithms.selection_sort(arr)

if sorted == expected:
     print("selection sort - Ok ->",sorted)
else:
     print("selection sort - Err ->",sorted)

#testing for quick sort
arr      = [5,3,3,1,3,4,5]
expected = [1,3,3,3,4,5,5]
sorted   = algorithms.quick_sort(arr)

if sorted == expected:
     print("quick sort - Ok ->",sorted)
else:
     print("quick sort - Err ->",sorted)


#testing for binary search
one = algorithms.binary_search(sorted,1)
if one is not None:
    print("binary search - Ok ->", one)
else:
    print("binary search - Err ->", one)

#testing for factorial
zerobang  = algorithms.factorial(0)
onebang   = algorithms.factorial(1)
threebang = algorithms.factorial(3)

if zerobang == 0:
    print("factorial - Ok ->",zerobang)
else:
    print("factorial - Err ->",zerobang)

if onebang == 1:
    print("factorial - Ok ->",onebang)
else:
    print("factorial - Err ->",onebang)

if threebang == 6:
    print("factorial - Ok ->",threebang)
else:
    print("factorial - Err ->",threebang)
