"""
 Write a program that asks the user as input a wavelength value
 (real number, which can be written in scientific notation,
 e.g., 1.23e-7), and displays the description of the corresponding
 part of the electromagnetic spectrum, as shown in the table below.
"""
wavelength = float(input("Dalga boyu değeri(m): "))

if (wavelength > 10**-1):
    print("Radyo dalgaları")
elif (wavelength > 10**-3 and wavelength < 10**-1):
    print("Mikrodalgalar")
elif (wavelength > 7*(10**-7) and wavelength < 10**-3):
    print("Kızılötesi")
elif(wavelength > 4*(10**-7) and wavelength < 7*(10**-7)):
    print("Görünür ışık")
elif(wavelength > 10**-8 and wavelength < 4*(10**-7)):
    print("Ultraviyole")
elif(wavelength > 10**-11 and wavelength < 10**-8):
    print("X-Işınları")
elif(wavelength < 10**-11):
    print("Gama ışınları")





