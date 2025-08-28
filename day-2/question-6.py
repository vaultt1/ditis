# 6. The marks obtained by a student in 3 different subjects are input by the user. 
# Your program should calculate the average of subjects and display the grade. 
# The student gets a grade as per the following rules:
# Average Grade
# 90-100    A
# 80-89     B
# 70-79     C
# 60-69     D
# 0-59      F


sub1=int(input("Enter your marks in Physics: "))
sub2=int(input("Enter your marks in Chemistry: "))
sub3=int(input("Enter your marks in Maths: "))

avg_marks = (sub1+sub2+sub3)/3

if 89<avg_marks<=100:
    print(f"Congratulations! You got A grade!")
if 80<=avg_marks<90:
    print(f"Congratulations! You got B grade!")
if 70<=avg_marks<80:
    print(f"Congratulations! You got C grade!")
if 60<=avg_marks<70:
    print(f"Congratulations! You got D grade!")
if 0<=avg_marks<60:
    print(f"Congratulations! You got F grade!")