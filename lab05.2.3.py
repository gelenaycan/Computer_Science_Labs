"""
05.2.3 Predator-prey simulation. The Lotka-Volterra equations describe
a predator-prey ecological model that is based on a set of fixed
positive constants:
• A. the growth rate of prey;
• B. the rate of destruction of prey by predators;
• C. the mortality rate of predators);
• D. the rate of increase of predators through the consumption of prey.
Considering these constants, the following conditions hold in this model:
I. a population of prey x increases at a rate dx=Ax dt (proportional
to the number of prey) but is simultaneously destroyed by predators at
a rate dx=− B xy dt (proportional to the product of the numbers of prey
and predators);
II. a population of predators y decreases at a rate
dy = − C y dt dy = − C y dt (proportional to the number of predators),
but increases at a rate dy = D xy dt (proportional to the product of the
number of prey and predators).
From these conditions, the system of differential equations derives:
dx/dt =Ax − Bxy dy/dt =−Cy + Dxy
This means that, considering two time periods n and n + 1, the variation
in the number of populations of prey (x) and predators (y), respectively,
from one period to the next is given by:
xn+1 = xn×(1+A−B×yn)
yn+1 = y×(1−C+D×xn)
Write a program that asks the user the input values of the four constants,
the initial number of prey and predator populations, and the number of
periods to be simulated. After, the program calculates and displays the
number of the two populations in each of the periods considered. As test
input, use A = 0.1, B = 0.01, C = 0.01, and D = 0.00002, with initial
populations of prey and predators of 1000 and 20, respectively.
"""

def main():

   A = float(input("A: "))
   B = float(input("B: "))
   C = float(input("C: "))
   D = float(input("D: "))

   prey = int(input("Enter the initial prey (1000 is a good choice): "))
   predators = int(input("Enter the initial predators (20 is a good choice):"))

   iterations = int(input("How many iterations?: "))

   for period in range (1, iterations + 1):

      new_prey = prey * (1+A - B*predators)
      new_predators = predators * (1-C + D*prey)

      if round(new_prey) !=0 and round(new_predators) !=0:
         print(f"[PERIOD {period:4}]": Predators := {round(new_predators)} vs Prey := {round(new_prey)})

      if round(new_prey) == 0:
         print(f"Prey has been eliminated...RIP")
         exit(0)

      prey = new_prey
      predators = new_predators

if __name__ == "__main__":
   main()
