# 1. Write a Python program that finds the longest word in a list of strings. Use map() to calculate the length of each word, and filter() to get the word with the maximum length.



def f1():
    words = ["python", "functional", "programming", "is", "powerful"]
    
    lengths = list(map(len, words))
    
    max_length = max(lengths)

    is_max = lambda word: len(word) == max_length
    
    longest_words = list(filter(is_max, words))
    
    print(longest_words)

f1()
