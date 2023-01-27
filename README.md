# Computer_Science_Labs
Politecnico di Torino-Computer Science Lecture's labs
07JCJLI Computer Science, 2022/23 Lab01
1
-Computer Science Laboratory 01
Themes
1. A first approach to computational thinking:
a. Computers and computer programs
b. Well-formulated problems and algorithms
c. Flowcharts and pseudocode
2. Python first steps:
a. Environment set-up
b. Creating and executing programs
c. Print to terminal
Discussion
A. Explain the difference between using a computer program and programming a computer.
B. A toaster is a single-function device, but a computer can be programmed to carry out
different tasks. Is your cell phone a single-function device, or is it a programmable
computer? (Your answer will depend on your cell phone model.)
C. What are the characteristics of an algorithm that needs to be understood and executed by a
computer?
D. What is the relationship between the starting problem, the pseudocode, the computer
program, the flowchart, and the programming language?
Exercises
Part 1 – From problem to algorithm
Task: Asses whether the following problems are formulated in such a way that they can managed by
a computer program. If they are, write an algorithm (as pseudocode and/or flowchart) to solve
them. Otherwise, describe why they cannot be managed by a computer program. Complete at least
the first four exercises during the laboratory session and finish the remaining ones at home. It is not
required to write any Python code.
01.1.1 Scheduling. In a scheduling program, we want to check whether two appointments overlap.
For simplicity, appointments start at a full hour, and we use military time (with hours 0–23).
The following pseudocode describes an algorithm that determines whether the appointment
with starting time start1 and ending time end1 overlaps with the appointment with starting
time start2 and ending time end2.
If start1 > start2
s = start1
Else
s = start2
If end1 < end2
e = end1
Else
e = end2
If s < e
07JCJLI Computer Science, 2022/23 Lab01
2
The appointments overlap.
Else
The appointments don’t overlap.
Check this algorithm with the following example values used as test cases: an appointment
from 10–12 and the second one from 11–13.
Second example: an appointment from 10–11 and one from 12–13. [R3.12]
01.1.2 Seasons. The following algorithm yields the season (Spring, Summer, Fall, or Winter) for a
given month and day.
If month is 1, 2 or 3
season = “Winter”
Else, if month is 4, 5 or 6
season = “Spring”
Else, if month is 7, 8 or 9
season = “Summer”
Else, if month is 10, 11 or 12
season = “Fall”
If month can be divided by 3 and day is >= 21
If season is “Winter”
season = “Spring”
Else, if season is “Spring”
season = “Summer”
Else, if season is “Summer”
season = “Fall”
Else
season = “Winter”
Draw the corresponding flowchart. Verify the correctness of the algorithm with a series of
test date. [R3.13]
01.1.3 On the road. You want to find out which fraction of your car’s use is for moving to work, and
which is for personal use. You know the one-way distance from your home to your work
place. For a particular period, you recorded the beginning and ending kilometers on the
odometer and the number of working days. Write an algorithm to settle this question.
[R1.16]
01.1.4 Checkboard tiling. Make a plan for tiling a rectangular bathroom floor with alternating black
and white tiles measuring 10 × 10 cm. The floor is of size 50 x 30 cm [Worked Example 1.1]
01.1.5 Future Decisions. A student that is about to finish his/her high school and wants to choose
which University apply to. They can base their decision on other people suggestions, and on
the mean salary obtainable one year after graduation. Most of the faculties they are
interested in offer statistics on the employment of grad students. How can they decide?
01.1.6 Know when to stop. The value of π can be computed according to the following formula: 
07JCJLI Computer Science, 2022/23 Lab01
3
Write an algorithm to compute π. Because the formula is an infinite series and an algorithm
must stop after a finite number of steps, you should stop when you have the result
determined to six significant digits. [R1.18]
01.1.7 Back to square 1. Consider the following algorithms:
Use this algorithm to compute √3.
07JCJLI Computer Science, 2022/23 Lab01
4
Part 2 – From algorithms to code
Task: Debug the following program to understand how variables are assigned and computed inside a
python program.
01.2.1 Copy and paste the following code inside PyCharm:
def compute_operating_cost(annual_km_driven, years, fuel_cost, km_per_liter):
annual_fuel_consumed = annual_km_driven / km_per_liter
annual_fuel_cost = fuel_cost * annual_fuel_consumed
operating_cost = annual_fuel_cost * years
return operating_cost
car_1_price = float(input("What is the price of car 1?"))
car_2_price = float(input("What is the price of car 2?"))
car_1_km_per_liter = float(input("How many km does car 1 do with a liter of fuel?"))
car_2_km_per_liter = float(input("How many km does car 2 do with a liter of fuel?"))
years = int(input("How many years will you drive this car? "))
km_per_year = int(input("On average, how many km will you drive each year? "))
fuel_cost = float(input("On average, how much dollars does it coast a liter of fuel? "))
annual_km_driven = years * km_per_year
car_1_operating_cost = compute_operating_cost(annual_km_driven, years,
fuel_cost, car_1_km_per_liter)
car_2_operating_cost = compute_operating_cost(annual_km_driven, years,
fuel_cost, car_2_km_per_liter)
car_1_total_cost = car_1_price + car_1_operating_cost
car_2_total_cost = car_2_price + car_2_operating_cost
if car_1_total_cost < car_2_total_cost:
print("Car 1 is less expenisve overall")
else:
print("Car 2 is less expensive overall")
 
07JCJLI Computer Science, 2022/23 Lab01
5
Part 3 – From algorithms to code
Task: For each of the following sub-task, write a python program that prints out the required output.
If you have enough time, complete the exercises in the lab, otherwise complete them at home.
01.3.1 A phrase to celebrate the beginning of Computer Science laboratories. [P1.1]
01.3.2 Write a program that prints the sum of the first ten positive integers, 1 + 2 + … + 10. [P1.2]
01.3.3 Write a program that prints the product of the first ten positive integers, 1 × 2 × … × 10. (Use
* to indicate multiplication in Python.) [P1.3]
01.3.4 Write a program that prints your name in large letters, such as:
[P1.6]
01.3.5 Your name in a column.
01.3.6 Write a program that prints the balance of an account after the first, second, and third year.
The account has an initial balance of $1,000 and earns 5 percent interest per year. [P1.4]
01.3.7 Write a program that displays your name inside a box on the screen, like this:
+------+
¦ Dave ¦
+------+
Do your best to approximate lines with characters such as | - +.
[P1.5]
01.3.8 Write a program that prints an animal speaking a greeting, similar to (but different from) the
following, without using the command cowsay:
[P1.10]
01.3.9 An alphanumeric code of 16 characters alternating strings “abcd” and “1234”.
07JCJLI Computer Science, 2022/23 Lab01
6
01.3.10 A checkboard of size 5x5 where the white squares are indicated by a “0”, and the black
squares by a “1”.
01.3.11 O line of 100 dashes (“-”).
01.3.12 A sequence of 100 zeros.
01.3.13 The fourth element of the Fibonacci sequence, where every element is the sum of the two
preceding elements. The first two elements of the sequence are 0 and 1.
01.3.14 The first four element of the Fibonacci sequence in a column.
01.3.15 A closing phrase for this laboratory session, inside a box of your choosing, including the
computation of the percentage of exercises you completed.
14BHD Informatica, A.A. 2022/23 Lab02
1
-Laboratory Exercise 02
Topics
1. Variables in Python
a. Variable types
b. Basic arithmetic operators
c. String manipulation
Discussion
A. In what relation are the assigned value, variable, and data type?
B. Give an example of feasible operations on variables with assigned values corresponding to
different types of data.
C. Consider the "+" operator. What if it is used between...
a. Two variables with values of type int;
b. A variable with a value of type int and one with a value of type float;
c. Two variables with values of type str;
d. A variable with a value of type int and one with a value of type str.
Exercises
Part 1 - Arithmetic operations
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least two exercises during the lab session, and the rest at home.
02.1.1 Two numbers. Write a program that stores two integers in two constants defined in code,
and then displays them:
A. The sum;
B. The difference;
C. The product;
D. The average value;
E. The distance (i.e. the absolute value of the difference);
F. The maximum value (i.e. the greater of the two);
G. The minimum value (i.e. the lesser of the two).
Tip: Use the max() and min() functions defined in Python. They accept a sequence of commaseparated values in input and return the maximum and minimum value of the sequence,
respectively (for example, max(10, 5) returns 10). (P2.4)"
02.1.2 Resistances. Consider the following circuit.
14BHD Informatica, A.A. 2022/23 Lab02
2
Write a program that, starting from the resistance of the three resistors, given by the user,
calculates the total resistance, using Ohm's law. [P2. 38]
02.1.3 Digits. Write a program that stores in a constant a positive five-digit integer (therefore
between 10000 and 99999), and displays the individual digits of which it is composed. For example,
having the number 16384, the program must display, on separate lines: 1 6 3 8 4. (p2.16)
02.1.4 Hybrid car. Writing the pseudocode and its Python program that helps a person decide
whether or not to buy a hybrid car. The inputs of the program should be:
I. the cost of a new car;
II. the estimate of the kilometers traveled in a year;
III. The estimate of the cost of fuel;
IV. Efficiency in kilometers per liter;
V. The estimate of the resale value of the used car after 5 years.
Calculate the total cost of ownership of the car for 5 years (for simplicity, do not take into account
the cost of financing). To provide input to the program, search the Web for realistic prices and
consumption for two alternatives for buying a new car in the same price range: a hybrid model or
and a gasoline. Run the program twice to compare the two alternatives, considering the current fuel
price and the forecast of traveling 30,000 kilometers per year. (2.10 pm)
02.1.5 Electric force. According to Coulomb's law, the electric force (expressed in Newtons) between
two charged charged particles, respectively, Q1 and Q2, separated by a distance r, is
𝐹 =
𝑄1 𝑄2
4 𝜋 𝜀 𝑟
2
where 𝜀 =  8.854  × 10−12 Farad / meter. Write a program that calculates and shows on screen
the force relative to a pair of charged particles, allowing the user to choose the values Q1, Q2 (in
Coulomb) and r (in meters). (2.43 pm)
Part 2 – String Manipulation
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least two exercises during the lab session, and the rest at home.
02.2.1 Characters. Write a program that stores a string in a variable and displays the first three
characters of the string, followed by three periods, again followed by the last three characters. For
example, if the string is initialized to the value "Mississippi", the program must display "Mis...
ppi". What happens to the string is shorter than 6 characters? What if it's shorter than 3
characters? (p2.22)
02.2.2 Telephone Number. The following pseudocode describes how to transform a string
containing a ten-digit telephone number (such as "4155551212") into a more easily readable string,
formatted in the U.S. style, such as "(415) 555–1212":
I. Take the string consisting of the first three characters and surround it with round brackets
(this is the prefix, called "area code");
II. Concatenating the prefix with the string containing the next three characters, a hyphen, and
the string consisting of the last four characters results in the number in the required format.
Translate this pseudocode into a Python program that stores a 10-digit phone number in a string,
and then display it in the format just described. (2.33 pm)
02.2.3 Alignment. Format the output of exercise 02.1.1 so that descriptions and numbers are
aligned vertically, for example: 
14BHD Informatica, A.A. 2022/23 Lab02
3
Sum: 45
Difference: -5
......
[P2.5]
02.2.4 Emoji. According to data collected by the Unicode Consortium1
, the non-profit organization
responsible for digitizing the world's languages, "tears of joy" ( ) account for more than 5% of all
emojis used (the only other character that comes close to it is the ). The top ten emojis used
worldwide are: .
When exchanging messages on Telegram (or on your favorite messaging app), which are the three
emojis that you personally use most frequently? Using the Unicode encoding information collected
here2
, you cancreate a program that shows a scheme for each of these three emojis:
I. the position in the ranking (rank);
II. the Unicode Number;
III. the Unicode Name;
IV. the emoji itself.
Format the output so that the information related to each of the three emojis is collected on one
line, and the different fields are aligned vertically.
02.2.5 Registrations. The freshman of the students of a University is composed of two parts: a letter
and a sequence of numbers. Write a program that, starting from two serial codes, shows them on
the screen in ascending order based on the numerical part only. Tip: Use the default functions of
the Python language.
1 https://home.unicode.org/emoji/emoji-frequency/
2 https://unicode-table.com/
07JCJLI Computer Sciences, A.Y. 2022/23 Lab03
1
-Laboratory 03
Topics
1. Elaborations and comparisons between values of type int, float and str
2. Boolean expressions
3. Logic decisions
4. Conditional constructs (if, else, and elif)
5. Nested blocks and instructions
Discussion
A. What are the possible syntax forms of a conditional construct?
B. Explain the similarities and differences between:
a. conditional operators and Boolean operators;
b. assignments and equality test;
c. and, or, and not.
C. How do you define compound statements?
Exercises
Part 1 – Comparisons, relational and Boolean operators
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least two exercises during the lab, and the remaining ones at home.
03.1.1 True or False. For each of the following pairs of values, perform an equality test, assign the
result to a variable, and display it. Try to predict what the result of each test will be.
I. 1, 1;
II. 1, 1.0;
III. 2.0, sqrt(4);
IV. '1', 1;
V. 'hello', 'Hello'.
03.1.2 Identikit of the string. Write a program that reads a string and displays the appropriate
messages, after checking if:
I. it contains only letters;
II. it contains only capital letters;
III. it contains only lowercase letters;
IV. it contains only digits;
V. it contains only letters and digits;
VI. it starts with a lowercase letter;
VII. it ends with a point.
[P3.17]
03.1.3 Strings and substrings. DNA sequences are like long strings consisting of only four letters:
'A', 'C', 'T' and 'G'. Write a program that takes as input a "long sequence" of DNA of twenty
characters and a "short sequence" of three characters and displays: 
07JCJLI Computer Sciences, A.Y. 2022/23 Lab03
2
I. if the "long sequence" contains the "short sequence";
II. if yes:
a. from which position of the "long sequence" the "short sequence" starts;
b. how many times the "long sequence” contains the shorter substring.
[Chapter 3.8]
03.1.4 It’s equal. Describe the pseudocode corresponding to the following Python program:
x = 3.0
s == 'seven point five'
if x = 3.0:
 s == 'three point zero'
