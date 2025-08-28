# 3. Generate all possible pairs from two strings using list comprehension.
# Input: "ab" and "cd"


def f1():

    str1 = 'ab'
    str2 = 'cd'
    res=''
    res = [c1+c2 for c1 in str1 for c2 in str2]

    print(res)



f1()