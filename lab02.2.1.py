"""
Write a program that stores a string in a variable and
displays the first three characters
of the string, followed by three periods, again followed by
the last
three characters. For example, if the string is initialized
to the value "Mississippi", the program must
 isplay "Mis... ppi". What happens to the string is shorter
than 6 characters? What if it's shorter than 3 characters?
"""

















#define the string

string = input("Write a word:")

#get the length of the string

length = len(string)

#check if the string is shorter than 6 characters

if length<6:
    print(string)
elif length<3:
    print(string)
else:
    print(string[:3]+"..."+string[-3:])



