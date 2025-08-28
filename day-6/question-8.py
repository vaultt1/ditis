# 8. Write a program to find out the frequency of each number in stored in a list using a python dictionary.
# Example:
#   List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4]
# Output ={1: 1, 2: 3, 3: 1, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 1, 23: 1}


def f1():

    List1 = [1,2,3,4,5,6,7,8,9,7,6,2,4,2,5,23,6,4,50,44,89,5,4]

    counter ={}

    for num in List1:
            # check if the word is present in the dictionary
            if num in counter:
                # if it is present, increment the count
                counter[num] += 1
            else:
                # if it is not present, add the word with count = 1
                counter[num] = 1

    print(counter)



f1()