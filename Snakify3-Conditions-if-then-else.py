"""
Theory below, questions to follow:
1. Syntax
Conditions: if, then, else:

Let's consider the following problem: for the given integer X determine its absolute value.
If X>0 then the program should print the value X, otherwise it should print -X.
This behavior can't be reached using the sequential program.
The program should conditionally select the next step. That's where the conditions help:

x = int(input())
if x > 0:
    print(x)
else:
    print(-x)

This program uses a conditional statement if. After the if we put a condition (x > 0) following by a colon.
After that we put a block of instructions which will be executed only if the condition is true (i.e. evaluates to True).
This block may be followed by the word else, colon and another block of instructions which will be executed only if the
condition is false (i.e. evaluates to False). Is the case above, the condition is false, so the 'else' block is executed.
Each block should be indented using spaces.

if condition:
    true-block
    several instructions that are executed
    if the condition evaluates to True
else:
    false-block
    several instructions that are executed
    if the condition evaluates to False

The else keyword with the 'false' block may be omitted in case nothing should be done if the condition is false.
For example, we can replace the variable x with its absolute value like this:

2. Nested conditions

Any Python instruction may be put into 'true' blocks and 'false' block, including another conditional statement.
This way we get nested conditions. The blocks of inner conditions are indented using twice more spaces (eg. 8 spaces).
Let's see an example. Given the coordinates of the point on the plane, print its quadrant.

x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        # x is greater than 0, y is greater than 0
        print("Quadrant I")
    else:
        # x is greater than 0, y is less or equal than 0
        print("Quadrant IV")
else:
    if y > 0:
        # x is less or equal than 0, y is greater than 0
        print("Quadrant II")
    else:
        # x is less or equal than 0, y is less or equal than 0
        print("Quadrant III")

4. Bool objects and logical operators
The True and False objects have a special type called bool. As every type name can
be used to cast objects into that type, let's see what this cast gives for numbers:
print(bool(-10))    # True
print(bool(0))      # False - zero is the only false number
print(bool(10))     # True
print(bool(''))     # False - empty string is the only false string
print(bool('abc'))  # True

Sometimes you need to check several conditions at once. For example, you can check if a number n is divisible by 2 using the
condition n % 2 == 0 (n gives a remainder 0 when dividing by 2). If you need to check that two numbers n and m are both divisble
by 2, you should check both n % 2 == 0 and m % 2 == 0. To do that, you join them using an operator and (logical AND): n % 2 == 0 and m % 2 == 0.
Python has logical AND, logical OR and negation.
Operator and is a binary operator which evaluates to True if and only if both its left-hand side and right-hand side are True.
Operator or is a binary operator which evaluates to True if at least one of its sides is True.
Operator not is a unary negation, it's followed by some value. It's evaluated to True if that value is False and vice versa.
Let's check that at least one of the two numbers ends with 0:

5. 'elif' word

If you have more than two options to tell apart using the conditional operator, you can use if... elif... else statement.
Let's show how it works by rewriting the example with point (x,y) on the plane and quadrants from above:

x = int(input())
y = int(input())
if x > 0 and y > 0:
    print("Quadrant I")
elif x > 0 and y < 0:
    print("Quadrant IV")
elif y > 0:
    print("Quadrant II")
else:
    print("Quadrant III")

"""
#Solutions to questions
# 1) Given two integers, print the smaller value.
a=int(input())
b=int(input())

if a>b:
    print(b)
else:
    print(a)

# 2) For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero.
#    Try to use the cascade if-elif-else for it.
a = int(input())
if a<0:
    print(-1)
elif a>0:
    print(1)
else:
    print(0)

# 3) Given three integers, print the smallest value.
a = int(input())
b = int(input())
c = int(input())

if a<b and a<c:
    print(a)
elif b<c and b<a:
    print(b)
else:
    print(c)

#4) Given three integers, determine how many of them are equal to each other.
#The program must print one of these numbers: 3 (if all are the same),
#2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different).
a = int(input())
b = int(input())
c = int(input())

if a==b==c:
    print(3)
elif a==c and a !=b:
    print(2)
elif b==c and a!=b:
    print(2)
elif a==b and b!=c:
    print(2)
elif a!=b!=c:
    print(0)

#5) Chess rook moves horizontally or vertically. Given two different cells of the chessboard,
#determine whether a rook can go from the first cell to the second in one move.
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
#first two - for the first cell, and then the last two - for the second cell. The program should output YES
#if a rook can go from the first cell to the second in one move, or NO otherwise.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a ==c or b == d:
    print('YES')
else:
    print('NO')

#6 Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number,
#first two - for the first cell, and then the last two - for the second cell.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (a in(1,3,5,7) and b in(1,3,5,7)) and ((c in(1,3,5,7) and d in(1,3,5,7)) or (c in(2,4,6,8)and d in(2,4,6,8))):
    print('YES')
elif (a in(2,4,6,8)and b in(2,4,6,8)) and ((c in(1,3,5,7) and d in(1,3,5,7)) or (c in(2,4,6,8)and d in(2,4,6,8))):
    print('YES')
elif a in (2,4,6,8) and b in (1,3,5,7)and ((c in (2,4,6,8) and d in (1,3,5,7)) or (c in(1,3,5,7) and d in (2,4,6,8))):
    print('YES')
elif a in(1,3,5,7) and b in (2,4,6,8) and ((c in (2,4,6,8) and d in (1,3,5,7)) or (c in(1,3,5,7) and d in (2,4,6,8))):
    print('YES')
else:
    print('NO')

#model solution:
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')
#7) Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard,
#determine whether a king can go from the first cell to the second in one move.
#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two -
#for the first cell, and then the last two - for the second cell. The program should output YES if a king can
#go from the first cell to the second in one move, or NO otherwise.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a-c)==1 and abs(b-d)==1:
    print('YES')
elif (abs(a-c)==1 and abs(b-d)==0) or (abs(b-d)==1 and abs(a-c)==0):
    print('YES')
else:
    print('NO')
#ideal solution combines the if and first elif using <=1 (this includes 0 and 1 distances. )

#8) Bishop moves:
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a-c)==abs(b-d):
    print('YES')
else:
    print('NO')

#9)Queen move - combination of rook and bishop move it seems.
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if abs(a-c)==abs(b-d) or (a ==c or b == d):
    print('YES')
else:
    print('NO')

#10 Knight move
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if (abs(c-a)==1) and (abs(d-b)==2):
    print('YES')
elif (abs(c-a)==2) and (abs(d-b)==1):
    print('YES')
else:
    print('NO')
