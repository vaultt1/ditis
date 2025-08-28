# 7. Write a function filter_long_words() that takes a list of words and an integer len and returns the list of words that are longer than len.

def filter_long_words(words,min_length):
    result=[]
    for word in words:
        if len(word)>min_length:
            result.append(word)
    return result
    

words = ["Aryan", "Vyankatesh", "Varad", "Shyam", "Somya", "Chirayu"]
min_length = 5

long_words = filter_long_words(words, min_length)
print(f"Words longer than {min_length} characters: {long_words}")
