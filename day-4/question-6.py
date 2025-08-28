# 6. Write a Python program that filters out all strings that have more than 5 characters from a list of strings using the filter() function.
# Input:
#       words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']
# Output:   
#       ['Yellow', 'Purple', 'Orange']


def f1():
    words = ['Red', 'Green', 'Yellow', 'Purple', 'Orange']

    isValid = lambda n:len(n)>5

    res = list(filter(isValid,words))

    print(res)




f1()