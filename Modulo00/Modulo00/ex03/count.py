import sys
import string

def text_analyzer(text=None):

    '''This function takes a string as input and counts the number of uppercase characters,
       lowercase letters, punctuation marks, and spaces. If no string is provided as an argument,
       prompts the user to enter a string. If the argument is not a string, it is printed
       an error message.'''    
  
    if text is None:
        text = input("What is the text to analyze?\n")

    elif not isinstance(text, str):        
        return print("AssertionError: argument is not a string")

    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif char in string.punctuation:
            punctuation_count += 1
        elif char.isspace():
            space_count += 1

    print(f"The string has {upper_count} uppercase characters")
    print(f"The string has {lower_count} lowercase characters")
    print(f"The string has {punctuation_count} punctuation marks")
    print(f"The string has {space_count} spaces")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided\n")
    elif len(sys.argv) < 2:
        text_analyzer()
    else:
        text_analyzer(sys.argv[1])
