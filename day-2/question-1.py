#1. Write A Program which is taking 5 int value and calculate sum of cube of all numbers [Write cube function]

num1 = int(input("Enter a 1st number\n"))
num2 = int(input("Enter a 2nd number\n"))
num3 = int(input("Enter a 3rd number\n"))
num4 = int(input("Enter a 4th number\n"))
num5 = int(input("Enter a 5th number\n"))

def cube(num1,num2,num3,num4,num5):
    num1=num1**3
    num2=num2**3
    num3=num3**3
    num4=num4**3
    num5=num5**3
    print(num1,num2,num3,num4,num5)
    add(num1,num2,num3,num4,num5)

def add(num1,num2,num3,num4,num5):
    print(f"Addition of cubes of each numbers is: {num1+num2+num3+num4+num5}")
    
cube(num1,num2,num3,num4,num5)