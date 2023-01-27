"""
Prime numbers. Write a program that asks the user for an
integer number and shows all the prime numbers lower or
equal to that number. Example: if the user inputs 20,
the program shall output:
      2
      3
      5
      7
      11
      13
      17
      19
"""

#Kullanıcıdan bir tamsayı alın

sayi = int(input("Bir tam sayı girin: "))

#Asal sayıları yazdırın

print(("Asal sayılar:"))
for i in range(2, sayi + 1):
    asal_mi = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            asal_mi = False
            break

    if asal_mi:
        print(i)