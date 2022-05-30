#Theory:
#1. Strings
#A string can be read from the standard input using the function input() or defined
#in single or double quotes. Two strings can be concatenated, and we can also repeat
#a string n times multiplying it by integer:
print('>_< ' * 5)  # >_< >_< >_< >_< >_<

#A string in Python is a sequence of characters. The function len(some_string)
#returns how many characters there are in a string:
print(len('abcdefghijklmnopqrstuvwxyz'))  # 26

#Every object in Python can be converted to string using the function str(some_object).
#So we can convert numbers to strings:
s = str(2 ** 100)
print(s)  # 1267650600228229401496703205376
print(len(s))  # 31

# 2. Slices: single character
# A slice gives from the given string one character or some fragment: substring or subsequence.
# There are three forms of slices. The simplest form of the slice: a single character
#slice S[i] gives ith character of the string. We count characters starting from 0.
#That is, if S = 'Hello', S[0] == 'H', S[1] == 'e', S[2] == 'l', S[3] == 'l', S[4] == 'o'.
#Note that in Python there is no separate type for characters of the string.
#S[i] also has the type str, just as the source string.
# Number i in S[i] is called an index.
# If you specify a negative index, then it is counted from the end, starting with
#the number -1. That is, S[-1] == 'o', S[-2] == 'l', S[-3] == 'l', S[-4] == 'e', S[-5] == 'H'.
# Let's summarize it in the table:
(String S): 	H 	  e 	 l 	     l 	     o
Index: 	      S[0] 	 S[1]   S[2] 	S[3] 	S[4]
Index: 	     S[-5] 	 S[-4] 	S[-3] 	S[-2] 	S[-1]

# 3. Slices: substring
# Slice with two parameters S[a:b] returns the substring of length b - a, starting
# with the character at index a and lasting until the character at index b, not including
# the last one. For example, S[1:4] == 'ell', and you can get the same substring using S[-4:-1].
# You can mix positive and negative indexes in the same slice, for example, S[1:-1] is a
# substring without the first and the last character of the string (the slice begins with the
# character with index 1 and ends with an index of -1, not including it).
#
# Slices with two parameters never cause IndexError. For example, for S == 'Hello' the
# slice S[1:5] returns the string 'ello', and the result is the same even if the second index
# is very large, like S[1:100].
#
# If you omit the second parameter (but preserve the colon), then the slice goes to the end
# of string. For example, to remove the first character from the string (its index is 0) take
# the slice S[1:]. Similarly if you omit the first parameter, then Python takes the slice from
# the beginning of the string. That is, to remove the last character from the string, you can
# use slice S[:-1]. The slice S[:] matches the string S itself. 