print(s)
What is the output of this program?
03.1.5 Matter of logic. Write a program that takes as input an integer number x and displays the
following expressions on the screen, along with their truth values. Test the program with numerous
values of x.
I. x > 0 and x < 100
II. x > 0 or x < 100
III. x > 0 or 100 < x
IV. x > 0 and x < 100 or x == -1
[Chapter 3.7]
03.1.6 De Morgan. The De Morgan’s law makes it easy to apply the not to expressions containing
and/or operators. In particular, this law has two expressions, one for the negation of expressions in
and, and one for the negation of expressions in or:
not (A and B) is equal to not A or not B
not (A or B) is equal to not A and not B
Consider the following expressions, and for each of them apply De Morgan's law. Try to describe "in
words" the intuitive algebraic meaning of each of the expressions.
Then write a program that takes as input an integer x and for each of the following expressions
(which correspond to the negation of the expressions in exercise 03.1.5) prints: the starting
expression, the expression after applying De Morgan's law, and their truth value:
I. not (x > 0 and x < 100)
II. not (x > 0 or x < 100)
III. not (x > 0 or 100 < x)
IV. not (x > 0 and x < 100 or x == -1)
[Special Topic 3.5]
Part 2 – Decisions
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least two exercises during the lab, and the remaining ones at home.
07JCJLI Computer Sciences, A.Y. 2022/23 Lab03
3
03.2.1 Trends. Write a program that reads three numbers and displays the message "increasing" if
they are in strictly increasing order, "decreasing" if they are in strictly decreasing order, and
"neither" if they are in neither increasing nor decreasing order. "Strictly increasing" means that each
value must be greater than the previous one (similar meaning has the term decreasing): the
sequence 3 4 4, thus, it is not “increasing”. [P3.5]
03.2.2 Grades. Write a program that translates a letter grade entered by the user into the
corresponding numerical grade and prints it. The letter grades are 'A', 'B', 'C', 'D' and 'F',
possibly followed by a + or – sign. Their numerical values are, in order, 4.0, 3.0, 2.0, 1.0 and
0.0. 'F+' and 'F–' grades do not exist. A + sign increases the numerical grade by 0.3, while a –
sign decreases it by the same amount. The 'A+' grade is equal to 4.0. [P3.12]
03.2.3 Seasonal cycles. The following algorithm (already seen in exercise 01.1.2) identifies the
season (Spring, Summer, Fall or Winter, i.e., spring, summer, fall or winter, respectively) to which a
date belongs, given as month and day.
If month is 1, 2 or 3
season = “Winter”
Otherwise if month is 4, 5 or 6
season = “Spring”
Otherwise if month is 7, 8 or 9
season = “Summer”
Otherwise if month is 10, 11 or 12
season = “Fall”
If month is divisible by 3 and day >= 21
If season is “Winter”
season = “Spring”
Otherwise if season is “Spring”
season = “Summer”
Otherwise if season is “Summer”
season = “Fall”
Otherwise
season = “Winter”
Take back the analysis of the algorithm and then write a program that, by implementing it, asks the
user for a month and a day and, then, displays the season determined by this algorithm, verifying its
correctness. [P3.20]
03.2.4 Leap years. A 366-day year is called a leap year and is used to keep the calendar synchronized
with the Sun, since the Earth revolves around it once every 365.25 days or so. In reality, this number
is not accurate, and for all dates after 1582 the Gregorian correction applies: usually years divisible
by 4, such as 1996, are leap years, but years divisible by 100, such as 1900, are not; as an exception
to the exception, years divisible by 400, such as 2000, are leap years. Write a program that asks the
user for a year (greater than 1582) and determines whether it is a leap year using a single if
construct and Boolean operators. [P3.27]
03.2.5 Grades again. Given the numerical values of the grades explained in exercise 03.2.2, write a
program that translates a number between 0.0 and 4.0 into the literal grade closest to it. For
example, the number 2.8 (which could be the average of several grades) should be translated as
'B-'. Resolve cases of equality in favor of the better grade: for example, 2.85 should be translated
as 'B'. [P3.13]
07JCJLI Computer Sciences, A.Y. 2022/23 Lab03
4
03.2.6 Taxes. Write a program that calculates taxes according to the following scheme. The program
should acquire the value of the income from the user, and print the taxes due. It is not required to
print intermediate steps. [P3.25]
for civil status "unmarried" and
taxable income higher than but not higher than taxes are
of the sum in
excess of
$ 0 $ 8000 10% $ 0
$ 8000 $ 32 000 $ 800 + 15% $ 8 000
$ 32 000 $ 4 400 + 25% $ 32 000
for civil status "married" and
taxable income higher than but not higher than taxes are
of the sum in
excess of
$ 0 $ 16 000 10% $ 0
$ 16 000 $ 64 000 $ 1 600 + 15% $ 16 000
$ 64 000 $ 8 800 + 25% $ 64 000
03.2.7 Conversions. Write a program for the conversion of units of measurement. It asks the user
for: the starting unit of measurement (choosing from: ml, l, g, kg, mm, cm, m, km); the unit of
measurement to which it wants to convert (choosing from: fl, oz, gal, oz, lb, in, ft, mi),
rejecting incompatible conversions (such as, for example, km to gal); the value to be converted. The
program is supposed to display the data entered and the value resulting from the conversion.
[P3.26]
03.2.8 Shopping vouchers. A supermarket rewards its customers with shopping vouchers whose
amount depends on the amount of money spent on food. For example, if you spend $50, you get a
shopping voucher equal to 8% of the amount you spent. The table below shows the percentage used
to calculate the shopping voucher relative to different amounts. Write a program that calculates and
displays the value of the shopping voucher given to the customer, based on the amount of money he
or she spent on the purchase of groceries. [P3.40]
Money spent Percentage of the voucher
Less than $ 10 No voucher
From $ 10 to $ 60 8%
From more than $ 60 to $ 150 10%
From more than $ 150 to $ 210 12%
More than $ 210 14%
03.2.9 Wavelengths. Write a program that asks the user as input a wavelength value (real number,
which can be written in scientific notation, e.g., 1.23e-7), and displays the description of the
corresponding part of the electromagnetic spectrum, as shown in the table below. [P3.43]
07JCJLI Computer Sciences, A.Y. 2022/23 Lab03
5
Type Wavelength (m) Frequency (Hz)
Radio waves > 10−1 < 3 × 109
Microwaves 𝐹𝑟𝑜𝑚 10−3
𝑡𝑜 10−1 𝐹𝑟𝑜𝑚 3 × 109
𝑡𝑜 3 × 1011
Infrared 𝐹𝑟𝑜𝑚 7 × 10−7
𝑡𝑜 10−3 𝐹𝑟𝑜𝑚 3 × 1011 𝑡𝑜 4 × 1014
Visible light 𝐹𝑟𝑜𝑚 4 × 10−7
𝑡𝑜 7 × 10−7 𝐹𝑟𝑜𝑚 4 × 1014 𝑡𝑜 7.5 × 1014
Ultraviolet 𝐹𝑟𝑜𝑚 10−8
𝑡𝑜 4 × 10−7 𝐹𝑟𝑜𝑚 7.5 × 1014 𝑡𝑜 3 × 1016
X-Rays 𝐹𝑟𝑜𝑚 10−11 𝑡𝑜 10−8 𝐹𝑟𝑜𝑚 3 × 1016 𝑡𝑜 3 × 1019
Gamma rays < 10−11 > 3 × 1019
03.2.10 Back to the comet. A person on average can jump off the ground with a speed of 11
kilometers per hour without having to fear leaving the Earth's surface. Conversely, if a person
jumped with the same speed while on Halley's Comet, would he or she be able to return to the
surface? Create a program that allows the user to input a launch speed (in kilometers per hour) from
the surface of Halley's Comet, and determine whether the person jumping will be able to return to
the surface. If not, the program will need to calculate how much more mass the comet would have
to have for that to happen.
Hint: the escape velocity is equal to
𝜐𝑒𝑠𝑐𝑎𝑝𝑒 = √2
𝐺 𝑀
𝑅
,
where 𝐺 =  6.67  ×  10 −11 𝑁 𝑚2
/ 𝑘𝑔
2
is the gravitational constant, 𝑀 is the mass of the celestial
body, and 𝑅 is the radius. Halley’s Comet has a mass of 2.2  × 1014 𝑘𝑔 and a diameter of 9.4 𝑘𝑚 .
[P3.52]
14BHD Informatica, A.A. 2022/23 Lab04
1
-Laboratory Exercise 04
Topics
1. while and for loops
2. Elaboration of complex inputs
3. Simulations
Discussions
A. Discuss similarities and differences among the two following groups of instructions:
a. if, elif, and else.
b. while and for.
B. What is an infinite loop?
C. What is a simulation?
Exercises
Part 1 – Basic loops
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least two exercises during the lab session, and the rest at home.
04.1.1 Integer numbers. Write a program reading a sequence of integer numbers (an empty string is
the end of the sequence) and, after each input, executing and visualizing:
I. Partial sums of every number acquired; the program must visualize the result of the
calculations after each input.
As an example, if the input values are 1 7 2 9, the program shall visualize the partial sum
of the numbers acquired after each input:
a. After the first input (1), the first acquired value: 1.
b. After the second input (7), the sum between the first and the second acquired
values: 1 + 7 = 8.
c. After the third input (2), the sum between the first, the second, and the third
acquired values: 1 + 7 + 2 = 10.
d. After the fourth input (9), the sum between the first, the second, the third, and the
fourth values acquired: 1 + 7 + 2 + 9 = 19.
II. The minimum and the maximum values among the acquired ones.
III. How many acquired values are even, how many acquired values are odd. [P4.2]
04.1.2 String analysis. Write a program that takes as an input a line of text as a string and outputs
the following requests:
I. Only the capital letters in the string.
II. The letters in the string in even positions.
III. The same string with vowels (uppercase and lowercase) replaced by an underscore (_).
IV. How many digits are contained in the string.
V. The positions of all vowels in the string. [P4.3]
14BHD Informatica, A.A. 2022/23 Lab04
2
04.1.3 Shapes. Write a program that takes as an input an integer number n and prints a square and a
rhombus filled with asterisks (*), with each side long n asterisks. Example: using n=4, the program
shows:
****
****
****
****
 *
 ***
