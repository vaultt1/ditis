# 2. Extract vowels from a string using list comprehension. (Input: "education")

def f1():
    inputStr = input("Enter A String: ")

    vowels = [c for c in inputStr if c in 'aeiouAEIOU']

    print(vowels)


f1()