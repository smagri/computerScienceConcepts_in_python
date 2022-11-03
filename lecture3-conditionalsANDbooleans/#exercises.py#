#!/usr/bin/env python3

#from unicodedata import *


 # comparison conditionals are as per c/c++: ie =assignment >, >=,
 # ==equality, !=inequality...etc. note < always comes first 11:50m
 
print("NOTE SYNTAX: in <= or >= conditionals remember the < always comes first\n"
      "before the equals sign, useful to known, c is like this too I think ")


a = 1
b = 2
c = 2
print("a=",a, "b=",b, "c=",c)
if (a != b):
    print("video got this wrong, a is !=b, video says this is false")

# The  RELATIONAL   OPERATORS  COMPARE  THE  UNICODE   VALUES  OF  THE
# CHARACTERS OF THE STRINGS FROM THE  ZEROTH INDEX TILL THE END OF THE
# STRING. It  then RETURNS A  BOOLEAN VALUE ACCORDING TO  THE OPERATOR
# USED. sse docs.python.org/3/howto/unicode.html
#
# Python defaults to using UTF-8, 8bit values for encodings called
# code points.

# Unicode string is a sequence of code points, which are numbers from
# 0 through 0x10FFFF (1,114,111 decimal). This sequence of code points
# needs to be represented in memory as a set of code units, and code
# units are then mapped to 8-bit bytes. UTF-8 is a byte oriented
# encoding. The encoding specifies that each character is represented
# by a specific sequence of one or more bytes.

#Ans: 5=True,6=False,7=True,8=False.
d = "One"
e = "Two"
f = "Three"
g = "one"
print("The ord() fn converts a single unicode character to its inter code\n"
      "point, compare each code point to see which string is bigger,\n"
      "evaluate by using the and operator between each char in each string")
print("print unicode value of d is = ", [ord(each_char) for each_char in d])
print("print unicode value of e is = ", [ord(each_char) for each_char in e])
print("print unicode value of f is = ", [ord(each_char) for each_char in f])
print("print unicode value of g is = ", [ord(each_char) for each_char in g])
print("unicode of d string just using a for loop, not each_char value in list:")
for each_char in d:
    print(ord(each_char))

print("d=",d, "e=",e, "f=",f, "g=",g)
print()
print("d=", d)
print("e=", e)
print("f=", f)
print("g=", g)



print("String size is compared char by char: EVERY UNICODE VALUE FORECH CHAR IN\n"
      "LHS string needs to be < FOREACH CHAR IN RHS string,\n"
      "ie use the and operator foreach character, ignore any excess chars:???")
print("is d<e:")
if d<e:
    print("True")
else:
    print("False")

print("is e<f")
if e<f:
    print("True")
else:
    print("False")

print("is d<g")
if d<g:
    print("True")
else:
    print("False")

print("is g<e")
if g<e:
    print("True")
else:
    print("False")


    
# this means age<=12 makes x==True, note video uses x=(age<12):, colen
# seem not needed in python3 anyhow,it gives a syntax error.  If you
# use age<12 you need the colen though, that is what is normally used
# to get the required output from the code.

age = 10
x = (age<12)
print("using x assignment variable in condition")
if x:
    print("you are > 12 years of age, your meal is free")
else:
    print("you are < 12 years of age, you have to pay for your meal")

print("using a<12 om condition")      
if age<12:
    print("you are > 12 years of age, your meal is free")
else:
    print("you are < 12 years of age, you have to pay for your meal")


print("using (a<12) in condition")
if (age<12):
      print("you are > 12 years of age, your meal is free")
else:
      print("you are < 12 years of age, you have to pay for your meal")

    
# VIDEO 19min: use and: or: not:(just changes True to False) operators
# with boolians to test conditions.

print("exersies: 9, 10, 11, 12")
print(not (a == b)) #True
print(b < c or b > c) #False
print((a+1) == b and not b < c) #2==2 and not(False) => True
print((a <= b) and (b <= c)) or ((a >= b) and (b >= c)) # true and true => True

print("exercise:13") # answer: Reasonable cost
total_cost = 100.00
days = 3
cost_per_day = total_cost / days #33.333
if cost_per_day > 40:
    print("Too expensive")
elif cost_per_day > 30:
    print("Reasonable cost")
elif cost_per_day > 20:
    print("Excellent cost")
else:
    print("Incredible bargain")



print("exercise:15, method1") # answer: eligible for reduced benefits  
age = 67
income = 10000
if (age > 70):
    if (income < 15000):
        print("Eligible for benefits")
    else:
        if (income < 20000):
            print("Eligible for reduced benefits")
        else:
            print("Not eligible for benefits")
else:
    if (income < 20000):
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")


print("exercise:15, method2")        
if (age > 70):
    if (income < 15000):
        print("Eligible for benefits")
    elif (income < 20000):
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")
else:
    if (income < 20000):
        print("Eligible for reduced benefits")
    else:
        print("Not eligible for benefits")


print("exercise:15, method3")
if (income < 20000):
    print("Eligible for reduced benefits")
elif (age>70) and (income<15000):
    print("Eligible for benefits")
else:
    print("Not eligible for benefits")
    