*****
*******
*****
 ***
 *
[P4.22]
04.1.4 Words in reverse. Write a program that reads a word and outputs:
I. The reversed word. If the user writes the string 'Hello', the program shall output
'olleH' [P4.9]
II. The uppercase letters starting from the end. If the user writes the string 'HeLlO', the
program shall output 'OLH'.
04.1.5 Prime numbers. Write a program that asks the user for an integer number and shows as an
output a message showing whether the input number is prime.
04.1.6 Prime numbers. Write a program that asks the user for an integer number and shows all the
prime numbers lower or equal to that number. Example: if the user inputs 20, the program shall
output:
2
3
5
7
11
13
17
19
[P4.17]
04.1.7 Words and spaces. Write a program reading a word and showing all its substring, sorted by
increasing length. If the user inputs the string 'rum', the program shall output:
r
u
m
ru
um
rum
[P4.12]
14BHD Informatica, A.A. 2022/23 Lab04
3
04.1.8 Duplicate numbers. Write a program reading a sequence of integer numbers (the sequence
ends with an empty line) and, after each acquisition, compute and shows only the adjacent duplicate
numbers.
Example: if the input sequence at step IV are the values 1 3 3 4 5 5 6 6 6 3, the program shall
output the adjacent numbers repeated at least two times; at the end of the sequence of equal
numbers (after acquiring the first different number), it shall print:
I. Nothing at the first input (1), as it is the first value.
II. Nothing at the second input (3), as the adjacent values 1 and 3 are not duplicates (equal).
III. Nothing after the third input (3), as the acquired value is the duplicate of the previous one,
and the sequence of duplicate numbers may not be terminated yet.
IV. The value 3 after the fourth input (4), as the two latest adjacent values (3 and 4) are not
duplicated anymore; thus, the sequence of duplicate adjacent numbers is terminated, and
the program shall output the duplicate number.
According to this logic, the sequence 1 3 3 4 5 5 6 6 6 3 produces, in the end, the following
values: 3 5 6. [P4.2]
Part 2 – Application of loops
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least one exercise during the lab session, and the rest at home.
04.2.1 The game of Nim. In this game, two players alternate extracting marbles from a pile. At each
round, the number of marbles taken is up to the player, providing it is at least one, and at most half
of the number of marbles currently available. The player that takes the last marble loses.
Write a program allowing a user to play against the computer. The program shall:
I. Generate a random number between 10 and 100 to use as the quantity of marbles in the
pile in the beginning of the game.
II. Generate a random number, either 0 or 1, to decide whether the first move is on the player
or on the computer.
III. Generate a random number, either 0 or 1, to decide if the computer must play in a smart or
dumb way:
a. By playing dumb, on every move the computer takes a random number of marbles
from the sack (between 1 and n/2, given n as the current number of marbles left in
the pile).
b. By playing smart, it takes a number of marbles so that the number of the remaining
ones is a power of 2 diminished by 1 unit, meaning: 3, 7, 15, 31 o 63. This move is
always valid, except when the number of marbles is equal to a power of 2
diminished by 1. If such is the case, it randomly plays a valid move.
You can experimentally verify that the computer cannot be beat in smart mode, unless the initial pile
contains 15, 31 or 63 marbles. The same goes for human players: if the player draws first and
knows this strategy, the computer cannot win. [P4.23]
14BHD Informatica, A.A. 2022/23 Lab04
4
04.2.2 Image diagnostics. The radioactive decay of radioactive material can be modelled through the
following equation: 𝐴 = 𝐴0𝑒
−𝜆𝑡
, where 𝐴 is the quantity of the material at time 𝑡, 𝐴0 is the
quantity of the material at time 0 , and 𝜆 is the decay rate. More precisely 𝜆 =
ln 2
𝑇1
2
⁄
, where 𝑇1
2
⁄
is
the half-life of the substance (expressed in the same unit of measure of 𝑡).
Technetium-99 is a radioisotope used for diagnostics of brain images. It has a half-life of 6 hours.
Write a program showing the relative quantity 𝐴/𝐴0 in a patient body for each hour during the 24
hours next to the administration of the dose. [P4.39]
04.2.3 Trajectories. A cannonball is launched through the air with starting velocity 𝜐0. Physics books
say that the position of the cannonball after 𝑡 seconds is 𝑠(𝑡) = −
1
2
𝑔𝑡
2 + 𝜐0𝑡, where 𝑔 =
9.81 𝑚/𝑠
2
is the gravitational acceleration of Earth. However, no book mentions that this is a
dangerous experiment, so we may not want to perform it; however, we’re going to do that anyways,
thanks to our computers, assessing theory through a simulation. In our simulation, we are going to
consider very small time intervals Δ𝑡 . In a small time interval, velocity 𝜐 is almost constant, and we
can consider the distance travelled as Δ𝑠 = 𝜐Δ𝑡 . Write a program that, using the constant
DELTA_T = 0.01 (seconds), updates the position of the cannonball using the following formula:
s = s + v * DELTA_T.
Velocity is continuously changing, as the Earth gravitational force decreases it. In a small time
interval, Δ𝜐 = − 𝑔Δ𝑡 . Thus, we can update velocity using the following formula:
v = v – g * DELTA_T.
In each iteration, we must use the new value for the velocity to update the computation of the
travelled distance. The program shall continue the execution of the simulation up until the
cannonball falls to the ground. The program takes the initial velocity as an input (example: 100
m/s). It updates the velocity 100 times per each simulated second, but shows the current velocity
only once per simulated second, together with the value computed through the exact formula
𝑠(𝑡) = −
1
2
𝑔𝑡
2 + 𝜐0𝑡, for comparison.
Note: What is the advantage of simulating a phenomenon when we already have the exact formula?
The point is that the formula is not actually exact. Gravity acceleration is different at different
altitudes or distances from Earth. This is not represented in the formula, while our simulation might
be extended to include this observation. Thus, simulation is necessary for trajectories of objects
flying higher than usual, such as missiles. [P4.37]
14BHD Computer science, A.A. 2022/23 Lab05
1
-Laboratory Exercise 05
Topics
1. Using conditional constructs to make decisions (Lab03 review)
a. Processing and comparisons variables with values of type int, float and str
b. Boolean expressions
c. Logical choices
d. Conditional constructs (if, else, e elif)
e. Blocks and nested instructions
2. Use of loops for repeated execution of instructions (Lab04 review)
a. Loops with while and for statements
b. Complex input processing
c. Simulations
Discussions
A. What is a good strategy for creating a solution to a complex problem?
B. How can I understand if the program implementing the solution is working correctly?
Exercises
Part 1 – Basic loops
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least two exercises during the lab session, and the rest at home.
05.1.1 ATM. When you use an automated teller machine (ATM) with your bank card, you need to use
a personal identification number (PIN) to access your account. If a user fails more than three times
when entering the PIN, the machine will block the card. Assume that the user’s PIN is “1234” and write
a program that asks the user for the PIN no more than three times, and does the following:
• If the user enters the right number, print a message saying, “Your PIN is correct”,
and end the program.
• If the user enters a wrong number, print a message saying, “Your PIN is incorrect”
and, if you have asked for the PIN less than three times, ask for it again.
• If the user enters a wrong number three times, print a message saying “Your bank card
is blocked” and end the program.
[P3.39]
05.1.2 Noms des pays. French country names are feminine when they end with the letter e, masculine
otherwise, except for the following which are masculine even though they end with e:
• le Belize
• le Cambodge
• le Mexique
• le Mozambique
• le Zaïre
• le Zimbabwe
14BHD Computer science, A.A. 2022/23 Lab05
2
Write a program that reads the French name of a country and adds the article: “le” for masculine or
“la” for feminine, such as “le Canada” or “la Belgique”.
However, if the country name starts with a vowel, use “l’”; for example, “l’Afghanistan”.
For the following plural country names, use “les”:
• les Etats-Unis
• les Pays-Bas
[P3.30]
05.1.3 Factoring of integers. Write a program that asks the user for an integer and then prints out all
its factors. For example, when the user enters 150, the program should print
2
3
5
5
[P4.16]
05.1.4 At cinema. Write an application to pre-sell a limited number of cinema tickets. Each buyer can
buy as many as 4 tickets. No more than 100 tickets can be sold. Implement a program that prompts
the user for the desired number of tickets and then displays the number of remaining tickets. Repeat
until all tickets have been sold, and then display the total number of buyers.
[P4.33]
Part 2 – Applications loops
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least one exercise during the lab session, and the rest at home.
05.2.1 Random generator. A simple random generator is obtained by the formula
𝑟𝑛𝑒𝑤 = (𝑎 × 𝑟𝑜𝑙𝑑 + 𝑏) % 𝑚
where 𝑎 , 𝑏 , 𝑟 and 𝑚 are integers; moreover, the value rnew is equal to rold in the following
computation. Write a program that asks the user to enter an initial value for rold. Then print the first
100 random integers generated by this formula, using a = 32310901, b = 1729, and m = 224.
[P4.27]
05.2.2 The Drunkard’s Walk. A drunkard in a grid of streets randomly picks one of four directions and
stumbles to the next intersection, then again randomly picks one of four directions, and so on. You
might think that on average the drunkard doesn’t move far because the choices cancel each other out,
but that is actually not the case. Represent locations as integer pairs (x, y). Implement the drunkard’s
walk over 100 intersections, starting at (0,0), and print the ending location.
[P4.24]
05.2.3 Predator-prey simulation. The Lotka-Volterra equations describe a predator-prey ecological
model that is based on a set of fixed positive constants:
• A. the growth rate of prey;
• B. the rate of destruction of prey by predators;
• C. the mortality rate of predators);
• D. the rate of increase of predators through the consumption of prey.
14BHD Computer science, A.A. 2022/23 Lab05
3
Considering these constants, the following conditions hold in this model:
I. a population of prey x increases at a rate dx=Ax dt (proportional to the number of prey) but
is simultaneously destroyed by predators at a rate dx=− B xy dt (proportional to the
product of the numbers of prey and predators);
II. a population of predators y decreases at a rate dy = − C y dt dy = − C y dt (proportional to
the number of predators), but increases at a rate dy = D xy dt (proportional to the product
of the number of prey and predators).
From these conditions, the system of differential equations derives:
dx/dt =Ax − Bxy
dy/dt =−Cy + Dxy
This means that, considering two time periods n and n + 1, the variation in the number of populations
of prey (x) and predators (y), respectively, from one period to the next is given by:
xn+1 = xn×(1+A−B×yn)
yn+1 = y×(1−C+D×xn)
Write a program that asks the user the input values of the four constants, the initial number of prey
and predators’ populations, and the number of periods to be simulated. After, the program calculates
and display the number of the two populations in each of the periods considered. As test input, use A
= 0.1, B = 0.01, C = 0.01 and D = 0.00002, with initial populations of prey and predators of
1000 and 20, respectively.
[P4.36]
05.2.4 Electrical transformers. Transformers are often built by winding coils of wire around a ferrite
core. The figure illustrates a situation that occurs in various audio devices such as cell phones and
music players and music players. In this circuit, a transformer is used to connect a speaker to the
output of an audio amplifier to the output of an audio amplifier.
The symbol used to represent the transformer is intended to suggest two coils of wire. The parameter
n of the transformer is called the “turns ratio” of the transformer. (The number of times that a wire is
wrapped around the core to form a coil is called the number of turns in the coil. The turns ratio is
literally the ratio of the number of turns in the two coils of wire.)
When designing the circuit, we are concerned primarily with the value of the power delivered to the
speakers—that power causes the speakers to produce the sounds we want to hear. Suppose we were
to connect the speakers directly to the amplifier without using the transformer. Some fraction of the 
14BHD Computer science, A.A. 2022/23 Lab05
4
power available from the amplifier would get to the speakers. The rest of the available power would
be lost in the amplifier itself. The transformer is added to the circuit to increase the fraction of the
amplifier power that is delivered to the speakers. The power, Ps, delivered to the speakers is
calculated using the formula
𝑃𝑠 = 𝑅𝑠 (
𝑛𝑉𝑠
𝑛
2𝑅0 + 𝑅𝑠
)
2
Write a program that models the circuit shown and varies the turns ratio from 0.01 to 2 in 0.01
increments, then determines the value of the turns ratio that maximizes the power delivered to the
speakers.
[P4.40]
14BHD Computer Sciences, A.Y. 2022/23 Lab06
1
-Laboratory Exercise 06
Topics
1. Design and implementation of functions
a. Passing parameters
b. Use of return statement
2. Gradual refinement (Stepwise refinement) to break down complex operations into simpler
ones
a. Design of multiple functions to be used together
b. visibility (scope) of a variable
Discussion
A. What does it mean that the user of a function can consider it as a "black box?
B. What is the difference between returning a value and generating an output value for a
function?
C. How can you make a function reusable?
D. What is the scope of visibility of a variable?
Exercises
Part 1 – Single functions
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least two exercises during the laboratory session and the rest at home.
06.1.1 Speech Count. Write the function:
def count_vowels(string)
Returns the number of vowels in the string. Vowels are the letters a, e, i, o, and u; as well as
their respective capitalized versions. [P5.6]
06.1.2 Word Count. Write the function:
def count_words(string)
Returns the number of words in the string. Words are sequences of characters separated by
spaces (assume that between two consecutive words, there is exactly one space). For example,
count_words("Mary had a little lamb") returns 5.
How could the exercise be extended so that strings, where there are multiple spaces between
words, are correctly treated? [P5.7]
06.1.3 Geometric solids. Write functions:
def sphere_volume(r)
def sphere_surface(r)
14BHD Computer Sciences, A.Y. 2022/23 Lab06
2
def cylinder_volume(r, h)
def cylinder_surface(r, h)
def cone_volume(r, h)
def cone_surface(r, h)
To calculate the volume and surface area of a sphere of radius r, a cylinder with a circular base of
radius r and height h and a cone with a circular base with radius r and height h. Then write a
program that asks the user to enter the values r and h, then the program calls the six functions and
display the output results. [P5.9]
06.1.4 Bank Balance. Write a function that calculates the balance of a bank account by crediting
interest annually. The function receives as parameters: the number of years, the initial balance, and
the annual interest rate. [P5.22]
Part 2 – Algorithms that make use of functions
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least one exercise during the laboratory session and the rest at home.
06.2.1 NGOs. A non-governmental organization needs a program to calculate the share of financial
benefit to be allocated to each family in need of assistance. The formula is as follows:
I. If the family's annual income is between $30000 and $40000 and the family has at least 3
children, the subsidy is $1000 for each child;
II. If the family's annual income is between $20000 and $30000 and the family has at least 2
children, the subsidy is $1500 for each child;
III. If the family's annual income is less than $20,000, the subsidy is $2,000 for each child.
Write a function to perform these calculations. Then write a program that, in a cycle, asks the user to
provide the annual income and the number of children of each family requesting the subsidy,
displaying the corresponding value returned by the function. Use –1 as the sentinel value to finish
entering data. [P5.28]
06.2.2 Roman numerals. Write a program that converts a Roman numeral, such as MCMLXXVIII,
into its decimal representation.
Tip: First, write a function that returns the numeric value of each individual letter, then use the
following algorithm:
total = 0
s = string corresponding to the Roman numeral
Until s is empty
If s has length 1, or the value of its first character is greater than or equal to the value of its
second character
Add the value of the first character of s to the total
Remove the first character from s
Otherwise
difference = (value of the second character of s) – (value of the first character of s)
Add the difference value to the total
Remove the first two characters from s
[P5.27]
14BHD Computer Sciences, A.Y. 2022/23 Lab06
3
06.2.3 Aerodynamic drag. The drag force on a car is given by:
𝐹𝐷 =
1
2
𝜌𝜐
2𝐴𝐶𝐷
Where 𝜌 is the air density (1,23 𝑘𝑔/𝑚3
), 𝜐 is the velocity in 𝑚/𝑠, 𝐴 is the projected area of the car
(2,5 𝑚2
) and 𝐶𝐷 is the drag coefficient (0,2 ). The amount of power in watts needed to overcome
the resistance force is 𝑃 = 𝐹𝐷𝜐 , and the equivalent power in horsepower is 𝐻𝑝 = 𝑃/745.7. Write a
program that receives the car's speed and calculates the power in watts and horsepower needed to
overcome the resulting resistance force. [P5.36]
06.2.4 Electrical wire. The electric wire is a cylindrical conductor covered with an insulating material.
The resistance of a wire is given by the formula:
𝑅 =
𝜌𝐿
𝐴
=
4𝜌𝐿
𝜋𝑑
2
Where 𝜌 is the resistivity of the conductor 𝐿 and 𝐴, and 𝑑 are the length, cross-sectional area, and
wire diameter, respectively. The resistivity of copper is (1.678 × 10−8 Ω𝑚 ). The diameter 𝑑 of the
wire, is commonly specified by the American Wire Gauge (AWG), which is an integer value. The
diameter of an AWG- 𝑛 wire is given by the formula:
𝑑 =  0.127 × 92
36 − 𝑛
39 𝑚𝑚
Write a function
def diameter(wire_gauge)
that accepts the wire gauge and returns the corresponding diameter. Write another function
def copper_wire_resistance(length, wire_gauge)
that accepts the length and caliber of a piece of copper wire and returns its resistance.
The resistivity of aluminum is 2,82 × 10−8 Ω𝑚 . Write a third function
def aluminum_wire_resistance(length, wire_gauge)
that accepts the length and caliber of a piece of aluminum wire and returns its resistance. Then write
a program to test these functions. [P5.35]
14BHD Computer Sciences, A.Y. 2022/23 Lab07
1
Laboratory Exercise 07
Topics
1. Lists of items
2. Use the for loop to scroll through a list
3. Functions that use lists
Discussion
A. What is a list?
B. What are the differences between an element of a list, and its index?
C. What list's information is needed to scroll it without making mistakes?
Exercises
Part 1 – Elaboration of lists
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least two exercises during the laboratory session and the rest at home.
07.1.1 Sum with alternating signs. Write a program that receives as input a sequence of integers
(terminated by an empty line), and that calculates the alternating sum of its elements. For example, if
the program reads the data 1 4 9 16 9 7 4 9 11, it must calculate and display 1 - 4 + 9 -
16 + 9 - 7 + 4 - 9 + 11 = –2. [P6.8]
07.1.2 List of random numbers. Write a program that initializes a list with ten random integers
between 1 and 100 and then displays, on four successive lines:
I. All elements of even index;
II. All the elements that are even;
III. All elements in reverse order;
IV. The first and the last element.
[P6.1]
07.1.3 Remove the minimum value. Write a remove_min(v) function that removes the minimum
value from a v list without using the min() function or the remove() method. [P6.7]
07.1.4 Local highs. Read a sequence of integers ended by a blank line. Print the position of the local
maxima (numbers greater than both the previous and the next value) if there are any, otherwise print
the message 'There are no local maxima'. Extension: if there are several pairs of local maxima,
identify the two closest local maxima and print their position.
07.1.5 The same elements. Write the same_set(a, b) function that checks if two lists contain the
same elements, regardless of the order and ignoring the presence of duplicates. For example, the 
14BHD Computer Sciences, A.Y. 2022/23 Lab07
2
two lists 1 4 9 16 9 7 4 9 11 and 11 11 7 9 16 4 1 must be considered equal. The
function must not modify the lists that have been passed as parameters. [P6.12]
07.1.6 Ordered list. Write a program that generates a sequence of 20 random integer values between
0 and 99, then displays the generated sequence, orders it, and displays it again, sorted. Use the
sort() method. [P6.17]
07.1.7 Add up without the minimum. Write the sum_without_smallest(v) function that
calculates the sum of all the values of a list v, excluding the minimum value. [P6.6]
Part 2 – Algorithms that make use of lists
Delivery: For each of the following exercises, write a program in Python that responds to the requests
indicated. Complete at least one exercise during the laboratory session and the rest at home.
07.2.1 Measurement noise. Often the data collected during an experiment has to be processed to
remove some of the measurement noise. A simple approach to this problem involves replacing, in a
list of values, each value with the average between the same value and the two adjacent values (or of
the only adjacent value if the value under consideration is at one of the two ends of the list). Write a
program that does this, without creating a second list. [P6.36]
07.2.2 Distances. People who park their car in a row of parking lots usually prefer to maximize the
distance between the seat they occupy and the seats that are already occupied by other vehicles. They
therefore tend to occupy the central seat of the longest row of free seats available. For example,
consider the situation where ten seats are free:
_ _ _ _ _ _ _ _ _ _
The first person to arrive will occupy, with their vehicle, a seat in the central part of the row:
_ _ _ _ _ X _ _ _ _
The next person will place it in the middle of the longest vacated row (i.e. the one on the left):
_ _ X _ _ X _ _ _ _
Write a program that receives as input the number of parking spaces that make up the row of parking
spaces and that, each time a new space is occupied according to the rule indicated, displays the row
in the format indicated above. Tip: Use a list of Boolean values to indicate whether a parking space is
occupied or not. [P6.19]
14BHD Computer Sciences, A.Y. 2022/23 Lab07
3
07.2.3 Bulgarian solitaire. The Bulgarian Solitaire game starts with 45 cards. The cards are randomly
divided into a given number of randomly sized piles. For example, you can start with 5 piles of sizes
20, 5, 1, 9 and 10. Each turn, one card is subtracted from each pile, and a new pile is created
made up of the cards subtracted from the starting piles. For example, the starting configuration would
be transformed into stacks of sizes 19, 4, 8, 9 and 5. The game ends when the stacks have sizes
1, 2, 3, 4, 5, 6, 7, 8 and 9 (yes can show that you always get such a configuration). Write
a program that generates a random initial setup and displays it, and then continues with the solitaire
steps, displaying the setup after each step, and stopping when you reach the final solitaire setup.
[P6.20]
07JCJLI Computer Sciences, A.Y. 2022/23 Lab08
1
Laboratory 08
Topics
1. Lists
2. Tables
Discussion
A. Discuss similarities and differences between lists and tables
B. Describe the use of the indexes in:
a. strings;
b. lists;
c. tables.
C. How can you prevent an out-of-range error?
Esercizi
Part 1 – List and tables elaboration
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least two exercises during the laboratory session, and the remaining ones
at home.
08.1.1 Out-of-range. Write a program that contains an out-of-range error. What happens if
you run the program? [R6.10]
08.1.2 Buffer. Write the pseudocode for an algorithm that, given a list of defined length, moves the
elements "forward" one position (thus increasing their index by one unit), and moves the element at
the last position to the first position. For example, the list 1 7 9 3 0 4, after this operation,
becomes the list: 4 1 7 9 3 0. Write a program implementing the above described algorithm.
[R6.17]
08.1.3 Play dice. Write a program that generates a sequence of 20 random rolls of a dice, stores
them into a list and displays the generated values marking the longest set of identical values with
the following format:
1 2 5 5 3 1 2 4 3 (2 2 2 2) 3 6 5 5 6 3 1
If there are multiple sequences of identical values of maximum length, use the formatting shown to
highlight the first in order of occurrence. [P6.16]
08.1.4 Table. Write the instructions for the execution of the following operation for a table in Python
of 𝑚 rows and 𝑛 columns (dimensions are inserted by the user):
I. Initialize the table with values equal to zero (0);
II. Fill all the cells with values equal to one (1);
III. Fill the cells alternating 0 and 1 in a chess scheme;
IV. Fill with 0 only the cells of the upper row and of the lower one, leaving the rest of the table
unchanged;
07JCJLI Computer Sciences, A.Y. 2022/23 Lab08
2
V. Fill with 1 only the cells of the right column and of the left column, leaving the rest of the
table unchanged;
VI. Calculate and display the sum of all the elements.
After each operation, display the table. [R6.28]
08.1.5 Lists union. Write a function merge(a, b) that merges the two lists a and b, alternating
one element of the first and one element of the second. If one list is shorter than the other, the
items are alternated as long as possible, then the items left in the longer list are added, in order, to
the bottom. Starting lists should not be changed. If, for example, the content of a is 1 4 9 16
and the content of b is 9 7 4 9 11, the invocation of merge(a, b) return a new list composed
of the following values: 1 9 4 7 9 4 16 9 11. [P6.30]
08.1.6 Sorted lists union. Write a function merge_sorted(a, b) that merges two lists (which
are assumed to be already sorted ascending), returning a new, ascending sorted list. Manage a
current index for each list to keep track of portions already processed. Starting lists should not be
modified. If, for example, the content of a is 1 4 9 16 and the content of b is 4 7 9 9 11, the
invocation of merge_sorted(a, b) return a new list composed of the following values: 1 4 4 7
9 9 9 11 16. The method sort() and the function sorted() must not be used. [P6.31]
Parte 2 – Algorithms using lists and tables
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercise during the laboratory session, and the remaining ones
at home.
08.2.1 On average. Write the function neighbor_average(values, row, column) that, in a
table values, calculates the average value of an element's neighbors in the eight directions,
indexed as shown in the figure below (excluding the element itself). If, however, the element is on
an edge of the table, the average should be calculated by considering only those neighbors that
actually belong to the table. For example, if row and column are both 0, the element has 3
neighbors. [P6.23]
[i -1] [j - 1] [i - 1] [j] [i - 1] [j + 1]
[i] [j - 1] [i] [j] [i] [j + 1]
[i + 1] [j - 1] [i + 1] [j] [i + 1] [j + 1]
07JCJLI Computer Sciences, A.Y. 2022/23 Lab08
3
08.2.2 Magic squares. A 𝑛 × 𝑛 matrix containing the integer numbers 1,  2,  3, … , 𝑛
2 is a “magic
square” if the sum of its elements in each row, in each column, and in the two diagonals is the same.
For example, this is a magic square of size 4:
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
Write a program that acquires by the user 16 values, and places them in a table of 4 × 4 in order,
one row at a time from top to bottom, and in each row from left to right, and check whether, after
placing them, they form a magic square. Verify two properties:
I. All and only the numbers 1, 2, ..., 16 are present in the acquired data.
II. When the numbers are placed in the table, the sums of the rows, columns and diagonals are
all equal to each other. [P6.21]
08.2.3 Tic-tac-toe. Write a program that plays the tic-tac-toe game. The game of tic-tac-toe is played
on a 3 × 3 grid. The game is played by two human players taking turns. The first player marks the
moves with a circle ('o'), the second one with a cross ('x'). The player who has formed a
horizontal, vertical or diagonal sequence of 3 equal symbols. The program must, at each turn,
display the game board, ask the user for the coordinates of the next move symbol (row and column,
numbered from 1 to 3) as input, reverse the players after each move, and, when the game is over,
decree the winner or a tie condition. [P6.28]
X O
X O
O O X
07JCJLI Computer Sciences, A.Y. 2022/23 Lab08
4
08.2.4 Spring. Write a program that models and simulates the motion of an object of mass 𝑚
attached to an oscillating spring. When the spring is displaced from its equilibrium position by a
quantity 𝑥 , Hooke's law states that the restoring force is given by the formula:
𝐹 = −𝑘𝑥
where 𝑘 is a constant depending on the spring. For this simulation, use k = 10 N/m. Start with a
given displacement 𝑥 (i.e., x = 0.5 m). Set the initial speed to v = 0. Calculate the acceleration
𝑎 based on Newton's law (𝐹 = 𝑚𝑎 ) and Hooke's law, using a mass m = 1 kg. Use a small time
interval delta_t = 0.01 s and, at each step, update the speed, by calculating a change of 𝑎Δ𝑡 ,
and the displacement, by calculating a change of 𝑣Δ𝑡 . [P6.38]
07JCJLI Computer Sciences, A.A. 2022/23 Lab09
1
-Laboratory 09
Topics
1. Using conditional constructs for decision making (Lab03 recap)
2. Using cycles to execute repeating instructions (Lab04 recap)
3. Definition and elaboration of lists and tables (Lab08 recap)
Discussion
A. How are conditional constructs used for complex decision making?
B. A complex decision can be based on general and/or more specific conditions. How should
the conditional construct manage them?
C. In cyclic programming, what is an off-by-one error?
D. What is the search algorithm used to find an element in a set of unsorted elements?
E. Which constructor is more suitable to access the elements of a table with rows and
columns?
Exercises
Part 1 – Recap Exercises
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercise during the laboratory session, and the remaining ones
at home.
09.1.1 Lista of functions. Write list functions that carry out the following tasks for a list of integers.
For each function, provide a test program. All the operations must modify the list passed as a
parameter. [P6.4]
I. Swap the first and last elements in the list.
II. Shift all elements by one to the right and move the last element into the first position. For
example, 1 4 9 16 25 would be transformed in 25 1 4 9 16.
III. Replace all even elements with 0.
IV. Replace each element except the first and last by the larger of its two neighbors.
V. Remove the middle element if the list length is odd, or the middle two elements if the length
is even.
VI. Remove the middle element if the list length is odd, or the middle two elements if the length
is even.
VII. Return the second-largest element in the list.
VIII. Return True if the list is currently sorted in increasing order.
IX. Return True if the list contains two adjacent duplicate elements.
X. Return True if the list contains duplicate elements (which need not be adjacent).
09.1.2 Hidden rules. Write a program that, given an empty list l = [], initializes it with each of the
following sequences, after you have understood the rules used to generate them (if they exist):
[R6.1]
I. 1 2 3 4 5 6 7 8 9 10
II. 0 2 4 6 8 10 12 14 16 18 20
07JCJLI Computer Sciences, A.A. 2022/23 Lab09
2
III. 1 4 9 16 25 36 49 64 81 100
IV. 0 0 0 0 0 0 0 0 0 0
V. 1 4 9 16 9 7 4 9 11
VI. 0 1 0 1 0 1 0 1 0 1
VII. 0 1 2 3 4 0 1 2 3 4
09.1.3 Bar chart. Write a program that reads a sequence of input values and displays a bar chart of
the values, using asterisks (*), like this:
**********************
****************************************
****************************
**************************
**************
You may assume that all values are positive. First figure out the maximum value. That value’s bar
should be drawn with 40 asterisks. Shorter bars should use proportionally fewer asterisks. [P6.24]
09.1.4 What about negative numbers? Improve the program of Exercise 09.1.3 to work correctly
when the data set contains negative values. [P6.25]
09.1.5 Caption. Improve the program of Exercise 09.1.3 by adding captions for each bar. Prompt the
user for the captions and data values. The output should look like this:
 Egypt **********************
 France ****************************************
 Japan ****************************
 Uruguay **************************
