#!/usr/bin/env python3

#excersice 1, added vartiation myself for revision of operators
print("ex1: while loop division iterator")
i = 10
while i > 1:
    print (i)
    i /= 2 # i = i/2, returns i divided by 2


# remember,  fraction  is  'quotient/remainder": //  operator  returns
# quotient and % operator(also  called modulus) returns the remainder.
# note: a single / is just normal division.

print("practicing operators, quotient and remander/modulus, just for fun:")
print("while loop quotent iterator")
i = 10
while i > 1:
    print (i)
    i //= 2 # i = i/2, returns quotent. 5, 2


print("while loop remainder iterator")
i = 10
while i > 1:
    print (i)
    i %= 2 # i = i%2, i/2 modulus or remainder. 0 


print("ex3: range one value in parenthesis")
# 0, 1, 2, 3
for i in range(4):
    print (i)


print("ex4: range two values in parenthesis")
# 3, 4
for i in range(3,5):
    print (i)

print("ex5: range 3 values in parenthesis")    
# 1, 4, 7
for i in range (1,10,3):
    print (i)

    
print("countdown, 3 values in parenthesis: \n"
      "note: range(1,10,-3) doesn't execute a loop at all???, so loop conditiona"
      "is always evaluated once to start off with as normal for loops")
# 1
for i in range (1, 10, -3):
    print (i)

print("countdown, 3 values in parenthesis:")
for i in range (10, 1, -3):
    print (i)



print("ex:8")
print("note: the input(), user input statement is always interpreted as a string,\n"
      "so use, int() to convert it to an integer so it can be used in a\n"
      "for range() loop")

count = int(input("enter a number and count from 1 to that number, with for loop: "))
for i in range(1, count+1):
    print(i)

print("again but using a while loop instead of a for/range() loop:")
i=1
count = int(input("enter a number: "))
while (i<=count):
    print(i)
    i += 1 # remember, the +/- is always on the LHS, c is like this too.


print("ex:9")
print("for loop output:")
for i in range(2, 7, 3):
    print(i)

print("while loop output:")
i = 2
while(i<7):
    print(i)
    i = i + 3



print("ex: 10")

num_btw_1_and_10_i_define = 5
num_input = 0
while (num_input != num_btw_1_and_10_i_define):
    num_input = int(input("enter a number between 1 and 10,\n"
                          "till you guess a number I have defined:"))
    
print("you have guessed the correct number, ie 5")

    
