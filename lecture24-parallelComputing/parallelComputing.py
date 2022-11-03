#!/usr/bin/env python3

# In the  1960s, Gordon Moore,  one of the  founders of Intel,  made a
# famous prediction: that  the number of transistors  on an integrated
# circuit would follow  an exponential growth rate,  doubling every so
# many years. This idea came to be  known as “Moore’s law,” and it has
# driven the computer chip design  industry for many years. And though
# the  rate  of  growth  may  have  slowed,  we’re  still  seeing  big
# improvements  as  our  computers  become smaller  and  faster.   But
# there’s a big difference between  simply having more transistors and
# being able to use them effectively.  As chip designers have had more
# and more  to work with,  it’s been increasingly difficult  to figure
# out how to  use those additional transistors to get  bigger and more
# powerful processors. Instead, designers  have increasingly turned to
# parallelism to make use of  the resources available.  Instead of one
# bigger  processor,   they’ve  used  the  transistors   to  make  two
# processors—or  four processors—on  the same  chip. This  has led  to
# dual-core, quad-core, and multicore home computers.

# When a single  processor becomes faster, we  could expect everything
# running on it to run faster. But putting in a dual-core processor—in
# other  words,   using  parallelism—doesn’t  necessarily   cause  our
# programs to run faster. The  particular computation we’re doing will
# determine  whether  we can  actually  make  use of  the  parallelism
# provided.


# But  to make  full use  of  parallel processing,  we need  to do  it
# explicitly.  We’ll  focus   just  on  Python  on   a  standard  home
# computer. And,  for this  case, the  main way  we take  advantage of
# parallelism   is  through   threading,  or   multiprocessing.   With
# threading, we’ll be  creating functions that can run  in a different
# process, or “thread,”  than the main program. The  main program will
# spawn these  other processes,  each of which  will be  running their
# respective   functions.  Those   spawned   processes  will   execute
# separately  from  the  main  program,  and  if  there  are  multiple
# processors available (such as on  a multicore computer), they’ll run
# on these different  cores at the same time—that is,  in parallel. If
# there’s just a single core  central processing unit, these processes
# will  still  run  just  fine;   there  just  won’t  be  any  overall
# improvement in the performance.


# The following  is a  very simple example  of a  multiprocess “Hello,
# World” program.  See  .pdf for explination, but basically  we have a
# 'main' program thread  and one that runs a  print_function() fn.  If
# you have multiple cores on your  pc they will run on different cores
# I think.   Will work  on a  single processor but  you won't  get the
# speed benifits.

from multiprocessing import Process
import time


# def print_function():
#     print("Hello, World!")


# if __name__ == '__main__':
#     p = Process(target=print_function)
#     p.start()


# def print_function(name):
#     print("Hello,", name)

# if __name__ == '__main__':
#     p = Process(target=print_function, args=("John",))
#     p.start()


# Notice that our function just takes in a number and prints a message
# “Printing from process” and then the number that was passed in.


# In our main routine, we’ll create a list of 20 processes. We’ll have
# a loop, with  i ranging up to  20, and for each one,  we’ll create a
# process in  which “print_process” is the  function and i is  used as
# the parameter. After that, we’ll  go through and actually start each
# process, in a separate loop.

# I  don't  seem  to  get  the  same  result  as  the  book.   Setting
# print_process() to run in parallel should produce out of order print
# statemets as each process can run  on a different processor which in
# turn have  other processes  running on  them so  the order  of print
# statements should be different???  Read  book for timeslice stuff is
# interesting.


def print_process(number):
    print("Printing from process", number)

if __name__ == '__main__':
    process_list = []
    for i in range(20):
        p = Process(target=print_process, args=(i,))
        process_list.append(p)

    for p in process_list:
        p.start()

