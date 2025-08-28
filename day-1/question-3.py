# 3. Write a program to accept a 4 digit number and
#   a. Display face value of each decimal digit
#   b. Display place value of each decimal digit
#   c. Display no in reverse order by changing decimal place values 
# If user enters a 4 digit number 9361
#   output should be 
#       a. 9 3 6 1 
#       b. 9361 = 9000 + 300 + 60 + 1 
#       c. 1639

    
def a(num):
    j=1000
    for i in range(4):
        quo=int(num/j)
        print(f"{quo}",end=" ")
        num = num-(quo*j)
        j=j/10


def b(num):
    j=1000
    for i in range(4):
        quo=int(num/j)
        print(f"{int(quo*j)}",end=" ")
        num = num-(quo*j)
        j=j/10


def c(num):
    for i in range(4):
        rem=int(num%10)
        num=int(num/10)
        print(rem,end=" ")


num= int(input("Enter any 4-digit number: "))

if (num<10000) & (num>999):
    print(f"a. ")
    a(num)
    print(f"\nb. ")
    b(num)
    print(f"\nc. ")
    c(num)
else:
    print(f"Number {num} is not a 4-digit number!")
