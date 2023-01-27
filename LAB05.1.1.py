"""
05.1.1 ATM. When you use an automated teller machine (ATM) with your bank card, you need to use
a personal identification number (PIN) to access your account. If a user fails more than three times
when entering the PIN, the machine will block the card. Assume that the user’s PIN is “1234” and write
a program that asks the user for the PIN no more than three times, and does the following:
• If the user enters the right number, print a message saying, “Your PIN is correct”,
and end the program.
• If the user enters a wrong number, print a message saying, “Your PIN is incorrect”
and, if you have asked for the PIN less than three times, ask for it again.
• If the user enters a wrong number three times, print a message saying “Your bank card
is blocked” and end the program.
"""

CORRECT_PIN = 1234

def main():

    for i in range(3):

        user_pin = input("What is your PIN code?: ")

        while not user_pin.isnumeric():
            user_pin = input("Wrong format! What is your PIN?: ")

        user_pin = int(user_pin)

        if user_pin == CORRECT_PIN:
            print("Your pin is CORRECT. Welcome.")
            exit(0)
        else:
            print("Your pin is incorrect")

    print("Your bank card is blocked")
    exit(0)

if __name__ == "__main__":
    main()


