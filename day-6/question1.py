#1. Extract all odd numbers from a given list using list comprehension.
# numbers = [1, 2, 3, 4, 5, 6, 7]




def f1():

    numbers = [1, 2, 3, 4, 5, 6, 7]

    oddNums = [ n for n in numbers if n%2!=0]

    print(f'Odd numbers are: {oddNums}')



f1()