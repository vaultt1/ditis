# 9. write a function to return simple interest.
# To calculate simple interest, you can use the formula: SI = (P × R × T) / 100
# SI: Stands for simple interest
# P: Represents the principal amount
# R: Represents the interest rate per year
# T: Represents the time in years


def calc_SI(p,n,r):
    return ((p*n*r)/100)
    
p=float(input("Enter Principal for simple interest to be calculated: "))
n=float(input("Enter Number of years for simple interest to be calculated: "))
r=float(input("Enter Rate of Interest for simple interest to be calculated: "))

print(f"Simple Interest for Principal of {p}/- Rs, for {n} years at the rate of {r}% will be: {calc_SI(p,n,r)}/- Rs.")