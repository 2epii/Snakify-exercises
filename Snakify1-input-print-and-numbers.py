# Lesson 1 on snakify

# Examples of Print statement in python:
print(5 + 10)
print(3 * 7, (17 - 2) * 8)
print(2 ** 16)  # two stars are used for exponentiation (2 to the power of 16)
print(37 / 3)  # single forward slash is a division
print(37 // 3)  # double forward slash is an integer division
        # it returns only the quotient of the division (i.e. no remainder)
print(37 % 3)  # percent sign is a modulus operator
        # it gives the remainder of the left value divided by the right value

#using input() to get user input
#eg:
print('What is your name?')
name = input()  # read a single line and store it in the variable "name"
print('Hi ' + name + '!')


# Q1
#i) Write a program that takes three numbers and prints their sum. Every number is given on a separate line.

# This program reads three numbers and prints their sum:
a = int(input())
b = int(input())
v = int(input())
print(a + b + v)

# ii) Write a program that greets the person by printing the word "Hi" and the name of the person. See the examples below.
a = input()
print("Hi "+a)

# iii) Write a program that takes a number and print its square.
def square(x):
    return x**2

#print to test
print(square(int(input())))

# iv) Write a program that reads the length of the base and the height of a right-angled triangle and prints the area. Every number is given on a separate line.
# Read the numbers b and h like this:
b = int(input())
h = int(input())

print(0.5*b*h)

# Write a program that greets the user by printing the word "Hello", a comma, the name of the user and an exclamation mark after it. See the examples below.
# Warning. Your program's output should strictly match the desired one, character by character. There shouldn't be any space between the name and the exclamation mark.
# You can use + operator to concatenate two strings. See the lesson for details.
# Read the name:
name = input()
print("Hello, "+ str(name)+"!")

# v) N students take K apples and distribute them among each other evenly.
#    The remaining (the undivisible) part remains in the basket. How many apples will each single student get? How many apples will remain in the basket?
#    The program reads the numbers N and K. It should print the two answers for the questions above.
# Read the numbers like this:
n = int(input())
k = int(input())
print(k//n) # floor division eg if k = 50, n = 6, 50//6 = 8

print(k%n) # modulus eg if k = 50, n = 6, 50%6 = 2 as when you do 50 into 6 you have 6*8 =48, remainder 2. Modulus gives you remainder.

# vi) Write a program that reads an integer number and prints its previous and next numbers.
#     See the examples below for the exact format your answers should take. There shouldn't be a space before the period.

#Remember that you can convert the numbers to strings using the function str.
a = int(input())

print("The next number for the number "+ str(a) +" is "+ str(a+1) +".")
print("The previous number for the number "+ str(a) +" is "+ str(a-1) +".")

# vii) A timestamp is three numbers: a number of hours, minutes and seconds.
#      Given two timestamps, calculate how many seconds is between them.
#      The moment of the first timestamp occurred before the moment of the second timestamp.
hr1 = int(input())
min1 = int(input())
sec1 = int(input())
hr2 = int(input())
min2 = int(input())
sec2 = int(input())

time1_in_seconds = hr1*3600+min1*60+sec1
time2_in_seconds = hr2*3600+min2*60+sec2
diff = time2_in_seconds - time1_in_seconds
print(diff)

# viii) A school decided to replace the desks in three classrooms. Each desk sits two students.
#       Given the number of students in each class, print the smallest possible number of desks that can be purchased.
#       The program should read three integers: the number of students in each of the three classes, a, b and c respectively.
#       In the first test there are three groups. The first group has 20 students and thus needs 10 desks.
#       The second group has 21 students, so they can get by with no fewer than 11 desks.
#       11 desks is also enough for the third group of 22 students. So we need 32 desks in total.

import math
a = int(input())
b = int(input())
c = int(input())

min_desks = math.ceil(a/2)+math.ceil(b/2)+math.ceil(c/2)
print(min_desks)
