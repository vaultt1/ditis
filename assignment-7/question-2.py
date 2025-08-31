#2. Write a version of a palindrome recognizer that also accepts phrase palindromes such as
# "Go hanga salami I'm a lasagna hog.",
# "Was it a rat I saw?",
# "Step on no pets",
# "Sit on a potato pan, Otis",
# "Lisa Bonet ate no basil",
# "Satan, oscillate my metallic sonatas",
# "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!".

# Note:  that punctuation, capitalization, and spacing are usually ignored.




import re

def is_palindrome(phrase):

    normalized_phrase = phrase.lower()
    
    cleaned_phrase = re.sub(r'[^a-z0-9]', '', normalized_phrase)
    
    return cleaned_phrase == cleaned_phrase[::-1]

def f1():

    test_phrases = [
        "Go hanga salami I'm a lasagna hog.",
        "Was it a rat I saw?",
        "Step on no pets",
        "Sit on a potato pan, Otis",
        "Lisa Bonet ate no basil",
        "Satan, oscillate my metallic sonatas",
        "I roamed under it as a tired nude Maori",
        "Rise to vote sir",
        "Dammit, I'm mad!"
    ]
    
    for phrase in test_phrases:
        if is_palindrome(phrase):
            print(f"'{phrase}' is a palindrome!")
        else:
            print(f"'{phrase}' is NOT a palindrome.")


f1()
