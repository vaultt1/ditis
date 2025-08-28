# 6. Find and display the largest number of a list without using built-in function max(). Your program should ask the user to input values in list from keyboard.


count=int(input("Enter number of items you want to enter in the list: "))

def maximum(list):
    max=list[0]
    for num in list:
        if num>max:
            max=num
    print(f"Maximum value in given list is: {max}")

list=[]

for i in range(0,count):
    new_val=int(input(f"Enter a value for index {i}: "))
    list.append(new_val)

print(f'{list}')
maximum(list)

