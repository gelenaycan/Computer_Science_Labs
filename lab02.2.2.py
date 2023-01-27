"""
The following pseudocode describes how to
transform a string containing a ten-digit
telephone number (such as "4155551212") into a
more easily readable string, formatted in the
U.S. style, such as "(415) 555–1212":
I. Take the string consisting of the first
three characters and surround it with round brackets
(this is the prefix, called "area code");
II. Concatenating the prefix with the string
containing the next three characters, a hyphen,
and the string consisting of the last four characters
results in the number in the required format.
Translate this pseudocode into a Python program
that stores a 10-digit phone number in a string,
and then display it in the format just described.

"""

#define the phone number

phone_number = "1234567891"

#split the phone number into ints parts

area_code = phone_number[:3]
middle_digits = phone_number[3:6]
last_digits = phone_number[6:]

#format the phone number

formatted_phone_number = "("+area_code+")" + middle_digits + "-" + last_digits

#display the formatted phone number

print(formatted_phone_number)