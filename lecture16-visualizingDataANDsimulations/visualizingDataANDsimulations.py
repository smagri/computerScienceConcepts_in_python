#!/usr/bin/env python3

# One  of  the best  packages  to  create  visualizations of  data  is
# matplotlib.   It  has a  very  wide  range  of capabilities  and  is
# probably  the  most  well-  known and  popular  Python  package  for
# creating PLOTS, GRAPHS, AND CHARTS FROM DATA.

# python –m pip install matplotlib

# Installing   matplotlib  will   require  installing   several  other
# libraries, too.


from matplotlib import pyplot
# pyplot.axes()
# pyplot.show()


# We learn  how to  use graphical  tools like this  by looking  at the
# documentation. In particular, the API is the application programming
# interface. The API documentation lists the various commands that are
# provided and the  details of how each is used.   For matplotlib, you
# can see the key plotting commands if  you follow the link at the top
# of the  page to “pyplot.”  That gives you  a whole list  of commands
# provided in pyplot, and  if you click on each of  them, it will give
# you a  more detailed description of  what the command does  and what
# parameters it takes in.


# The plot command can take in few  lists. The first one gives all the
# x-values. The second  one gives all the y-values.  Parameters to the
# axis command.  The  parameter is a list of four  numbers, giving the
# minimum  and maximum  extents for  the  x-axis and  the minimum  and
# maximum for the y-axis.

# METHOD1:
pyplot.plot([0,1,2,3,4,5], [0,1,4,9,16,25])
pyplot.axis([0,5,0,25])
pyplot.show()

# METHOD2, more compact implementation, but must put at top of file, a
# new from.

# from matplotlib.pyplot import plot, axis, show

# xlist = range(0,6)
# ylist = []
# for i in xlist:
#     ylist.append(i*i)
#     plot(xlist, ylist)
#     axis([0,5,0,25])
#     show()
