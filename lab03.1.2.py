"""
03.1.2 Identikit of the string. Write a program that reads a string and displays the
appropriate
messages, after checking if:
I. it contains only letters;
II. it contains only capital letters;
III. it contains only lowercase letters;
IV. it contains only digits;
V. it contains only letters and digits;
VI. it starts with a lowercase letter;
VII. it ends with a point.

"""

elements = ['abc', 'ABC', 'ABC123', '123', 'ABC123abc', 'abcdef','abc.']

for element in elements:
    if element.isalpha():
        print(element+ ' contains only elements.')
    elif element.isupper():
        print(element+' contains only capital letters')
    elif element.islower():
        print(element+ ' contains only lowercase letters')
    elif element.isdigit():
        print(element+ ' contains only digits.')
    elif element.isalnum():
        print(element+ ' contains only letters and digits.') #yalnızca harf ve rakam içerir
    elif element[0].islower():
        print(element+ ' start with a lowercase letter.')
    elif element[-1] == '.':
        print(element+ ' ends with a dot.')
        