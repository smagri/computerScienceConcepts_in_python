#!/usr/bin/env python


print("ex1:")
def something1(a):
    a = 0
b=3
something1(b)
print(b) # b=3


print("ex2: LISTS are mutable in fn's, so like a global variable.")
def something2(a):
    a[0] = 0
b=[1,2,3] # b is a list which is mutable and thus delta it in fn
          # delta'sit in main
something2(b)
print(b) # b=0,2,3


print("ex3: paramaters in fn call override any defaults in fn def.")
def something3(a, b=2, c=3, d=4):
    return a + b + c + d
val = something3(3, 10, d=5)
print(val) # val =3+2+3+5=13 or 3+10+3+5=21


print("ex4: ")
def something4():
    a = 3
a = 2
something4()
print(a) # a=2


print("ex5: using global variables in a fn:")
def something5():
    global a
    a = 3
a = 2
something5()
print(a) # a=3


print("ex6:")
def something6():
    a[0] = 0
a = [1, 2, 3]
something6()
print(a) # a=[0,1,3]



print("ex7:")
def something7(a, b):
    print (a, b) #  2,1
a = 1
b = 2
something7(b, a)


print("ex8: increace all the elements in the list [1,2,22] by 1")
a = [1, 2, 22]
for i in range(len(a)):
    a[i] +=1
print(a)


print("ex9: multiply 1-4 parameters together returning the product of them")
def times4(a, b=10, c=1, d=3):
    return a*b*c*d
print(times4(10)) # 100
