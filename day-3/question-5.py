# 5. Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise.


def overlapping(list1, list2):
    for i in list1:
        if i in list2:
            return True
    return False
    
list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]

print(f"{overlapping(list1, list2)}")