Switzerland **************
[P6.26]
09.1.6 List of integer numbers. Write a program that reads from input a list of positive integer
numbers provided on single row and separated by the character ':', for example :
3:12:21:8:4:7. The program must print, maintaining the same format:
I. The input numbers, excluding the maximum and the minimum (for example, 12:8:4:7);
II. Among the inputted numbers, only the even values (for example, 12:8:4);
III. Among the inputted numbers, only the 2-digits numbers (for example, 12:21). 
07JCJLI Computer Sciences, A.A. 2022/23 Lab09
3
Part 2 – Applications
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercise during the laboratory session, and the remaining ones
at home.
09.2.1 The theater. A theater seating chart is implemented as a table of ticket prices, like this:
10, 10, 10, 10, 10, 10, 10, 10, 10, 10
10, 10, 10, 10, 10, 10, 10, 10, 10, 10
10, 10, 10, 10, 10, 10, 10, 10, 10, 10
10, 10, 20, 20, 20, 20, 20, 20, 10, 10
10, 10, 20, 20, 20, 20, 20, 20, 10, 10
10, 10, 20, 20, 20, 20, 20, 20, 10, 10
20, 20, 30, 30, 40, 40, 30, 30, 20, 20
20, 30, 30, 40, 50, 50, 40, 30, 30, 20
30, 40, 50, 50, 50, 50, 50, 50, 40, 30
Write a program that prompts users to pick either a seat or a price. Mark sold seats by changing the
price to 0. When a user specifies a seat, make sure it is available. When a user specifies a price, find
any seat with that price. [P6.27]
09.2.2 Concatenated words. While traveling, a good way to pass time is to play the game
“concatenated words”. The first player starts by telling an initial word, then, in turns, the following
player should tell a word that starts with last 2 letters of the word said by the previous player. It is
forbidden to say a word that has been said in a previous turn. An example is the sequence: 'cat',
'attic', 'ice', 'cerulean', 'animal'. Write a program that allows to manage one or
more games. Each game ends when one of the players enters:
1. a word that has already been said in a previous turn;
2. an invalid word;
3. an asterisk (*) to quit the game. This character can also be inputted when the player is
unable to find a valid word.
09.2.3 The best client. A supermarket wants to reward its best customer of each day, showing the
customer’s name on a screen in the supermarket. For that purpose, the customer’s purchase
amount is stored in a list (customers) and the customer’s name is stored in a corresponding list
(customers). Implement a function:
name_of_best_customer(sales, customers)
that returns the name of the customer with the largest sale.
One you have done that, write a program that prompts the cashier to enter all prices and names,
adds them to two lists, calls the function that you implemented, and displays the result. Use a price
of 0 as a sentinel. [P6.33]
07JCJLI Computer Sciences, A.A. 2022/23 Lab09
4
09.2.4 Spiral. Write a program that asks the user to input a value N, builds a matrix N x N, fills it
with a sequence of integer numbers between 1 and N**2, and prints the resulting table. For
example, if N = 4, the program should print the table on the left, following the instructions shown
in the table on the right (this table should not be an output of your program).
1 2 3 4 ⨀ → → ↴
12 13 14 5 ↱ → ↴ ↓
11 16 15 6 ↑ ⨂ ↵ ↓
10 9 8 7 ↑ ← ← ↵
09.2.5 Pet shop. A pet shop wants to give a discount to its clients if they buy one or more pets and at
least five other items. The discount is equal to 20 percent of the cost of the other items, but not the
pets. Implement a function:
discount(prices, is_pet)
The function receives information about a particular sale and computes the discount to apply. For
the i-th item, prices[i] is the price before any discount, and is_pet[i] is a Boolean variable
that is Trueif the item is a pet.
Once you have done that, write a program that prompts a cashier to enter each price and then a 'Y'
for a pet or 'N' for another item. Use a price of –1 as a sentinel. Save the inputs in a list. Call the
function that you implemented and display the discount. [P6.32]
09.2.6 Flooding. You are given a 𝑁 × 𝑁 table heights of real values that give the height of a
terrain at different points in a square. Write a function:
flood_map(heights, water_level)
that prints out a flood map, showing which of the points in the terrain would be flooded if the water
level reaches the value water_level. The flood map is an 𝑁 × 𝑁 table of strings, each composed
by a single character. In the flood map, print a '*' for each flooded point and a space ' ' for each
point that is not flooded. Here is a sample map:
* * * * * *
* * * * * * * *
* * * * * *
* * * * * * *
* * * * * * * *
* * * * * * * * * *
* * * * * * *
* * * * * *
 * *
 
