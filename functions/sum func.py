"""
when there's a str in iterable, then it will raise an exception
sum(iter, start) is equal to sum(iter) + start

"""
import sys

numbers = [1, 2, 3, 4]
numbers_and_letters = [1, 2, 3, 4, "hola"]

try:
    print(f"sum of numbers are: {sum(numbers)}")
    print(
        f"sum of list with numbers and letters are {sum(numbers_and_letters)}")
except Exception as e:
    print(e)
    sys.exit()
