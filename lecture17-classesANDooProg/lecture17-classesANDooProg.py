#!/usr/bin/env python3


# Classes and  objects allow us  to combine operations and  data. When
# they are packaged all together, we have  the data we need as well as
# the operations that work with that data.

# A  class  can be  thought  of  as  the  general blueprint  for  some
# category,  while   the  objects  are  specific   instances  of  that
# category. In other words, the class  is a type, while each object is
# just a variable.


###############################################################################
#                               CREATING CLASSES                              #
###############################################################################

# Classes are the containers in which  we can package the data and the
# functions that  belong with the  data.  Classes are basically  a new
# type that a variable can take on, like integers, floats, strings, or
# lists.


# EVERYTHING that's INDENTED BELONGS TO the CLASS.
class BankAccount:
    # attributes in python, member variables in c++
    balance = 0.0
    deposits = [] # remember lists are mutable, initialize an empty list here

# First, we  can create an instance  of the class. Each  instance of a
# class is known as an object.  We create an object that’s an instance
# of a class by writing the class 1 84 | L e ct u r e 17 — C las s e s
# and  Obj  ect-  Or iented  Pr  ogr  a  mmi  n g  name,  followed  by
# parentheses. We  can assign  this instance to  a variable.   In this
# case, we have a class called BankAccount, and we create one instance
# of the class, which we assign to the variable my_account.


# The idea of classes and objects is common across many languages, but
# terms for the variables that are within objects vary. In Python, the
# variables that  are inside a class,  and help define the  class, are
# called “attributes”  of the class. In  Java, the parts of  an object
# are called “fields”; in C++, they are called “member variables.”


# In Python,  some attributes can be  set to apply equally  across all
# members of a  class, so that every object has  that attribute, while
# other  attributes   can  be  defined  individually   for  only  some
# objects. In the previous example,  “balance” was an attribute across
# the entire class—in fact, it was the only attribute of the class.


 # class instanciated/object created, called my_account
my_account = BankAccount()
your_account = BankAccount()
my_account.balance = 150.90
checking_account = BankAccount()
checking_account.deposits.append(100.0)
checking_account.deposits.append(150.0)
checking_account.deposits.append(20)
savings_account = BankAccount()

# accessing member data and methods with the . operator

###############################################################################
#                                 MUTABLE DATA                                #
############################################################################### 
# remember  LISTS  ARE MUTABLE,  so  have  the same  memory  locations
# always.  So  every object is  looking at the  same list in  the same
# memory location.  So values are the same froeach object.

print("my current account balance is $", my_account.balance)
print("your current account balance is $", your_account.balance)
print("the checking account deposits are: ", checking_account.deposits)
print("the savings account deposits are: REMEMBER LISTS ARE MUTABLE ",
      savings_account.deposits)



###############################################################################
#        METHODS define functions in a class                                  #
###############################################################################

# any initial  values set in the  class are going to  be shared across
# all instances, which leads to  problems with mutable data types. The
# alternative  is  to create  instance  variables,  which are  created
# separately for each instance of  the class. With instance variables,
# we never need to worry about the changes to one object inadvertently
# affecting the attributes of a different object.

###############################################################################
#        The sepcial method, init method, is also called the
#        constructor lets us get around initialising class variables
#        differently foreach object.
#
###############################################################################

################################################################################
# self parameteris special, it's automatically filled in.  The self
# parameter refers to the current instance of the object.  It allows
# us to referr to things within this particular instance of an object.
# So, if we write "self.balance", we mean the balance in this one
# instance.
################################################################################
# EXAMPLE, the __init_ function is executed whenever a new instance of
# the class, or object, is created.
print("Using the init fn or constructor for instantiating objects in python:")
class BankAccount:
    balance = 0.0
    def __init__(self, ):
        "The __init__(self, args), args are optional, \n"
        "is called the init fn or costructor."
        # this makes the deposits list unique for each instance
        self.deposits = []

checking_account = BankAccount()
savings_account = BankAccount()
checking_account.deposits.append(100.0)
print("the checking account deposits are: ", checking_account.deposits)
print("savings account deposits are, using __init_ constructor is",
      savings_account.deposits)



# In general, we should try to use instance variables instead of class
# variables. So, instead of creating  a “balance” class variable, it’s
# better to create an instance variable  in the init function, like we
# did  for deposits.   Practically, it’s  not much  different, but  it
# helps ensure  that we know that  the variable is something  that can
# change from  object to object.   Generally, the only time  we should
# use class variables  is when there’s some single  value, usually one
# that’s not  likely to  change, that  should be  the same  across all
# instances of the class.


# Our init command created separate instance variables and initialized
# those individual instance variables independently.