07JCJLI Computer Sciences, A.A. 2022/23 Lab09
5
Once you have done that, write a program that builds a 10x10 height matrix, reading one hundred
terrain height values and shows how the terrain gets flooded when the water level increases in 10
steps from the lowest point in the terrain to the highest [P6.35]
07JCJLI Computer Sciences, A.Y. 2022/23 Lab10
1
-Laboratory 10
Topics
1. Reading and writing files
2. Exception handling
3. Data processing
Discussion
A. What happens if you try to read or write open a file that does not exist?
B. What is the difference between reporting and handling an exception?
C. What is the difference between sequential access and random access?
Exercises
Part 1 - File Processing
Assignment: for each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercise during the lab session, and the remaining ones at home.
10.1.1 Enola Gay. Write a program that reads the text file input.txt, and writes each line read in
the file output.txt preceded by its line number inserted as a comment between characters '/*'
and ' */'. If, for example, the input.txt file contains the text:
Enola Gay
is the bomber who, on August 6, 1945,
dropped the first atomic bomb on Hiroshima.
nicknamed Little Boy.
the generated output.txt file must contain the text:
/*1*/Enola Gay
/*2*/is the bomber who, on August 6, 1945,
/*3*/dropped the first atomic bomb on Hiroshima.
/*4*/nicknamed Little Boy.
[P7.2]
10.1.2 From the bottom. Write a program that reads all the lines in a text file input.txt, reverses
their order, and writes them to another file output.txt. For example, if the input.txt file
contains the text: 
07JCJLI Computer Sciences, A.Y. 2022/23 Lab10
2
Mary had a little lamb
Its fleece was white as snow
And everywhere that Mary went
The lamb was sure to go.
the generated output.txt file must contain the text:
The lamb was sure to go.
And everywhere that Mary went
Its fleece was white as snow
Mary had a little lamb
[P7.9]
10.1.3 Ring Search. Write a program that searches for a given word in the contents of a group of
files. The program must ask the user for input:
I. A list of file names on a single line, separated by commas;
II. A word to search.
File names must be stored in a list, while the word to be searched must be stored in a variable. The
program must display all lines that contain the word, even as a substring of other words, without
distinguishing between uppercase and lowercase letters. Each displayed line must be preceded by
the name of the file in which it is located. For example, if the word to be searched is 'ring,' and the
list contains the files:

