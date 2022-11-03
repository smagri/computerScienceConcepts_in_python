#!/usr/bin/env python

# Classes and objects  are great at tying together  different types of
# data, Data structures  are focused on how to  organize large amounts
# of the same type of data.

# By adding structure to data with data structures we can speedup some
# of the operations on that data.

# STACKS: ---------- The stack data  structure is basically just this,
# only with data  instead of books.  If we add  something new onto the
# stack, we  will call the operation  a push().  if we  remove the top
# item from the stack,  we will call it a pop().   Stacks give us what
# is referred to as last in, first out, that is, the last thing pushed
# is the first thing popped.

# Queue: ---------- gives you a first  in, first out process?  This is
# what you encounter when people queue  up to stand in line, the first
# one in line is  the first one handled. For the  first element in the
# list, we just pass in a .pop(0), and the first element is removed.


# Fn  Call stack:  ----------  Inside computers,  stacks  have a  very
# fundamental use.  As we make  function calls, the computer memory is
# storing data in what is referred to as the call stack, also known as
# a  _control  stack_  or  _runtime stack_  or  _frame  stack_,  which
# consists of function activation records, which keep track of all the
# variables and data defined in that part of the program.


# HASH fn: ---------- A function to convert some particular key phrase
# into a number  that can be used  to index into an array  is called a
# hash  function.  Use  'chaining' or  lists  of lists  when the  hash
# function comes up with the same  index into the array storage.  Hash
# tables can  get much  more complicated  than this,  but fortunately,
# there is a tool in Python  that basically implements hash tables for
# us,  and  we  do  not  even  have to  come  up  with  our  own  hash
# function. In Python, this tool  is called dictionary, and the Python
# command to create a new dictionary is called dict.

# Compared to the  alphabetical list of a traditional  dictionary in a
# book, a hash  table is designed to be more  efficient. And there are
# other  names  for  hash  tables,  including  map,symbol  table,  and
# associative array.


# SETS: ---------- are another hash table data structure in python.  A
# set is  just a collection  of items, but it  will be stored  using a
# hash  table instead  of  a list  so that  it  does mathematical  set
# operations  and  checks  set  membership  very  quickly.   Use  _in_
# statement to check whether  or not a particular item is  in a set or
# not.

# Note  that we  could get  the  exact same  effect by  using the  set
# command, as  follows, instead of  the curly braces. The  set command
# takes in a list as a parameter, and all the elements of the list get
# put into the  set.  One big advantage of the  set command over curly
# braces is that  the set command lets  us create an empty  set. If we
# just have  curly braces,  with nothing inside,  that will  create an
# empty dictionary, not an empty set. So,  if we want to start with an
# empty set  and gradually add  things to it, we  have to use  the set
# command.   use  .add(value) and  .remove(value)  to  add and  remove
# elements from a set.

################################################################################
# a stack is last in, first out, LIFO

# happens when we call functions in  a program with each function data
# pused onto  the stack  successively and  then popped  off in  a LIFO
# fashion when each function returns.

class Stack:
    _stack = []
    def push(self, item):
        self._stack.append(item)

    def pop(self):
        return self._stack.pop()

namestack = Stack()

print("answer should be, using the Stack class defined"
      ".push(), .pop() methods:"
      "\nJoseph\nJames\nJohn\n")
namestack.push("John")
namestack.push("James")
namestack.push("Joseph")
person = namestack.pop()
print(person)
person = namestack.pop()
print(person)
person = namestack.pop()
print(person)
    

print("\n\nanswer should be just using a normal stack nomenclature,\n"
      " .append() and .pop() methods:\n"
      "Joseph\nJames\nJohn\n")
my_name_stack = []
my_name_stack.append("John")
my_name_stack.append("James")
my_name_stack.append("Joseph")
person = my_name_stack.pop()
print(person)
person = my_name_stack.pop()
print(person)
person = my_name_stack.pop()
print(person)



################################################################################
# a queue is first in, first out, FIFO
#

# It's like a  buffer, allowing you to handle your  data later without
# loosing it as it is coming  in real fast(did this in programming for
# megatronic systems)

print("answer should be, using the Queue class defined"
      " .enqueue(), .deque() methods:")
