# 4. Write a program to accept three integer numbers and find its average.


def avg(n1,n2,n3):
    return int((n1+n2+n3)/3)

n1=int(input("Enter 1st Number\n"))
n2=int(input("Enter 2nd Number\n"))
n3=int(input("Enter 3rd Number\n"))

print(f"Average of numbers {n1},{n2} and {n3} is: {avg(n1,n2,n3)}")