book.txt, address.txt, homework.py
then the program, having processed the contents of those files, should display the rows where the
word to be searched is found with the following format:
book.txt: There is only one Lord of the Ring, only one who can bend it to
his will
book.txt: The ring has awoken; it's heard its master's call.
address.txt: Kris Kringle, North Pole
address.txt: Homer Simpson, Springfield
homework.py: string = "text"
[P7.6]
10.1.4 Hotel. The administrative manager of a hotel records sales in a text file. Each line contains the
following 4 information, separated by semicolon characters (';'):
I. the client's name;
II. the service sold;
III. the amount paid;
IV. the date of the event.
The services sold may be, for example, a dinner, a conference, or lodging. The proper format for this
file is for it to contain 4 fields per line, and for the amount paid to contain values of type float. 
07JCJLI Computer Sciences, A.Y. 2022/23 Lab10
3
Write a program that reads this text file, and displays the total amount for each type of service,
reporting an error if the file does not exist or if its format is incorrect. [P7.29]
10.1.5 Second possibility. Write a program that asks the user to enter a series of values of type
float. When the user enters a value that is not of the correct type, the program must give the user
a second chance to enter the value, and after two chances it must stop reading the input,
terminating the program immediately. Data entry continues until the user enters an empty string
('') as input. Sum all correctly specified values and display their sum when the user has finished
entering data. Use exception handling to detect improper input. [P7.13]
Part 2 - Data processing: matching and encryption
Assignment: for each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercise during the lab session, and the remaining ones at home.
10.2.1 Random monoalphabetic cipher. Caesar's cipher is a monoalphabetic substitution cipher, in
which each letter in the plaintext is replaced in the ciphertext by the letter that is a certain number
of positions later in the alphabet. Because the number of positions used for translation is fixed,
Caesar's cipher is too easy to hack. To make the ciphertext more difficult to decipher, an alternative
strategy is to use a word as the key instead of a number. For example, if the word that is used as the
key is FEATHER, first the duplicate letters are removed, yielding FEATHR, and then the remaining
letters of the alphabet are added in the queue, in reverse order. This results in the following
sequence.
F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
Then, the letters are encrypted according to the following scheme.
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓
F E A T H R Z Y X W V U S Q P O N M L K J I G D C B
Any other characters (e.g., spaces, digits, or punctuation marks) must remain unchanged.
Write a program that requests as input from the user the name of a text file to be encrypted or
decrypted, the choice of which operation to perform (encryption or decryption), a keyword, and the
name of a file in which to write the output of the processing. The program must store the keyword
entered by the user in a variable, and use it to encrypt or decrypt the text file provided as input, then
write the result of the processing to the indicated output file. [P7.20]
10.2.2 University transcript. Write a program that displays a list of examinations passed by a
student, with their grades. A classes.txt file is available, which contains the codes for all courses
delivered in the educational institution (a U.S. college), the contents of which will be similar to this
one:
CSC1
CSC2
CSC46
CSC151
MTH121 ...
07JCJLI Computer Sciences, A.Y. 2022/23 Lab10
4
For each course, there is a file whose name corresponds to the course code, followed by '.txt'.
This file lists the people who passed the course exam, showing for each the identification number
('Student ID') and the grade obtained. For example, the file CSC2.txt might contain the text:
11234 A12547 B
16753 B+
21886 C ...
Write a program that prompts the user to enter a 'Student ID' as input, and then displays the
list of passed exams associated with it, reporting the grades obtained for each exam, respecting the
following format.
Student ID: 16753
CSC2 B+
MTH121 C+
CHN1 A PHY50
A-
[P7.28]
10.2.3 Playfair cipher. It is possible to decipher a text by simple analysis of the frequency of
occurrence of individual letters. One way to thwart this strategy is to jointly encrypt pairs of letters.
The Playfair cipher is a simple scheme that applies this strategy. In this scheme, first a keyword is
chosen, and the letters duplicated in it are eliminated. Then you place the keyword thus worked out
in a 5 × 5 checkerboard, followed by the remaining letters of the English alphabet in order. Since
there are only 25 squares and the English alphabet has 26 letters, 'I' and 'J' are considered
indistinguishable. Check that in the source text the letters are even, if not, add a 'Z'. Using 'PLAYFAIR',
transformed to 'PLAYFIR', as the keyword, the following pattern is obtained.
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
07JCJLI Computer Sciences, A.Y. 2022/23 Lab10
5
Starting from this table, to encrypt a pair of letters, e.g., 'AM,' you locate the portion of the table
that has 'A' and 'M' at two ends:
P L A Y F
I R B C D
E G H K M
N O Q S T
U V W X Z
The encoding of the pair 'AM' is done by finding the values at the two remaining ends of the
portion of the table, in this case, 'FH'. If the two letters of the pair are on the same row or on the
same column, such as, the pair 'GO', the encoding is done by swapping the letters with each other,
obtaining, in this case, 'OG'. Decryption follows the same rules. Write a program that encrypts or
decrypts a text file according to the Playfair cipher scheme. [P7.23]
10.2.4 Covalent bonds. Suppose a file contains the energies and bond lengths for covalent bonds,
such as those illustrated by the table below.
Bond (single |, double ||,
or triple |||)
Bond energy
(kJ/mol)
Bond length
(nm)
C|C 370 0.154
C||C 680 0.13
C||C 890 0.12
C|H 435 0.11
C|N 305 0.15
C|O 360 0.14
C|F 450 0.14
C|Cl 340 0.18
O|H 500 0.10
O|O 220 0.15
O|Si 375 0.16
N|H 430 0.10
N|O 250 0.12
F|F 160 0.14
H|H 435 0.074
The format of the file (denoted bond_data.txt) requires that each row in the table correspond to
a row of text, and that, in each row, the three fields are separated by a space (' '), and does not
provide a header. For example, a file containing the data presented in the table might contain the
text:
C|C 370 0.154
C||C 680 0.13
C||C 890 0.12 ... 
07JCJLI Computer Sciences, A.Y. 2022/23 Lab10
6
Write a program that accepts data from one column as input and displays data from the other two
columns in the file. If the input data has a match to multiple rows in the table, the program must
return data from the other two columns to all rows that have a match to the input value. For
example, a bond length of 0.12 must return both triple bond C||C and bond energy 890 kJ/mol,
and single bond N|O and bond energy 250 kJ/mol. [P7.34] 
14BHD Informatica, A.A. 2022/23 Lab11
1
-Laboratory 11
Topics
1. Sets
2. Dictionaries
3. Search in tables
Discussion
A. Discuss common things and differences between:
a. A list;
b. A set;
c. A dictionary.
B. Discuss if a dictionary can have:
a. Two keys with the same value;
b. Two values with the same key.
C. If Python didn’t offer set, but you needed it in a program, what container could you use
instead?
Exercises
Part 1 – Complex data structures
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercises during the laboratory session, and the remaining ones
at home.
11.1.1 Counting words. Write a program counting all occurrences of a word in a text file whose
name is obtained as an input. Assume the file contains only alphabetical characters or white spaces.
The program shall output all the words in the file, with the number of occurrences near each word.
[P8.2]
11.1.2 Most frequent words. Extend the program of exercise 11.1.1 so that it shows the 5 most
frequent words in the file, not including “the”, prepositions and conjunctions. [P8.3]
11.1.3 Two strings. Write a program taking as input two strings, then visualizing (with no
repetitions):
I. Each character appearing in both strings.
II. Each character appearing in only one of the strings.
III. All the alphabetical letters not appearing in any string.
Hint: use set() to turn the string into a set of character. [P8.9]
11.1.4 Censor. Write a ‘censor‘ program, reading a file (bad_words.txt) containing a list of bad
words (come 'sex', 'drugs', 'Python' and so on), a word for each line, reading them into a
set. Then read another file (raw_text.txt), containing some of the bad words read before. The
program shall generate a third file (censored_text.txt) containing the previous text, but with all 
14BHD Informatica, A.A. 2022/23 Lab11
2
words and sub-words censored if they contain bad words, using as many asterisks ('*') as the
length of the bad word. [P8.14]
11.1.5 Sparse vectors. A sparse vector is a sequence of numbers, most of which are 0s. A dictionary
is an efficient structure to memorize a sparse vector; in such a dictionary, keys are positions in which
there are only values different from zero and each value is the number itself. For instance, the
sequence 0 0 0 0 0 4 0 0 0 2 9 can be represented by the dictionary {5:4, 9:2, 10:9}.
Write a function, sparse_array_sum(a, b), whose arguments are two sparse arrays
represented as dictionaries, a and b. Without modifying the parameters, the function shall return
their sum vector as a sparse vector, where each value in the i
th position is the sum of the values of
a and b in each position i. [P8.22]
11.1.6 Sieve of Eratosthenes. The Sieve of Eratosthenes is an iterative algorithm, well known in
Ancient Greece, computing all prime numbers before an integer number n. In each iteration, it
deletes all values multiple of the lowest value present in the set, starting from 2 up to √𝑛. After the
last iteration, only prime numbers remain. Implement a function using the Sieve of Eratosthenes.
First, insert all numbers from 2 to n. Then, eliminate all multiples of 2, except for 2 (as is: 4, 6,
8, 10, 12, and so on, up to n). As a second step, eliminate all multiples of 3, except for 3 (as
is, 6, 9, 12, 15, and so on, up to n). Go on until only prime numbers remain. [P8.4]
Part 2 – Complex operations
Task: For each of the following exercises, write a program in Python that meets the given
requirements. Complete at least one exercise during the laboratory session, and the remaining ones
at home.
11.2.1 Pro capite income. Write a program reading values from the file rawdata_2004.txt
inserting them in a dictionary whose keys are the names of Countries, and the values are the annual
income pro capite. Please, notice that each field is separated by a tabulation character '\t'. Then,
the program shall ask the user to input names of Countries to show each value of pro capite yearly
income. Program shall terminate when the string 'quit' is written. Try also working with
rawdata_2021.csv performing the same exercise. [P8.17]
11.2.2 Genes. In cells, DNA contains fundamental information so that the organism provides all the
functions useful to live. To support the cell functions, instructions in DNA are first transcribed into
RNA molecules. Later, RNA molecules get translated into proteins. Translation from RNA to
messenger RNA (mRNA) to proteins is based on genetic code, which is the set of rules in which a
sequence of nucleotides ('A', 'C', 'U' e 'G') gets translated in a sequence of amino acids for
proteic synthesis. Each amino acid corresponds to one or more sequences of 3 nucleotides, called
codons. The following table1
shows the codon that in mRNA code the 20 ordinary amino acids.
1 Codice genetico (Wikipedia): https://it.wikipedia.org/wiki/Codice_genetico
14BHD Informatica, A.A. 2022/23 Lab11
3
Amino acid Codons Amino acid Codons
Ala GCU, GCC, GCA, GCG Leu UUA, UUG, CUU, CUC, CUA,
CUG
Arg CGU, CGC, CGA, CGG, AGA,
AGG
Lys AAA, AAG
Asn AAU, AAC Met AUG
Asp GAU, GAC Phe UUU, UUC
Cys UGU, UGC Pro CCU, CCC, CCA, CCG
Gln CAA, CAG Ser UCU, UCC, UCA, UCG, AGU,
AGC
Glu GAA, GAG Thr ACU, ACC, ACA, ACG
Gly GGU, GGC, GGA, GGG Trp UGG
His CAU, CAC Tyr UAU, UAC
Ile AUU, AUC, AUA Val GUU, GUC, GUA, GUG
Following codons indicate the start and the end of the translation process. Note, start codon also
codificates Methionine ('Met').
Instruction Codons
start AUG, GUG
stop UAG, UGA, UAA
Write a program elaborating a sequence of mRNA inserted as an input from the user, showing the
sequence of amino acid translated. To simulate the translation problem, use a dictionary
genetic_code, which, reading all info reported as a table in codice_genetico.csv, memorizes
codons and amino acids codified by those codons, choosing opportune keys and values. Then, iterate
through the sequence inserted by the user until you find a 'start'. Iterate through the next part
memorizing the result of the translation in a list called protein. Translation shall stop when the
'stop' sequence is found. Example: starting from the sequence ('start' and 'stop' are
underlined), GUAUGCACGUGACUUUCCUCAUGAGCUGAU, the program shall output:
MetHisValThrPheLeuMetSerstop. If no codon of 'start' and 'stop' is found, then output an
error.
11.2.3 Labyrinth. Write a program reading a text file (maze.txt) containing an image of a labyrinth,
where asterisks ('*') are walls and spaces (' ') are paths.
* *******
* * * *
* ***** *
* * * *
* * *** *
* * *
***** * *
* * *
******* *
Create a dictionary corridor which uses tuples (row, column) as
keys, meaning corresponding positions to the corridors and which values
are sets of positions corresponding to the corridor and near the
positions specified by the key. Example: start key is (1, 1), highlighted
in blue, and its adjacent positions are {(1, 2), (0, 1), (2, 1)}.
In the end, output the dictionary. [P8.20]
11.2.4 Thread of Ariadne. The thread of Ariadne helped Theseus finding the exit from Minosses’
labyrinth, tracking the direction towards the exit. Extend exercise 11.2.3 so that, starting from any
point, you can find the labyrinth exit, using the following algorithm:
Starting from corridors, build a new dictionary paths whose keys are the tuples (row,
column) of positions initially equal to '?'. Then loop through the keys of paths and, for 
14BHD Informatica, A.A. 2022/23 Lab11
4
each key representing the edges of the labyrinth (exit), substitute '?' with a path leading
to the exit: 'N' (as 'North'), 'E' (as 'East'), 'S' (as 'South') o 'W' (as 'West').
After the substitution, use the dictionary corridors to find the adjacent paths, loop
through the keys of paths with value '?'. and, for each of those, verify if they have at
least one adjacent position whose value is in paths different from '?'. If so, replace '?'
with a string leading to the position of the adjacent cell.
Example: Key (1, 1) has, as adjacent cells, {(1, 2), (0, 1), (2, 1)}. If key (0,
1) contains 'N', in paths, if in the current iteration key (1, 1) is still '?', since there is a
value other from '?', will get the value 'N', as the adjacent cell is in the 'North' direction.
If you can’t substitute any keys in the current iteration, terminate the program.
In the end, show the obtained labyrinth, where each position of the corridor contains the fastest
way to the exit. Example:
*N*******
*NWW*?*S*
*N*****S*
*N*S*EES*
*N*S***S*
*NWW*EES*
*****N*S*
*EEEEN*S*
*******S*
[P8.21]
Magic boxes
Alice has 42 magic boxes.
Each box has infinite capacity, but can only store one type of objects. The type
itself is not relevant, but once an object has been inserted in a box, then only
objects of that type can be added. For instance, after inserting an apple, any
number of apples can be added, even tons, but not a single banana.
If a magic box is emptied, it can be refilled with a new type of objects. For
instance, after removing all the apples from the box, a banana can be stored;
and after that, any number of bananas, but not apples anymore.
Bob is handling Alice a sequence of objects; Alice should store them in the magic
boxes according to previous notes. At the same time, Carl is asking Alice for
objects; Alice should take the object Carl is asking for from one box, and handle
it to him.
Write a program to simulate the behavior of Alice, Bob, and Carl. A text file
named ‘actions.txt’ contains the actions performed by Bob and Carl, one per
line, in the form “Bob gives a OBJECT” or “Carl takes a OBJECT”. The
program should check what happen, reporting a message if Alice is not able to
respond correctly because either she can’t store Bob’s object in a box, or she
can’t give Carl the requested object because it’s not available.
The file is correct. Object names are a single word and are written in CAPITAL.
For instance (and assuming that Alice has only 2 boxes):
Bob gives a APPLE
Bob gives a BANANA
Bob gives a APPLE
Bob gives a CHERRY
Generates an error, because Alice cannot store a CHERRY
Bob gives a APPLE
Bob gives a BANANA
Bob gives a APPLE
Carl takes a CHERRY
Bob gives a CHERRY
Generates an error, because Alice cannot give a CHERRY
Bob gives a APPLE
Bob gives a BANANA
Bob gives a APPLE
Carl takes a BANANA
Bob gives a CHERRY
Generates no errors, as the box with the first BANANA is emptied and can later
store a CHERRY.
1
