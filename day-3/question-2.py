# 2. Write a program that accepts a list from user and print the alternate element of list.

nums=[0,0,0,0,0]
for i in range(0,5):
    nums[i]=input("Enter any number or string to add in list: ")

print(f" ")

for i in range(0,5):
    if ((i)%2)==0:
        print(f"Element at index {i} is: {nums[i]}")
    else:
        continue