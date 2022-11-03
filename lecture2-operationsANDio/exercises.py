#!/usr/bin/env python3

a = 10
b = 15
a += b
print(a)

a = 10
b = 15
a = b
b = 1
print(a)


a = 10
b = 15
a = a*a+b
print(a)


# hum I would have thought a*a+b = 100+15=115
a = 10
b = 15
a *= a+b # becomes a = a * (a+b) = 250 here
print(a)


print("\nint to float with float()")
a = 10
print(a)
b = float(a)
print(b)


print("\nstring to int with int()")
a = "10"
b = int(a)
print(b)


print("\nTwo strings seperated by a comma will print string1 string2, ie a space\n"
      "is inserted between the strings")
a = "Welcome"
b = "Home"
print(a,b)


print("\nString concatination will print string1string2, ie no space\n"
      "is inserted between the strings")
a="Welcome"
b="Home"
print(a+b)


print("\nAdd two strings 10 and 15 and convert string to an integer")
a = "10"
b = "15"
c = a+b
d = int(c)
print(d)
print() # this will print a blank line


# exercises 10-13:
# ---------------
bread = 2.00
print(bread)
print()


bread_price = 1
cheese_price = 2
cost = 2*bread_price + 3*cheese_price
print(cost)


age = input("enter your age:")
print(age)
print()


name = input("enter your name: ")
characteristic = input("enter a personality characteristic: ")
print("Sir",name,"the",characteristic)



