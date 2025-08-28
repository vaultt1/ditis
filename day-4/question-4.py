# 4. Write a Python program that calculates the sum of the squares of all odd numbers in a list of integersusing map() and filter().
# 


def f1():

    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def isOdd(n):
        if n % 2 != 0:
            return n

    oddNums = list(filter(isOdd,numbers)) 
    

    squareOf = lambda n:n**2

    squares= list(map(squareOf,oddNums)) 

    sum_Of_Squares = 0
    for square in squares:
        sum_Of_Squares+=square

    print(sum_Of_Squares)



f1()