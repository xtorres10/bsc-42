import sys

def text_analyzer(string=None):
    """
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if isinstance(string, int):
        return ("Argument is not a string")
    if string is None:
        string = input("What is the text to analyze?\n")
    upper = 0
    lower = 0
    space = 0
    punct = 0
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isspace():
            space += 1
        elif char in '''!()-[]{};:'"\,<>./?@#$%^&*_~''':
            punct += 1
    total = upper + lower + space + punct
    print(f"The text contains {total} character(s):\n\
    - {upper} upper letter(s)\n\
    - {lower} lower letter(s)\n\
    - {punct} punctuation mark(s)\n\
    - {space} space(s)")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        text_analyzer(sys.argv[1])
    else:
        print('Error, expect 1 argument.')
