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


#ii)
# iii)
# iv)
# v)
# vi)
# vii)
# viii)
# Xi)
# X)
