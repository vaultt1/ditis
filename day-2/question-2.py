#2. Write a Python function to find the maximum of three numbers

def find_max():

    num1=int(input("Enter 1st number \n")) 
    num2=int(input("Enter 2nd number \n")) 
    num3=int(input("Enter 3rd number \n")) 

    if num1>num2:
        if num1>num3:
            print(f"Number {num1} is greated among {num1}, {num2} and {num3}")
        else num3>num2:
            print(f"Number {num3} is greated among {num1}, {num2} and {num3}")
    else:
        if num2>num3:
            print(f"Number {num2} is greated among {num1}, {num2} and {num3}")
        else:
            print(f"Number {num3} is greated among {num1}, {num2} and {num3}")
    
    
find_max()