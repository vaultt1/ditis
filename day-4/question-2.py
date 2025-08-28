# 2. Write a Python program to double all numbers in a given list of integers. Use Python map, lambda function.


def f1():
    list1 = [1,2,3,4,5,6,7,8,9]
    double = lambda n:n*2
    doubled_list = list(map(double,list1))
    print(list1)
    print(doubled_list)

f1()