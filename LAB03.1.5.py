"""
Matter of logic. Write a program that takes as input an integer
number x and displays the following expressions on the screen, along
with their truth values. Test the program with numerous values of x.
I. x > 0 and x < 100 II. x > 0 or x < 100 III. x > 0 or 100 < x
IV. x > 0 and x < 100 or x == -1

"""

x = int(input('Lütfen bir tamsayı girin: '))

print('x>0 and x <100:', x > 0 and x < 100)
print('x>0 or x<<00:', x>0 or x<100)
print('x>0 or 100<x', x>0 or 100<x)
print('x>0 and x<100 or x == -1', x>0 and x<100 or x == -1)