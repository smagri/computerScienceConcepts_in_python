#!/usr/bin/env python3

# If  you want  to  see how  many are  already  installed, try  typing
# “help(“modules”).”


# Basically,  every Python  program can  be  regarded as  a module  in
# waiting, because  every “.py” file  can potentially be  imported for
# use as a module.  So, in  that sense, there are probably millions of
# potential  “modules”  floating  around   out  there.   |  But  while
# technically any  Python can be  regarded as a  module, realistically
# what raises a program  to the level of a module  is that the program
# provides a  set of functions,  classes, and constants that  all work
# together  to accomplish  a  common  goal. A  good  module will  also
# provide  a “clean”  interface to  the user,  revealing only  as much
# about how  it works  as is  needed for  the user  to use  the module
# effectively.


# For example, the standard library’s  module called “math” has a list
# of about  45 functions that  are included.   There is a  square root
# function,  and there  are  functions for  computing greatest  common
# divisor or cosine. In addition, some values are defined, such as the
# value of  pi.  To write  a program  using these commands,  we’d just
# import the math  module. Then, we can use “math.cos”  to compute the
# cosine and “math.pi” to  get pi. If we were going to  be doing a lot
# of math,  we might bring in  the whole math module  by writing “from
# math import *.”   We can then write our math  calculations even more
# directly, without having to put “math.” in front of each one.


# One  thing  that helps  you  find  what  you  want is  that  modules
# themselves  are  often  bundled  together  into  what  Python  calls
# packages. A package is a collection of modules.  A package can bring
# in many modules, and we can  access those modules by adding an extra
# period and  then the name of  the subpackage or module.  The rest of
# the import works just like before.

# Python also has  a recommended tool for  installing packages, called
# pip.  You can install a Python  package using pip by typing the line
# “python –m pip install <package name>.”


# Once you’ve installed  a package on your computer, using  it is just
# the same as  the standard Python library. You  just import whichever
# packages or  modules you want  to use and  go from there.   For most
# packages, you  can get a  list of  commands that a  package provides
# from within  Python.  After  importing the module,  you can  use the
# “dir”   command,  passing   in   the  module   name.   import   math
# print(dir(math))

# If the  developers of the  module were good about  using docstrings,
# you should  be able  to write  “help(),” with  the function  name in
# parentheses, to find out more about the function, too. More helpful,
# however, is to look at the  online documentation for that package to
# see how to use it.


