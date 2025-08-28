# 5. Extract only the keys from a dictionary using list comprehension.


def f1():

    dict1={'name':'person',"age":19, 'ph-no':4566544683}

    keys = [key for key in dict1.keys()]

    print(keys)



f1()