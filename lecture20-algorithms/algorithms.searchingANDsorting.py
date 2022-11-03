#!/usr/bin/env python
# -*- coding: utf-8 -*-



# A few of the most well-known algorithms for searching and sorting

# Algorithms

# Say for example we are trying to find v value in list L, is it there or not.


###############################################################################
#                                LINEAR SEARCH                                #
###############################################################################
# Linear searching, you go down the  line, looking at each item in the
# list.  Write this function.

def isIn(L, v):
    # is v in list L, return true or faluse
    i=0
    while (i<len(L)):
        if L[i] == v:
            return True
        else:
            i+=1

    return False #if we haven't retruned by now v is not in list L



favorite_foods = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings',
                  'pecan pie', 'ice cream']
print(isIn(favorite_foods, 'gumbo'))
print(isIn(favorite_foods, 'coconut'))


# However, using the built-in function in the _in_ command does the
# same as isIn().  This linearly searches each element of the list. 
if 'gumbo' in favorite_foods:
    print("using LINEAR SEARCH, gumbo is in favourite_foods list")
    print(True)
else:
    print("usign LINEAR SEARCH, gumbo is NOT in favourite_foods list")
    print(False)
    
if 'coconut' in favorite_foods:
    print("using LINEAR SEARCH, coconut is in favourite_foods list")
    print(True)
else:
    print("using LINEAR SEARCH, coconut is NOT in favourite_foods list")
    print(False)




###############################################################################
###############################################################################
# SORTING A LIST ALLOWS YOU TO SEARCH FOR VALUES MORE EFFICIENTLY.
###############################################################################
###############################################################################



###############################################################################
# SELECTION SORT, in-place sort:
###############################################################################

#Sort from smallest to largest. we  look through all of our values and
# find the  smallest one. We put  that into the first  place.  We then
# repeat that process to find the next-smallest item and put that into
# the  second  place.  Each  time,  we  have to  look  at  all of  our
# remaining  items  so  that  we  can  select  the  one  that  is  the
# smallest-remaining item.   That is where  we get the  name selection
# sort.
 
# Another  decision that  comes up  when  sorting is  whether to  move
# around e  original elements of the  list or make a  copy.  Lists are
# mutable data types, so you have  the ability to reorder the elements
# themselves, if you  want.  If you directly sort the  elements of the
# list, that is called an in-place sort.  In contrast, an out-of-place
# sort means that you create a new list that is a copy of the original
# one.  In this case, the original list stays unchanged, while we also
# have a new, sorted, list to work with.  Choosing whether you want an
# in-place or  out-of-place sort  will depend on  whether you  need to
# maintain the  original order  for some  reason. If  so, you  want an
# out-of-place sort. The  more common case, though, is to  just do the
# sort in place  where you just swap the two  elements, from where you
# pull out to where you put in.

# Choosing  whether you  want an  in-place or  out-of-place sort  will
# depend on whether  you need to maintain the original  order for some
# reason. If so, you want an  out-of-place sort. The more common case,
# though, is to just do the sort in place.


# In the  selection sort,  we can  sort in place  by making  sure that
# every time we  place a new element into its  final position, we swap
# it with an existing element.
def selectionSort(L):
    maxindex = len(L) -1 # as index starts from zero

    for i in range(0,maxindex-1):
        #find the smallest remaining
        min_index = i
        for j in range(i+1, maxindex+1):
            if L[j] < L[min_index]:
                # SELECT the next smallest index from the rest/remaing
                # of your list by searching the entire list and
                # comparing it to the current smallest value index
                min_index = j
                #swap that item
                temp = L[i]
                L[i] = L[min_index]
                L[min_index] = temp



###############################################################################
# INSERTION SORT, in-place sort:                                                             #
###############################################################################

# Selection sort works, but it spends  a lot of time going through the
# entire unsorted list on every iteration. Insertion sort is a different
# approach that can  be much faster and simpler. For  insertion sort, at
# iteration n, we’ve sorted the first  n elements. So, the only thing to
# do on each iteration is add one more element into the right spot.

