"""
05.1.3 Factoring of integers. Write a program that asks the user for an integer and then prints out all
its factors. For example, when the user enters 150, the program should print
2
3
5
5
"""



def main():

    number = input("Write a number: ")

    while not number.isnumeric():
        number = input("Come on..I said NUMBERRR!!: ")

    number = int(number)

    factor = 2
    print("The factors are: ")
    while number > 1:
        if number % factor == 0:
            print(factor)
            number = number / factor

        else:
            factor = factor + 1

if __name__ == "__main__":
    main()