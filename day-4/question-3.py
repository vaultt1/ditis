# 3. Write a Python program to convert a given list of integers and a tuple of integers into a list of strings. Use Python map.

def f1():
    list1=[1,2,3,4,5,6,7,8,9]
    tuple1=(1,2,3,4,5,6,7,8,9)

    toStr = lambda num:str(num)

    numsString = list(map(toStr,list1))
    print(numsString)

    numsString = list(map(toStr,tuple1))
    print(numsString)

f1()