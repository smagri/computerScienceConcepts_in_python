#!/usr/bin/env python3

# As you write the details of  your code, you’ll find yourself writing
# functions.   You’ll also  find that  within those  functions, you’ll
# make use  of more function calls,  which are when you  initiate some
# action that has been defined  with a function. Calling “print” means
# that we’re using the print  function, and calling “input” means that
# we’re using  the input function.  And  you can treat these  calls as
# black boxes of their own.


# We define a function by starting  with the key term “def,” short for
# “define.”  Next,  we have  the name of  our function—the  command we
# want to use to call the function. Following that are parentheses. If
# our  function  is  going  to  take  in  some  form  of  input,  that
# information is going  to be specified inside  the parentheses. Then,
# we  have  a  colon,  just   like  we’ve  seen  in  conditionals  and
# loops.  Finally,  we have  the  commands  that the  function  should
# do. These are indented, again just like we saw with conditionals and
# loops.


# The term we  use for the first line defining  the function is called
# its  header.   The actual  commands  it  should do—the  part  that’s
# indented—is called the body.

# define fn with no input parameters and fn name warn, parentheses
# must always exist even if no parameters are passed. Then add the
# colon at the end.
def warn():
    print("Warning! Use program at your own risk.")

a = 3
print (a)
warn() # call fn
print("Welcome!")


# Remember that functions are able to return values.
def getName():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    full_name = first + ' ' + last
    return full_name
name = getName()
print(name)

# Sometimes we might want to return more than one variable.

def getNameR2():
    first = input("Enter your first name:")
    last = input("Enter your last name:")
    return first, last
userfirst, userlast = getNameR2()
print("print lastname, firstname: ", userlast +" "+ userfirst)





###############################################################################
#                                  DOCSTRINGS                                 #
###############################################################################

# special syntax  used to provide  these comments for a  function, and
# it’s  called  a  docstring,  that  ends and  begins  with  a  triple
# quotation mark, it should come right after the function header.

# If  you use  the command  “help” for  any function,  passing in  the
# function name  as a  parameter, you will  get information  about the
# function, including its docstring.


def greet(name):
    """Print a greeting: Hello, name. Maybe put in help on howto used the fn
    here. This is the docstring for a function.  Place it in triple quotes."""
    print("Hello, "+name)

help(greet)

