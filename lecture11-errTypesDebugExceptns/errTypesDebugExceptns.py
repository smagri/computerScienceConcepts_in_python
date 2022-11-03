#!/usr/bin/env python3

###############################################################################
#                             EXCEPTIONS, basically runtime error checking
#
###############################################################################


# guess this is like using std::cerr in c++ and fprint() on an
# incorrect return value from a function call in c



# Runtime erros come up when a program is running, eg from incorrect
# input.  Python has a special way to deal with runtime errors, other
# languages do too.  It is done with exceptions which handle special
# error condititions that can occur.


# For example, trying to open a  file that doesn’t exist, converting a
# string to an integer when the string  turns out to be a word instead
# of a  number, or dividing  by zero will  usually cause a  program to
# crash, printing out  an error. Exceptions are a way  of taking these
# problems and handling  them in some way so that  the program doesn’t
# have to crash. For  example, if opening a file to  read it in fails,
# we can ask the user for a new filename.


#  Exceptions are handled in Python through “try-except blocks,” which
# are ways  of containing  code that might  create the  exception. You
# start with the statement “try,”  followed by a colon. Then, indented
# is  all  the code  for  which  you want  to  possibly  check for  an
# exception. Following that is  an except statement, identifying which
# error you  want to deal  with, and  finally, indented again,  is the
# code to run in case you do run into that error.



# try:
     #Commands to try out
# except <name of exception>:
     #how to handle that exception


#     There is a list of built-in exceptions for Python, arranged in a
# hierarchy,                                                        at
# https://docs.python.org/2/library/exceptions.html. There are a large
# number of different  exceptions defined and a  mechanism for letting
# users define  new ones. To  see a  list of the  standard exceptions,
# look  up  a  Python  language  reference.  A  few  useful  ones  are
# TypeError, OSError, and ZeroDivisionError.

# Avoid using exceptions  for cases that can and should  be handled at
# the point the problem is  detected.  Conversely, use exceptions only
# when the problem can’t be handled at the point of detection.
