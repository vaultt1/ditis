# 5. Write a Python program that adds two lists element-wise using the map() function.
# Input:
#       list1 = [1, 2, 3, 4, 5]
#       list2 = [5, 4, 3, 2, 1]
# Expected Output:
#       [6, 6, 6, 6, 6]


def f1():
    
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 4, 3, 2, 1]
    
    def add(n1,n2):
        return n1+n2

    res = list(map(add,list1,list2)) 
    
    print(res)


f1()