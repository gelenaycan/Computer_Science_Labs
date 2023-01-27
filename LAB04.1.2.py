"""
04.1.2 String analysis. Write a program that takes
as an input a line of text as a string and outputs
the following requests:
I. Only the capital letters in the string.
II. The letters in the string in even positions.
III. The same string with vowels
(uppercase and lowercase) replaced by an underscore (_).
IV. How many digits are contained in the string.
V. The positions of all vowels in the string.
"""

#read the input string

text = input("Enter a line of text: ")

# I.Only the capital letters in the string

capital_letters = [c for c in text if c.isupper()]
print(f"Capital letters: {capital_letters}")

# II. The letters in the string in even positions
even_letters = [c for i, c in enumerate(text) if i % 2 == 0]
print(f"Letters in even positions: {even_letters}")

# III. The same string with vowels (uppercase and lowercase) replaced by an underscore (_)
vowels = "aeiouAEIOU"
text_with_vowels_replaced = "".join(["_" if c in vowels else c for c in text])
print(f"String with vowels replaced: {text_with_vowels_replaced}")


# IV. How many digits are contained in the string
digit_count = sum([1 for c in text if c.isdigit()])
print(f"Number of digits: {digit_count}")

# V. The positions of all vowels in the string
vowel_positions = [i for i, c in enumerate(text) if c in vowels]
print(f"Vowel positions: {vowel_positions}")