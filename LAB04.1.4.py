"""

Write a program that reads a word and outputs:
I. The reversed word. If the user writes the
string 'Hello', the program shall output 'olleH' [P4.9]
II. The uppercase letters starting from the end.
If the user writes the string 'HeLlO', the program
shall output 'OLH'.

"""

# Read the input word

word = input("Enter a word: ")

# I. The reversed word

reversed_word = word[::-1]
print(f"Reversed word: {reversed_word}")

# II. The uppercase letters starting from the end
uppercase_letters =  [c for c in reversed_word if c.isupper()]
print(f"Uppercase letters starting from the end: {uppercase_letters}")