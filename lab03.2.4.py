"""
 A 366-day year is called a leap year and is used to keep the
 calendar synchronized with the Sun, since the Earth revolves
 around it once every 365.25 days or so. In reality, this number
 is not accurate, and for all dates after 1582 the Gregorian
 correction applies: usually years divisible by 4, such as 1996,
 are leap years, but years divisible by 100, such as 1900,
 are not; as an exception to the exception, years divisible
 by 400, such as 2000, are leap years. Write a program that
 asks the user for a year (greater than 1582) and determines
 whether it is a leap year using a single if construct and
 Boolean operators.
"""

year = int(input("Lütfen bir yıl girin: "))

if year < 1582:
    print("Gregorian correction applies can not use before 1582.")
elif (year % 4== 0 and year % 100 !=0) or (year % 400 == 0):
    print(year, " is a leap year.")
else:
    print(year, "is not a leap year.")