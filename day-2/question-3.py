# 3. write a program to find given number is positive ,negative or zero.


num=int(input("Enter a number to check if it is a zero, positive or negative number\n"))

if num<0:
    print(f"Number {num} is negative!")
elif num > 0:
    print(f"Number {num} is positive!")
else:
    print(f"Number is zero!")