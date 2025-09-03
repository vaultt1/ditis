#4. Write a program that reads a string from keyboard and display:
#a) The number of uppercase letters in the string
#b) The number of lowercase letters in the string
#c) The number of digits in the string
#d) The number of whitespace characters in the string

def f1():
   
    def analyze_string(input_string):
        uppercase_count = 0
        lowercase_count = 0
        digit_count = 0
        whitespace_count = 0

        for char in input_string:
            if char.isupper():
                uppercase_count += 1
            elif char.islower():
                lowercase_count += 1
            elif char.isdigit():
                digit_count += 1
            elif char.isspace():
                whitespace_count += 1
        
        print(f"Number of uppercase letters: {uppercase_count}")
        print(f"Number of lowercase letters: {lowercase_count}")
        print(f"Number of digits: {digit_count}")
        print(f"Number of whitespace characters: {whitespace_count}")

    user_input = input("Enter a string: ")
    analyze_string(user_input)



f1()


