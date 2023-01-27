"""

Write a program that calculates taxes according to the following
scheme. The program should acquire the value of the income from
the user, and print the taxes due. It is not required to print
intermediate steps. [P3.25]
for civil status "unmarried" and taxable income higher than
$ 0
$ 8000
$ 32 000
for civil status "married" and taxable income higher than
$ 0
$ 16 000
$ 64 000
but not higher than
$ 8000 $ 32 000
but not higher than
$ 16 000 $ 64 000
taxes are
10%
$ 800 + 15% $ 4 400 + 25%
taxes are
10%
$ 1 600 + 15% $ 8 800 + 25%
of the sum in excess of
$ 0
$ 8 000
$ 32 000 of the sum in excess of
$ 0
$ 16 000
$ 64 000
"""


def main():

    Medeni_hal = input("Medeni Halinizi giriniz, Evli ise 'E', Bekarsanız 'B' giriniz. :")
    Gelir = float(input("Yıllık gelirinizi giriniz: "))
    Medeni_hal = Medeni_hal.upper()


    if Medeni_hal == "E" or "e":
       if Gelir >= 0 and Gelir < 8000:
           print(Gelir - (Gelir * 10) / 100 , "Toplam Gelir")
       elif Gelir >= 8000 and Gelir < 32000:
          print("Toplam Geliri ", (Gelir - (Gelir * 15)/100)+800, ".")
       else:
           print("Toplam Gelir", (Gelir - ((Gelir*25)/100) + 4400), ".")

    elif Medeni_hal == "B" or "b":
        if Gelir >= 0 and Gelir < 16000:
            print("Toplam Gelir", (Gelir - (Gelir*10)/100) , ".")
        elif Gelir >= 16000 and Gelir < 64000:
            print("Toplam Gelir", (Gelir - (Gelir*15)/100) + 16000, ".")
        else:
            print("Toplam Gelir", (Gelir-(Gelir*25)/100) + 88000, ".")

    else:
        print("Lütfen doğru bilgi girdiğinize emin olun.")


if __name__ == "__main__":
    main()
