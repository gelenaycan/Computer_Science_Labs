"""
03.1.6 De Morgan. The De Morgan’s law makes it easy to apply the
not to expressions containing and/or operators. In particular,
this law has two expressions, one for the negation of expressions
in and, and one for the negation of expressions in or:
not (A and B) is equal to not A or not B not (A or B) is equal
to not A and not B
Consider the following expressions, and for each of them apply
De Morgan's law. Try to describe "in words" the intuitive
algebraic meaning of each of the expressions.
Then write a program that takes as input an integer x and
for each of the following expressions (which correspond to
the negation of the expressions in exercise 03.1.5)
prints: the starting expression, the expression after
applying De Morgan's law, and their truth value:
I. not(x>0andx<100) II. not(x>0orx<100) III. not(x>0or100<x)
IV. not(x>0andx<100orx==-1)
"""

def I(x):
    return not(x>0 and x<100)

def II(x):
    return not(x>0 or x<100)

def III(x):
    return not(x>0 or 100<x)

def IV(x):
    return not(x>0 and x<100) and not(x==-1)


print(I(50))
print(I(-1))
print(I(200))

print(II(50))
print(II(-1))
print(II(200))

print(III(50))
print(III(-1))
print(III(200))

print(IV(50))
print(IV(-1))
print(IV(200))
