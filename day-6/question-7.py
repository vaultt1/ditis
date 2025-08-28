# 7. List all consonants in the string “Yellow Yaks like yelling and yawning and yesterday they yodeledwhile eating yuky yams”.


def f1():
    givenStr = 'Yellow Yaks like yelling and yawning and yesterday they yodeledwhile eating yuky yams'

    vowels = 'aeiou'
 
    consonants = [c for c in givenStr.lower() if c.isalpha() and c not in vowels]

    print(consonants)

f1()



