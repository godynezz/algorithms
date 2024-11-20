import algorithms
arr      = [3,3,1,3,4,5]
expected = [1,3,3,3,4,5]
sorted = algorithms.sort(arr)

if sorted == expected:
     print("Ok ->",sorted)
else:
     print("Err ->",sorted)

one = algorithms.binarysearch(sorted,1)
if one is not None :
    print("Ok ->", one)
else:
    print("Err ->", one)


threebang = algorithms.fat(3)

if threebang == 6:
    print("Ok ->",threebang)
else:
    print("Err ->",threebang)


