# 3. Define a function subtract() that takes two lists and returns difference (i.e. excess elements from list1). 
# If 
#   list1 = [10, 20, 30, 40] 
# and 
#   list2 = [30, 40, 50, 60], 
# then 
# result should be [10, 20]

 

def f1():

    list1 = [10, 20, 30, 40] 
    s1=set(list1)

    list2 = [30, 40, 50, 60]
    s2=set(list2)

    print(f"{s1 - s2}")


f1()