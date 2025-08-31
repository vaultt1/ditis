# 7. Write a function in Python to count and display the total number of words in a text file.


def counter(newdata):
    count=0
    for _ in newdata:
        count=count+1
    print(count)

def f1():
   
    with open("./story.txt", "rt") as file:
        data=file.read()
        
    data = data.replace("\n"," ").split(' ')
    
    counter(data)


f1()