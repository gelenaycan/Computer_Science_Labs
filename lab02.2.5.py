"""
 The freshman of the students of a University
 is composed of two parts: a letter and a sequence
 of numbers. Write a program that, starting from two
 serial codes, shows them on the screen in ascending
 order based on the numerical part only. Tip: Use the
 default functions of the Python language.
"""

#define the serial codes

code1 = input("Write the first code:")
code2 = input("write the second code:")

#extract the numerical part of each code

num1 = int(code1[1:])
num2 = int(code2[1:])

#check which code has a higher numerical part

if num1>num2:
    print(code2)
    print(code1)
else:
    print(code1)
    print(code2)