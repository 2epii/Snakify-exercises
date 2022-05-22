## 1. Integer arithmetics

#We already know the following operators which may be applied to numbers: +, -, * and **.
#The division operator / for integers gives a floating-point real number (an object of type float).
#The exponentiation ** also returns a float when the power is negative:

print(17 / 3)  # gives 5.66666666667
print(2 ** 4)  # gives 16
print(2 ** -2) # gives 0.25

#There's a special operation for integer division where the remainder is discarded: //.
#The operation that yields a remainder of such a division looks like %.
#Both operation always yield an object of type int.

#2. Floating-point numbers

#When we read an integer value, we read a line with input() and then cast a string to integer using int().
#When we read a floating-point number, we need to cast the string to float using float():
#eg:
x = float(input())
print(x)

#Floats with very big or very small absolute value can be written using a scientific notation.
#Eg., the distance from the Earth to the Sun is 1.496·1011, or 1.496e11 in Python.
#The mass of one molecule of the water is 2.99·10-23, or 2.99e-23 in Python.
#One can cast float objects to int objects by discarding the fraction part using the int() function.
#This function demonstrates so called rounding towards zero behavior:
print(int(1.3))   # gives 1
print(int(1.7))   # gives 1
print(int(-1.3))  # gives -1
print(int(-1.7))  # gives -1

#3. math module

#Python has many auxiliary functions for calculations with floats. They can be found in the math module.

#To use this module, we need to import it first by writing the following instruction at the beginning of the program:

#import math

#For example, if we want to find a ceiling value for x, the smallest integer not less than x,
#we call the appropriate function from the math module: math.ceil(x).
#The syntax for calling functions from modules is always the same: module_name.function_name(argument_1, argument_2, ...)
#eg
import math

x = math.ceil(4.2)
print(x)
print(math.ceil(1 + 3.8))

#Some of the functions dealing with numbers - int(), round() and abs() (absolute value aka modulus) - are built-in and don't require any imports.

# All the functions of any standard Python module are documented on the official Python website. Here's the description for math module. The description of some functions is given:
# Function 	Description
# Rounding
# floor(x) 	Return the floor of x, the largest integer less than or equal to x.
# ceil(x) 	Return the ceiling of x, the smallest integer greater than or equal to x.
# Roots and logarithms
# sqrt(x) 	Return the square root of x
# log(x) 	With one argument, return the natural logarithm of x (to base e). With two arguments, return the logarithm of x to the given base
# e 	The mathematical constant e = 2,71828...
# Trigonometry
# sin(x) 	Return the sine of x radians
# asin(x) 	Return the arcsine of x, in radians
# pi 	The mathematical constant π = 3.1415...

#Now for the actual exercises!
#Q2i) Given an integer number, print its last digit.
a = int(input())
#179%10 is remainder when you write 179/10, i.e. 17.9, so 17 r 9
print(a%10)

# ii) Given an integer. Print its tens digit.
a = int(input())
l = list(str(a))

if len(l)==1:
    print(0)
else:
    print(int(l[-2]))

# alternative solution:
 print(a//10%10) # eg 179//10 = 17, and 17%10 is 17/10 = 1.7, remainder is 7, so answer is 7.
 # e.g. if you have 7 say. 7//10 = 0, and 0%10 = 0

# iii) Given a three-digit number. Find the sum of its digits.
a=int(input())
print(a//100+a//10%10+a%10) # matches model solution

# iv) Given a positive real number, print its fractional part.
a = float(input())
print(a-int(a))
#or
a = float(input())
print(a-a*10//10)

# v)   Given a positive real number, print its first digit to the right of the decimal point.
a = float(input())
print(int(a*10)%10)

# vi) A car can cover distance of N kilometers per day. How many days will it take to cover a route of length M kilometers? The program gets two numbers: N and M.
#    my solution:
N = int(input())
M = int(input())
if M%N==0:
    print(M//N)
else:
    print(M//N +1)

#model solution:
from math import ceil
n = int(input())
m = int(input())
print(ceil(m / n)) # ceiling function rounds up to nearest number, so if division is decimal days as in some instances here, it'd round it up to the next whole day!

# vii)   Given the integer N - the number of minutes that is passed since midnight - how many hours and minutes are displayed on the 24h digital clock?
#        The program should print two numbers: the number of hours (between 0 and 23) and the number of minutes (between 0 and 59).
#        For example, if N = 150, then 150 minutes have passed since midnight - i.e. now is 2:30 am. So the program should print 2 30.
N= int(input())
print(N//60,N%60)

# viii) A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
#       A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.
A = int(input()) # dollars
B = int(input()) # cents
N = int(input()) # N numbers of cupcakes
Cent_to_dollars = B*N
print(A*N+(B*N//100),(B*N%100))

# Xi) H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
#     Determine the angle (in degrees) of the hour hand on the clock face right now.
H = int(input()) # Hours
M = int(input()) # Minutes
S = int(input()) # Seconds
# each hour the hour hand moves (1/12)*360 degrees.
# So each minute the hour hand moves: (1/12) *360/60 = 0.5 degrees
# So each second the hour hand moves (1/2)/60=1/120 degrees
print(H*30+M*0.5+S/120)

# X)Hour hand turned by α degrees since the midnight.
#Determine the angle by which minute hand turned since the start of the current hour.
#Input and output in this problems are floating-point numbers.

#for every 360 degrees the min hand turns, the hour hand turns 1/12*360 = 30 degrees
hours_degrees_moved = float(input())
mins_moved = ((hours_degrees_moved/30)*360)%360
print(mins_moved )
