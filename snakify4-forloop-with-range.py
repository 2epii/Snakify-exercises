#few examples of loop code:

for i in range(5, 8):
    print(i, i ** 2)
print('end of loop')

for character in 'hello':
    print(character)

for i in range(3):
print(i)

for i in range(10, 0, -2):
    print(i)

print(1, 2, 3, sep='', end=' -- ')
print(4, 5, 6, sep=' * ', end='.')
#this gives output: 123 -- 4 * 5 * 6.
#note how both these are on the same line

# Q1) Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively.
a = int(input())
b = int(input())
for i in range(a,b+1):
    print(i, end =' ')

#2)  Given two integers A and B. Print all numbers from A to B inclusively,
#    in ascending order, if A < B, or in descending order, if A ≥ B.
a = int(input())
b = int(input())

if a<b:
    for i in range(a,b+1):
        print(i,end = ' ')
else:
    for i in range(a,b-1,-1):
        print(i,end = ' ')
#3) 10 numbers are given in the input. Read them and print their sum. Use as few variables as you can.
a=0
for i in range(0,10):
    a = a+int(input())
print(a)
#nb: a=a+int(input()) can be written as: a+=int(input()

#4)N numbers are given in the input. Read them and print their sum.
#The first line of input contains the integer N, which is the number of integers to follow.
#Each of the next N lines contains one integer. Print the sum of these N integers.
p=0
for i in range(int(input())):
    p+=int(input())
print(p)

#5) For the given integer N calculate the following sum:
    #1^3+2^3+…+N^3
p=0
for i in range(int(input())):
    p+=(i+1)**3
print(p)

#6) In mathematics, the factorial of an integer n, denoted by n! is the following product:
#n!=1×2×…×n
#For the given integer n
#calculate the value n!. Don't use math module in this exercise.
n = int(input())
p=1
for i in range(n,0,-1):
    p=p*i
print(p)
#model solution less convoluted!
res = 1
n = int(input())
for i in range(1, n + 1):
    res *= i
print(res)

#7 Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it.
# number of numbers that are equal to zero, not the number of zero digits.
n = int(input())
count = 0
for i in range(n):
    if int(input())==0:
        count+=1
print(count)

#8)Given an integer n, print the sum 1!+2!+3!+...+n!.
#This problem has a solution with only one loop, so try to discover it. And don't use the math library :)

n = int(input())
sum = 0
p=1
for i in range(1,n+1):
    p=p*i
    sum+=p
print(sum)

#9 For given integer n ≤ 9 print a ladder of n steps. The k-th step consists of the integers from 1 to k without spaces between them.
#To do that, you can use the sep and end arguments for the function print().
n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end = '')
    print()

#10) There was a set of cards with numbers from 1 to N. One of the card is now lost.
#Determine the number on that lost card given the numbers for the remaining cards.
# Given a number N, followed by N − 1 integers - representing the numbers on the remaining
# cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

ls1 =[]
ls2=[]
for i in range(a):
    ls1.append(i+1)

for i in range(a-1):
    ls2.append(int(input()))

for i in ls2:
    ls1.remove(i)
print(ls1[0])

#model solution:
n = int(input())
sum_cards = 0
for i in range(1, n + 1):
    sum_cards += i
# One can prove the following:
# sum_cards == n * (n + 1) // 2
# However, we'll calculate that using the loop.
for i in range(n - 1):
    sum_cards -= int(input())
print(sum_cards)
