#5. Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "C".

def counter(data):
    count=0
    for newline in data:
        for i in range(len(data)):
            if newline[i][0]=='C':
                count=count+1
            
    print(len(data)-count)

def f1():
   
    with open("./story.txt", "rt") as file:
        data=file.read()

    counter(data.split("\n"))


f1()