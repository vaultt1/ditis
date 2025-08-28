# 4. In following text count occurrence of each letter (irrespective of case).
# 
# Hint: convert string to same case e.g. text.lower(). Do not use Counter collection.
# 

def f1():
    text = """Python is a high-level general-purpose programming language. Its design philosophyemphasizes code readability with the use of significant indentation. Python is dynamically typed andgarbage-collected. It supports multiple programming paradigms, including structured, object-orientedand functional programming."""

    text = text.lower()

    alpha = {'a':0,'b':0}
    for word in text:
        for letter in word:
            if letter in alpha.keys():
                    alpha[letter]=alpha.get(letter)+1
            else:
                alpha[letter]=1
    
    print(alpha)

    maximum_times = max(alpha.values())

    print(maximum_times)

    maxOccurrence = 0

    for key in alpha.keys():
        if alpha[key]==maximum_times:
             print(key)
             maxOccurrence=key


    print(f"The character '{maxOccurrence}' --> 'The WhiteSpace' which is occured {maximum_times} times")


f1()
