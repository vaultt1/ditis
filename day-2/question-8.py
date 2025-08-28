# 8. Write a program that prompts the user to input a character and determine the character is vowel or consonant


char = input("Please enter a single character to determine if it's a vowel or a consonant: ")
    
if len(char)==1:
    if 64<ord(char)<91 or 96<ord(char) <122:
        if char in 'aeiouAEIOU':
            print(f"Character {char} is a vowel")
        else:
            print(f"Character {char} is a consonant")
    else:
        print(f"Character {char} is a neither a consonant nor a vowel. ")
else:
    print(f"Please enter only ONE character!")