#1.Using for loop, write and run a Python program to find factorial from 0 to 10.

def fact_of(num):
    fact=1
    if num==0 or num==1:
        return fact
    else:
        for num in range(1,num+1):
            fact = fact*num
        return fact

for i in range(0,11):
    print(f"Factorial of: {i} is: {fact_of(i)}")
    

