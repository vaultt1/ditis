# 1. Given a dictionary of students and their favourite colours:
# 
# people={'Arham':'Blue','Lisa':'Yellow',''Vinod:'Purple','Jenny':'Pink'}

# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name




def f1():
    people={
        'Lisa':'Yellow',
        'Vinod':'Purple',
        'Jenny':'Pink',
        'Arham':'Blue'
    }

    count = 0
    for p in people:
        count = count+1

    print(f"a. ---> {count}",end="\n\n")

    for key in people.keys():
        if key == 'Lisa':
            people[key]='Red'
        
    print(f"b. ---> {people}",end="\n\n")

    people.pop('Jenny')
    print(f"c. ---> {people}",end="\n\n")

    print(f"d. ---> ",end="\n\n")
    names = list(people.keys())
    names.sort()
    print(names)

    colours = list(people.values())
    colours.sort()
    print(colours)


f1()