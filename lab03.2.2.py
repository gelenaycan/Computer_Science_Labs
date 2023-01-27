"""
Write a program that translates a letter grade entered by
the user into the corresponding numerical grade and prints
it. The letter grades are 'A', 'B', 'C', 'D' and 'F',
possibly followed by a + or – sign. Their numerical values are,
in order, 4.0, 3.0, 2.0, 1.0 and 0.0. 'F+' and 'F–' grades do
not exist. A + sign increases the numerical grade by 0.3,
while a – sign decreases it by the same amount. The 'A+'
grade is equal to 4.0.
"""


result = float(input("Sınav sonucunu girin: "))

if result == 4.0 :
    print("your grade is A+")
elif result <4.0 and result > 3.7 :
    print("your grade is A")
elif result <3.7 and result > 3.3 :
    print("Your result is A-")
elif result <3.3 and result > 3.0:
    print("your result is A")


# gibi gibi gibi olabilir ve chatgbt der ki

def translate_grade(grade):
  if grade == "A+":
    return 4.0
  elif grade == "A":
    return 4.0
  elif grade == "A-":
    return 3.7
  elif grade == "B+":
    return 3.3
  elif grade == "B":
    return 3.0
  elif grade == "B-":
    return 2.7
  elif grade == "C+":
    return 2.3
  elif grade == "C":
    return 2.0
  elif grade == "C-":
    return 1.7
  elif grade == "D+":
    return 1.3
  elif grade == "D":
    return 1.0
  elif grade == "D-":
    return 0.7
  elif grade == "F":
    return 0.0
  else:
    return "Invalid grade"

# test the function
print(translate_grade("A+")) # should print 4.0
print(translate_grade("A")) # should print 4.0
print(translate_grade("B+")) # should print 3.3
print(translate_grade("C-")) # should print 1.7
print(translate_grade("F")) # should print 0.0
print(translate_grade("G")) # should print "Invalid grade"
