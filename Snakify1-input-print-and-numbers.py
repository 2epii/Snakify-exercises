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

# Write a program that takes a number and print its square.
def square(x):
    return x**2

#print to test
print(square(int(input())))
