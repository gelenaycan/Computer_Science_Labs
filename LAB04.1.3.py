"""

Write a program that takes as an
input an integer number n and prints
a square and a rhombus filled with
asterisks (*), with each side
long n asterisks.
Example: using n=4, the program shows:
      ****
      ****
      ****
      ****
         *
        ***
       *****
      *******
       *****
        ***
         *

"""

# Read the input number

n = int(input("Enter a number: "))

# Print the square
for i in range(n):
    print("*" * n)

print() # print an empty line

#print the rhombus

for i in range(n):
    print(" " * (n - i -1) + "*" * (2 * i + 1))

for i in range(n -2, -1, -1):
    print(" " * (n - i -1) + "*" * (2 * i + 1))