# 2. Write a program to sum all the values of a dictionary.
# 
# Hint:
#   dict1 = {‘key 1’: 200, ‘key 2’: 300}
# Expected output Result: 500

def f1():
    nums = {'num1':1,'num2':2,'num3':3,'num4':4,'num5':5}
    res=0
    for num in nums.values():
        res +=num
    print(res)


f1()