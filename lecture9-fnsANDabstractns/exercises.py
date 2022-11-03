#!/usr/bin/env python3


# just picking out some interesting ones here


###############################################################################
#                          REVISION range() STATEMENT                         #
###############################################################################
#
#
# range STATEMENT:
# ---------------

# * specifies starting index of 0, max index within range parentheses,
#   itteration increment is 1.

# * If  there are  two values  in the  parentheses we  increment by  1
#   starting from the first value and not exceeding the second.

# * If there are three numbers, start index, limit index and increment
# * amount.  If the increment amount is -ve you countdown.

print("ex1: ans: XXXXX")
def something1(a, b):
    for i in range(a):
        print(b,end='') # REMOVE EOL from print
something1(5, 'X')
print("")

print("ex2: ans: 4, ie countdown from 3 to 2 and not exceeding 2, ie !<=2")
def something2(a, b):
    for i in range(a):
        b = b*b
        return b
print(something2(3,2))


print("ex3: ans: 4 6")
def something3(a):
    return a-1, a+1
a, b = something3(5)
print(a, b)


print("ex4: ans: give a list to a for loop, iterate over it\n"
      "sum and subtract all elments, ")
def something4(a):
    sum = 0
    for b in a:
        if b < 0:
            sum -= b 
        else:
            sum += b
    return sum

# sum = 2, 2--4=6, 9, 10, 17, 21
print(something4([2, -4, 3, -1, 7, -4]))


def something5(a):
    sum1 = 0
    sum2 = 0
    for i in range(len(a)): # len(a)=6
        if i%2 == 0: # calculate REMAINTER
            sum1 += a[i]  # 2, 6, 12=sum1
        else:
            sum2 += a[i] # 1, 4, 9=sum2
    return sum1, sum2

x, y = something5([1, 2, 3, 4, 5, 6])
print(x,y)


def ex6(aint, astr):
    print("exercise 7")
    
    for i in range(aint): # index i=0 to not exceed value, 0, 1, 2 == aint times
        print(astr)
    return
        

ex6(3, "simone")


print("ex8:\n"
      "a fn that takes in 3 numbers and returns the one in the middle: 7,9,12")
listOfNums = [7, 9, 12]

def middleNum(listOfNums):
    middleIndex = len(listOfNums) // 2  # getsd a whole number quotient
    return listOfNums[middleIndex]

print("middle number is: ", middleNum(listOfNums))


print("ex9:\n")


