"""
Given the numerical values of the grades explained in exercise
03.2.2, write a program that translates a number between 0.0 and
4.0 into the literal grade closest to it. For example,
the number 2.8 (which could be the average of several grades)
should be translated as 'B-'. Resolve cases of equality in favor
of the better grade: for example, 2.85 should be translated as 'B'.
"""

number = float(input("Lütfen 0.0 ile 4.0 arasında bir sayı girin: "))

if number >= 3.85:
    grade = "A"
elif number >= 3.5:
    grade = "A-"
elif number >= 3.15:
    grade = "B+"
elif number >= 2.85:
    grade = "B"
elif number >= 2.5:
    grade = "B-"
elif number >= 2.15:
    grade = "C+"
elif number >= 1.85:
    grade = "C"
elif number >= 1.5:
    grade = "C-"
elif number >= 1.15:
    grade = "D+"
elif number >= 0.85:
    grade = "D"
else:
    grade = "F"

print(number, "notu:", grade)
