import algorithms

#testing for selection sort
arr      = [3,3,1,3,4,5]
expected = [1,3,3,3,4,5]
sorted   = algorithms.selection_sort(arr)

if sorted == expected:
     print("Ok ->",sorted)
else:
     print("Err ->",sorted)


#testing for binary search
one = algorithms.binary_search(sorted,1)
if one is not None:
    print("Ok ->", one)
else:
    print("Err ->", one)

#testing for factorial
zerobang  = algorithms.factorial(0)
onebang   = algorithms.factorial(1)
threebang = algorithms.factorial(3)

if zerobang == 0:
    print("Ok ->",zerobang)
else:
    print("Err ->",zerobang)

if onebang == 1:
    print("Ok ->",onebang)
else:
    print("Err ->",onebang)

if threebang == 6:
    print("Ok ->",threebang)
else:
    print("Err ->",threebang)
