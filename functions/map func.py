"""map() returns iterator with each element of first iterator passed to func"""

array = [x for x in range(1, 10+1)]
print("array is: ", array)

array = map(lambda x: x+1, array)
print("modified array is: ", list(array))


"""
array is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
modified array is:  [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
"""
