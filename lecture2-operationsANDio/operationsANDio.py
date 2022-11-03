#!/usr/bin/env python3

# Note: if we use python(so python2 on ubuntu18.04) we need the line:
# -*- coding: utf-8 -*- as exactly our second line of code.  Remember
# this course is using python3.

# Computer memory is  composed of several layers  that are categorized
# by how close they  are to the processor. The closer  to the CPU, the
# easier and faster it’ll be for the CPU to access that memory. As you
# get farther away from the CPU, it takes longer to access the memory,
# but  you   get  more  of   it,  and  it  generally   becomes  longer
# lasting. Critical data  might be moved from one layer  to another as
# needed.

# Some memory, called the registers, is  built right into the CPU, and
# some other memory,  the cache, is in the same  integrated circuit as
# the CPU.  This is all really short-term memory, and most programmers
# don’t need to worry about it.

# The next  level of memory  is the  main one programmers  care about—
# called main memory, or sometimes  primary memory.  This is the main,
# short-term memory of the computer.  It’s the working memory where we
# keep all the things that are running, from the operating system that
# we’re  working  inside  of  to the  programs  that  we’re  currently
# executing. This memory is still close to the CPU.

# The random access memory (RAM) is  also referred to as “volatile” or
# temporary  memory. The  way existing  technology works,  if we  lose
# power to the computer, the data in this memory is lost. When we talk
# about variables  in memory,  we’re talking  about variables  held in
# temporary memory.  When we  run a program,  part of  this temporary,
# working memory is set aside for use by variables in the program.

# Farther away from the CPU, memory is in so-called permanent storage—
# what’s also called secondary memory, or just storage. Whether it’s a
# hard-disk drive or  a solid-state drive using flash  memory, this is
# where we  store longer-term information, such  as files. Programmers
# deal with  storage by deciding  what data we  want to “read  in” for
# attention in  temporary, working memory  or “write out” to  files in
# storage.

# Beyond secondary memory that is  on board the computer, there’s also
# what’s  called tertiary  memory,  or remote  storage.  This is  data
# that’s   stored  more   remotely,   possibly  offline   or  over   a
# network. Remote storage

# You can use single, '',  or double, "", quotes to indicate strings.
x = 'pizza'
print(x)
x = "pepperoni pizza"
print(x)

# In Python,  you can name variables  anything you want, subject  to a
# few rules: use only letters,  numbers, and underscore; and don’t use
# a number at  the beginning. In addition, a few  of Python’s built-in
# commands, such as  “print,” are known as keywords and  are not to be
# used as the name of a variable.

# Variables  have types  and  python will  determine it  automatically
# depending on what you assign to it, unlike other languages.

# You join two  strings in python with the plus,  +, or addition sign,
# this  is called  concatination.   You can't  do string  subtraction,
# multiplication  and  division  though.   However, it  does  let  you
# multipy  a string  by an  integer to  represent the  string repeated
# several times.


print("this is string " + "concatination")

# We can  print multiple  items by  seperating them  by commas  in the
# print() command.  By default print() prints one space for each comma.
print("What type of pizza have we defined, answer:", x)

# this just waits for you to enter an input on the commandline
#b = input()
#print("you entered:", b)

# note again  that COMMAND  LINE INPUT, ie  using input()  FUNCTION IS
# TREATED AS A STRING.

a = input("Enter value one:")
b = input ("Enter value two:")
print("The sum is", a+b) # so this is a string concatination

# to  treat  input()  input  or strings  like  numbers,use  eg  int(),
# float()...etc

a = "1"
b = "3.14159"
print(a)
print(b)
c = int(a)
d = float(b)
print(c)
print(d)