class Queue:
    _queue = []
    def enqueue(self, item):
        self._queue.append(item)

    def dequeue(self):
        return self._queue.pop(0)

    def isEmpty(self):
        retrun (len(self._queue) == 0)



print("\n\nanswer should be just using a defined Queue class,\n"
      " .enqueue() and .dequeue(0) methods:\n"
      "John\nJames\nJoseph")
namequeue = Queue()
namequeue.enqueue("John")
namequeue.enqueue("James")
namequeue.enqueue("Joseph")
person = namequeue.dequeue()
print(person)
person = namequeue.dequeue()
print(person)
person = namequeue.dequeue()
print(person)


print("\n\nanswer should be just using a normal Queue nomenclature,\n"
      " .append() and .pop() methods:\n"
      "John\nJames\nJoseph")
my_name_que = []
my_name_que.append("John")
my_name_que.append("James")
my_name_que.append("Joseph")
person = my_name_que.pop(0)
print(person)
person = my_name_que.pop(0)
print(person)
person = my_name_que.pop(0)
print(person)



################################################################################

# hash table  = used to  represent a large  series of data  as indexes
# into  an array,  index is  a hash  number, to  make access  to large
# datasets managable.   You can use  some associative value or  a hash
# function to get your index.

# When you get the same index for your data item you can use chaining,
# a list of lists into that slot.  Still your data is more managable.

# in python  a dictionary, dict() is  used to implement a  hash table,
# with a built in internal hash function.

# They can also  be called map, symbol table and  associative array, I
# guess we use  a map/dict...etc to access key,value  pairs type data.
# Keys need to  be immutable(ie not changable) however,  values can be
# immutable or mutable(changable).

# use del fn  and key to remove  elements from the hash  table and add
# elements as below  with key value pair assignments in  a list or key
# value lists. use fn in to check if key is in the dictionary, returns
# true or false. use for statement to itterate over a dictionary.

cast = {"Cardinal Ximenez" : "Michael Palin", "Cardinal Biggles" : "Terry Jones"
        , "Cardinal Fang" : "Terry Gilliam"}
print("cast dictionary is:", cast)

print("make some additions to dictionary, now making it: ")
cast["customer"] = "John Cleese"
cast["shopkeeper"] = "Michael Palin"
print(cast)

print("output should be: \nMicheal Palin\nMicheal Palin\nTerry Gilliam")
print(cast["shopkeeper"])
print(cast["Cardinal Ximenez"])
print(cast["Cardinal Fang"])



################################################################################

# sets is a  collection of related data values associated  with a key,
# that uses a  hash function also to access the  data. This allows you
# to  check  for set  membership  really  quickly, using  mathematical
# fns(eg |-or &-intersection -,in one but not the other, ^ - in either
# set but not in both ) Use in statement to check if item is in set or
# not.  Set takes a list of items as it's paramter.  Note curly braces
# define dictionaryies,  sets have normal  braces () enclosing  a list
# [].  Use .add() and .remove() method  from to add or remove elements
# from a set.

# mathamatical fn's on sets:
# - substract common elements from set one that are in set 2, ie set1-set2
# | in one OR the other, logical/mathematical set.
# & in one AND the other, logical/mathamatical intersection.
# ^ XOR, one or the other but not both



################################################################################

# note  this is  a set  not a  dictionary as  we don't  have key,value
# pairs, even though we have curly braces
primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37}

# this format of set definition allows us to create empty sets
teens = set([13, 14, 15, 16, 17, 18, 19]) 
print("primes are:")
print(primes)
print("teens are:")
print(teens)

print("output primes-teens should be: 2 3 5 7 11 23 29 31 37, "
      "is stored in one and not the other, ie subtraction")
print(primes - teens)

print("output primes&teens should be: 13 17 19, "
      "and is stored in both, intersection")
print(primes & teens)


print("output primes|teens, OR, should be: all unique elements pertaining to both"
      "sets, and stored in one or the other")
print("ie ", 2,3,5,7,11,13,14,15,16,17,18,19,23,29,31,37)
print(primes | teens)

print("output primes^teens, XOR, should be: "
      "2 3, 5, 7, 11, 23, 29, 31, 37, 14, 15, 16")
print(primes ^ teens)