# With insertion sort, we start with the first item—and only the first
# item.  When we  take the second item,  all we do is  compare it with
# the first  item and insert it  in whichever position is  correct. We
# continue making iterations in this way,  where each time we take one
# more value and insert it into the list of sorted items. That’s where
# we get the name “insertion sort.”


def insertionSort(L):

    for i in range(0,len(L)): #as we need to keep a space in the front

        #of list in case
        print("")
        temp = L[i]
        print("temp=", temp)
        j = i-1 # work your way down the list from the current location
        print("before while loop i=", i,",j=", j)
        while (j>=0) and (L[j]>temp):
            print("i=", i,",j=", j)
            L[j+1] = L[j] # if down the list we get a value
            j -=1
            print("in while, list is: ", L)

        print("")
        print("j+1 is", j+1)
        L[j+1] = temp
        print("outside while, list is: ", L)

################################################################################
# PYTHON has a BUILD IN SORTING FUNCTION.  Fora list sort() for an
# inplace sort and sorted() for an out of place sort
#
################################################################################
#sort(L)
#sorted(favorite_foods)


###############################################################################
#                            BINARY SEARCH IMPLEMENTATION                     
###############################################################################
# You need to sort list first before applying this algorithm.  Where
# we reduce the search range by a factor of 2.  This is much more
# efficient than the linear search.  Implement here from pseudo code
# for practice.

def binaryIn(L, v):

    if len(L) < 1: return False # too avoid waisting time if the list is empty
    
    minIndex = 0
    maxIndex = len(L) - 1

#   if L[minIndex] == v or L[maxIndex] == v:  return True
    
    if L[minIndex] == v or L[maxIndex] == v:
        return True

    while minIndex < (maxIndex-1):
        midIndex = minIndex + ( (maxIndex-minIndex) // 2)

        if L[midIndex] == v:
            # value found
            return True
        elif L[midIndex] < v:
            # look in lower half range next
            minIndex = midIndex
        else:
            # looki in upper half range next
            maxIndex = midIndex

    # if we haven't returned by now the value v is not in the list L
    return False


    ###########################################################################
    # NOTE: need to sort list before applying binaryIn()
    #
    ###########################################################################

print("\nUN-SORTED favourite_foods ARE:")
print(favorite_foods)

selectionSort(favorite_foods)

print("selectionSort() SORTED favourite_foods ARE:")
print(favorite_foods)

print("")
if (binaryIn(favorite_foods, 'gumbo')):
    print("using BINARY SEARCH, gumbo is in favourite foods")
else:
    print("using BINARY SEARCH, gumbo is NOT in favourite foods")
    
    
if (binaryIn(favorite_foods, 'coconut')) == True:
    print("using BINARY SEARCH, coconut is in favourite foods")
else:
    print("using BINARY SEARCH, coconut is NOT in favourite foods")


# this is an IN PLACE, or insertion SORT, built in python function
print("")
print("UN-SORTED favourite_foods ARE:")
print(favorite_foods)
print("sort() METHOD, built in python IN-PLACE/INSERTION sort and merge sort "
      "on favourite_foods is:")
favorite_foods.sort()
print(favorite_foods)


# this is an OUT OF PLACE(makes a copy of original to order), built in
# python function.
print("")
print("UN-SORTED favourite_foods ARE:")
print(favorite_foods)
sorted_favourites = sorted(favorite_foods) # built in python function
print("sorted() Fn out-of-place sorted, built in python fn, favourte_foods are:")
print(sorted_favourites)
sorted_favourites = sorted(favorite_foods, reverse = True) # built in python function
print("REVERSE sorted() Fn out-of-place sorted, built in python fn, favourte_foods are:")
print(sorted_favourites)



print("")
print("UN-SORTED favourite_foods ARE:")
print(favorite_foods)
insertionSort(favorite_foods)
print(" Fn out-of-place sorted, built in python fn, favourte_foods are:")
print(favorite_foods)


print("")
myList = [6, 5, 10, 2, 7]
insertionSort(myList)
print("")
print("mylist is", myList)


print("")
myList = [6, 5, 10, 2, 7]
selectionSort(myList)
print("")
print("mylist is", myList)



