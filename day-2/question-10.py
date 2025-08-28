# 10. write a function to return compound interest.CI = P (1 + r/n) ^ ntP - Principal Amountr - Rate of interestn - Number of times interest compounds in a yeart - Number of years


def calc_CI(p, t, r, n):
    CI = p * (1 + r/n)**(n*t) - p
    return CI


p = float(input("Enter Principal for Compound Interest to be calculated: "))
t = float(input("Enter Number of years for Compound Interest to be calculated: "))
r = float(input("Enter Rate of Interest for Compound Interest to be calculated (in %): ")) / 100  
n = int(input("Enter Number of times interest compounds in a year: "))

CI = calc_CI(p, t, r, n)

print(f"Compound Interest for Principal of {p}/- Rs, for {t} years at the rate of {r*100}% compounded {n} times a year is: {CI:.2f}/- Rs.")
