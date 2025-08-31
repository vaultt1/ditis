# 4. Get the first letter of each word in a sentence.
# Input: "Python is very powerful"


def f1():

    inputStr = "Python is very powerful"

    words = inputStr.split(" ")

    first_letter = [w[0] for w in words]

    print(first_letter)


f1()