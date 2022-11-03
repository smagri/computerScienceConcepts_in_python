#!/usr/bin/env python3

# The idea  of object-oriented design  is encapsulation, where  we put
# together the  data, and  functions that  work on  that data,  into a
# single package. But  there are two other  aspects of object-oriented
# programming— inheritance and polymorphism.

###############################################################################
#                                 INHERITANCE                                 #
###############################################################################


class FootballPlayer:
    # GLOBAL members common to all children of this PARENT CLASS or
    # BASE CLASS or SUPERCLASS Footballplayer
    name = "John Doe"
    team = "None"
    def printPlayer(self):
        print(self.name+" playing for the "+self.team+":")

    def isGood(self):
        print("Error! isGood is not defined!")
        return False


    # CHILDREN or DERIVED class or SUBCLASSES of Footballplayer class,
    # NOTE: parent classname needs to be passed in.as parameter.
class Quarterback(FootballPlayer):
    pass_attempts = 0
    completions = 0
    pass_yards = 0

    def completionRate(self):
        return self.completions/self.pass_attempts

    def yardsPerAttempt(self):
        return self.pass_yards/self.pass_attempts

    def isGood(self):
        return (self.yardsPerAttempt() > 7)


class RunningBack(FootballPlayer):
    rushes = 0
    rush_yards = 0

    def yardsPerRush(self):
        return self.rush_yards/self.rushes

    def isGood(self):
        return (self.yardsPerRush() > 4)



# can this go in a main.py file:

player1 = Quarterback()
print(player1.name)
print(player1.pass_yards)


# This is  creating instances  of child  classes and  accessing member
# variables  to  set  them,  in python  member  variables  are  called
# attributes.

# We can also inherit methods as well as attributes or member variables.


player1 = Quarterback()
player1.name = "John"
player1.team = "Cowboys"
player1.pass_attempts = 10
player1.completions = 6
player1.pass_yards = 57
player2 = RunningBack()
player2.name = "Joe"
player2.team = "Eagles"
player2.rushes = 12
player2.rush_yards = 73


# Notice  that   we  can  call   printPlayer  for  both   player1  and
# player2.  Because  the  method  is   defined  in  the  parent,  it’s
# automatically  inherited by  the children.  We can  also call  those
# statistics  methods  that  are  specific to  each  of  the  children
# classes.

print(player1.printPlayer())
print("player1 completion rate is: ", player1.completionRate())
print("player1 yards per attempt is: ", player1.yardsPerAttempt())
print("player1 pass attempts: ", player1.pass_attempts)
print("player1 completions: ", player1.completions)
print("player1 pass yards: ", player1.pass_yards)

print(player2.printPlayer())
print("player2 yards per rush is: ", player2.yardsPerRush())
print("player2 pass yards: ", player2.rush_yards)


# comment #####################################################################
# Just like  in biology, where you  can inherit traits from  more than
# just  one  parent,  CLASSES  CAN INHERIT  PROPERTIES  FROM  MULTIPLE
# PARENTS. But for  the most part, you should stay  away from multiple
# inheritance. It can  make your code more confusing  to follow. Plus,
# IT’S VERY  RARE THAT  MULTIPLE INHERITANCE  IS ACTUALLY  THE “RIGHT”
# SOLUTION TO YOUR PROBLEM.
# comment #####################################################################


###############################################################################
#                                     POLYMORPHISM                            #
###############################################################################

# Polymorphisim means which means that a function, or method, can take
# on many different forms, depending on the context.


playerlist = []
playerlist.append(player1)
playerlist.append(player2)
for player in playerlist:
    player.printPlayer()
    if (player.isGood()):
        print("  is a GOOD player")
    else:
        print("  is NOT a good player")

# When the Python compiler sees the  call to isGood, it first looks at
# the  definition of  isGood  in the  child class.  If  there’s not  a
# definition of that  method there, it will look at  the parent to see
# if the  method is  defined there.  Inheritance  is useful  if you’re
# defining your own  set of classes, but we can  actually inherit from
# any other class.


# Python even lets you treat basic types like strings or integers as a
# parent  class.  Especially  useful  is  the fact  that  we  can  use
# inheritance to  create our own  exceptions (which are used  to catch
# errors that would otherwise cause the program to crash).???


###############################################################################
#                               JSON and PICKLE                               #
###############################################################################

# JSON(JavaScript Object Notation) and pickle are two important Python
# modules that make objects much more usable, they are in the standard
# library.   JSON  uses  syntax  for   objects  similar  to  Java  and
# Javascript. JSON  groups information in objects  using curly braces,
# with  each attribute  written as  an attribute  name, followed  by a
# colon, followed by the value. The  value can be a new object, nested
# inside the previous object.  It  is independent of the language that
# it was  produced in. For  this reason, JSON  is the most  common way
# that  data files  are transmitted  over the  web.  Also  note it  is
# string based.

# Python's JSON module has commands  that let us convert most data(but
# not all data types) to and from JSON string.

# PICKLE ######################################################################

# Pickle is  a module  that lets  you read and  write data  other than
# strings more easily. Pickle lets us  read and write data from a file
# in binary  format (which is how  most files you encounter  every day
# are stored, from images to  word-processing files). And it works for
# even more data types than JSON.  Pickle is a Python-specific format,
# though. If  you write a file  using pickle commands, it  needs to be
# read by another  Python program also using  pickle commands.  Pickle
# should not be used  for writing data that you need  to send to other
# people, and you should never read pickle- produced files from others
# unless you are certain of the  source, because it’s easy for them to
# contain malicious data.


