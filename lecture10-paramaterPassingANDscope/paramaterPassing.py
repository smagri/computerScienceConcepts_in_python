#!/usr/bin/env python

###############################################################################
#                   ParameterPassing SCOPE and MUTABLE DATAa                  #
###############################################################################


# A function is defined by the  header and the body. The header starts
# with the keyword “def,” followed by the function name, followed by a
# list of parameters  in parentheses and a colon. Then,  we indent the
# body, and we can exit the body by returning some value.


# All of our  code together is called our program,  but we’ll call the
# “main  program” the  stuff  that actually  gets executed  first—that
# isn’t part of a function  definition. As our program gets processed,
# the first line that gets executed is a line from the main program.


# When we call the  function, there is a whole new  area of memory set
# aside for  that function  to work  in. This  is called  the function
# activation  record.  In  that area  of  memory, we  will first  have
# variables created for the parameters.

# Python does function calls with PASS By VALUE.



# The function  runs when  it is  called from main  in its  own little
# memory area,  and when something  is finally returned, that  is sent
# back out to the “main” program  memory area.  After that, the memory
# for  that  function is  all  freed  up.   The activation  record  is
# destroyed, leaving that memory free to use again in the future.  And
# our program goes on  to the next line of code from  the main part of
# the program.  Once  the fn memeory it uses  is distroyed(fn returns)
# main or anything else can't access the variables in it.


# When we  declare a global  variable in  the function, it  means that
# within  that  function, when  we  refer  to  that variable,  we  are
# referring to  the exact same  variable as  in the main  program. So,
# when we set the  value of a variable in the  function, we change its
# value in the main program.  In general, using global declarations is
# discouraged.


#Another way to get an effect that  seems a lot like pass by reference
#is to use  mutable variables.  A mutable variable  roughly means that
#the  variable  is changeable  when  passed  as  a parameter,  and  an
#immutable one is one that can’t change when passed as a parameter.


###############################################################################
# THERE ARE MUTABLE DATA TYPES - eg a List #Because lists are mutable,
# when we pass them as a parameter, the value in the list can actually
# change.

###############################################################################


###############################################################################
#       DEFAULT VALUES, taken if no parameter value is passes to the fn   .    #
###############################################################################
def calc_miles(gallons, mpg=20.0):
    return gallons*mpg

print( calc_miles(10.0, 15.0) )
print( calc_miles(10.0) )


