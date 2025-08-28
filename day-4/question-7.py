# 7. Write a Python program that filters out numbers greater than 10 from a list of numbers using the filter()function.

# Input:
#       numbers = [5, 12, 3, 18, 9, 20, 22, 21]

# Output:[12, 18, 20, 22, 21]

def f1():
    numbers = [5, 12, 3, 18, 9, 20, 22, 21]

    isMoreThan10 = lambda n: n>10

    largerThan10=list(filter(isMoreThan10,numbers))

    print(largerThan10)


f1()