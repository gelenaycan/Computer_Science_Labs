"""

Write a program that asks the user for an
integer number and shows as an output a message
showing whether the input number is prime.

"""

#Kullanıcıdan bir tamsayı alın

number = int(input("Enter a number: "))

#Sayının asal olup olmadığını kontrol edin

is_prime = True
if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5)+1):
        if number % i == 0:
            is_prime = False
            break

#Sonucu yazdır

if is_prime:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")


