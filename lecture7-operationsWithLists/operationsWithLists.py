#!/usr/bin/env python

# lists are arrays in python, arrays being specific efficent version
# of them, you should generally use lists instead of arrays in python
# They are dynamically resizeable and the len function gives you the
# length of the list.


# Strings are actually a slight variation  on a list.  That means that
# slicing on strings  works basically like slicing on  lists.  The one
# big difference is that  we can't assign to a string  the same way we
# can with  lists.  ie, we  can't delete  parts of strings,  or insert
# strings in  the middle, as  we can with  regular lists.  You  need a
# separate set of commands to manipulate strings.

# Python lets  you create  lists in  which you  have a  combination of
# different types.  Most languages require an  arry to be all stuff of
# the same type, but in Python, it's okay to have a list of items with
# an integer, a float, a string,  and another list, for example.  This
# is useful when you want a group unlike things togeter.

# tuples are like immutable lists of three elements only???

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("sjm: print beginnng  to end of list, ie entire list")
print (mylist)

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("1. print second element of list")
print (mylist[1])

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("2. print elements 2, 3 and 4")
print (mylist[2:5])

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("3. print first three elements of list")
print (mylist[:3])

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("4. print 9th element to end of list")
print (mylist[8:])

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("5. print beginnng  to end of list, ie entire list")
print (mylist[:])

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("6. print last element of the list")
print (mylist[-1])

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("7. print the last three elements of the list")
print (mylist[-3:])


mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("8. print entire list")
print (mylist)


mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("9. print entire list with for loop")
for i in mylist:
    print (i)

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
mylist[3] = 100
print ("10. set fourth element of list to 100")
print (mylist)

mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
print ("11. setting list itterator i=0 has no effect over itteration, "
       "print entire list len() if list times.\n"
       "NOTE: 'print space() is  necessary!!! if printing within for loop,\n"
       "outside for loop is as per usual.")
for i in mylist:
    i = 0
    print (mylist)


mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
mylist.append(100)
print("12. append 100 to end of list")
print(mylist)


mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
mylist[1:5] = []
print("13. remove second element to 5th element")
print (mylist)


mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
mylist[2:8] = [100, 200]
print("14. replace element 3-8 with 100,200")
print (mylist)


mylist = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
mylist [2:2] = [100]
print("15. replace third element with 100")
print (mylist)


print("16. --------------------------------")
ages = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
minor_ages = []
for i in range(len(ages)):
    if (ages[i] < 18):
        minor_ages.append(ages[i])
    
print ("minor_ages are:")
print (minor_ages)


print("17. --------------------------------")
names = ["sim", "rich", "aj"]
ages = [52, 45, 11]
names_ages = names + ages
print(names_ages)
