"""
According to Coulomb's law, the electric force (expressed in Newtons) between two charged particles, Q1 and Q2, respectively, separated by a distance r,
๐น = ๐1 ๐2 -12 4 ๐ ๐ ๐2
where ๐ = 8.854 ร 10 farads/meter.
Write a program that calculates and displays the force relative to a doubly charged particle, allowing the user to select the values for Q1, Q2 (in Coulombs), and r (in meters).
"""

#electric force

Q1 = int(input("Q1= "))
Q2 = int(input("Q2= "))
r = int(input("yarฤฑรงap deฤerini giriniz: "))

ep = 8.854 * 10 **-12
from math import pi
F = (Q1 * Q2) / (4 * ep * (r **2 ) * pi)

print(F)

#define the constants

epsilon =  8.853 * 10**-12

#get the values from the user

q1= float(input("Enter the value of Q1 in Coulombs:"))
q2= float(input("Enter the value of Q2 in Coulumbs:"))
r= float(input("Enter the distance between the particles in meters:"))

#calculate the electric force

force = (q1*q2) / (4*3.14*epsilon*r**2)

#disply the result

print("The electric force is:",force,"Newtons")