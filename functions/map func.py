"""map() returns iterator with each element of first iterator passed to func"""

array = [x for x in range(1, 10+1)]
print("array is: ", array)

array = map(lambda x: x+1, array)
print("modified array is: ", list(array))
