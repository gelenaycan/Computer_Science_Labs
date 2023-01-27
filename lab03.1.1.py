"""
03.1.1 True or False. For each of the following pairs of values, perform an equality test, assign the result to a variable, and display it. Try to predict what the result of each test will be.
I. 1,1;
II. 1, 1.0;
III. 2.0, sqrt(4);
IV. '1', 1;
V. 'hello', 'Hello'.
"""

I = (1==1)

II = ( 1== 1.0)

from math import sqrt
III = (2.0 == sqrt(4))

IV = ('1' == 1)

v = ( 'hello' == 'Hello')

print(I)
print(II)
print(III)
print(IV)
print(v)