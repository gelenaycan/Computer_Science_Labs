"""
04.1.1 Integer numbers. Write a program reading a sequence of
integer numbers (an empty string is the end of the sequence) and,
after each input, executing and visualizing:
I. Partial sums of every number acquired; the program must visualize
the result of the calculations after each input.
As an example, if the input values are 1 7 2 9, the program shall
visualize the partial sum of the numbers acquired after each input:
a. After the first input (1), the first acquired value: 1.
b. After the second input (7), the sum between the first and
the second acquired
values:1 + 7 = 8.
c. After the third input (2), the sum between the first, the
second, and the third
acquired values: 1 + 7 + 2 = 10.
d. After the fourth input (9), the sum between the first,
the second, the third, and the
fourth values acquired:1 + 7 + 2 + 9 = 19.
II. The minimum and the maximum values among the acquired ones.
III. How many acquired values are even, how many acquired
values are odd
"""

"""
import sys

total = 0 #variable to store partial sum
minimum = float('inf') #variable to store the min value
maximum = float('-inf') #variable to store the max value
even_count = 0 #variable to store the count of even numbers
odd_count = 0 #variable to store the count of odd numbers

while True: #loop until an empty string is entered
    #read an integer number from the user
    number_str = input("Enter a number (empty string to end):")
    if number_str == "": #end the loop if an empty string entered
        break

    #covert the input string to an integer
    number = int(number_str)

    #update the partial sum
    total += number

    #update the minimum and maximum values
    minimum = min(minimum, number)
    maximum = max(maximum, number)

    #update the count of even and odd numbers

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

    print(f"Partial sum: {total}")
    print(f"minimum value: {minimum}")
    print(f"maximum value: {maximum}")
    print(f"even count: {even_count}")
    print(f"odd count: {odd_count}")

"""


import sys

def main():

    ok = True
    sum = 0
    even_number = 0
    total = 0
    minimum = sys.maxsize
    maximum = 0

    while ok:
        line = input("Write a number: ")
        if line == "":
            ok = False
        else:
            if not line.isdigit():
                print("This should be a number")
            else:
                num = int(line)
                if num < minimum:
                    minimum = num
                if maximum < num:
                    maximum = num
                if num %2 == 0:
                    even_number += 1
                total += 1
                sum = sum + num
                print(f"Sum: {sum}. Minumum: {minimum}. maximum: {maximum}. even{even_number}. odd numbers: {total - even_number}")


if __name__ == "__main__":
    main()



"""

import sys

def main():

    ok = True
    sum = 0
    even_number = 0
    total_acquisitions = 0
    minimum = sys.maxsize # any number "large enough" should be ok. However, this is the absolute maximum reachable
    maximum = 0

    while ok:
        line = input("Write a number: ")
        if line == "":
            ok = False
        else:
            if not line.isdigit():
                print("This should be a number!")
            else:
                num = int(line)
                if num < minimum:
                    minimum = num
                if maximum < num:
                    maximum = num
                if num % 2 == 0:
                    even_number += 1
                total_acquisitions += 1
                sum = sum + num # OR sum += num
                print(f"Sum: {sum}. Minimum: {minimum}. Maximum: {maximum}. Even numbers: {even_number}. Odd numbers: {total_acquisitions - even_number}")


if __name__ == "__main__":
    main()
"""