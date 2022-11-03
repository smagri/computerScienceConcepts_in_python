#!/usr/bin/env python3

print("EX2: open file for writing in dir above current.")

myfileW = open("../fileOpen4writing", "w")


print("EX3: close open files in ex1 and 2.")
myfileW.close()


print("EX5: Ask user for filename and write numbers 1-10, one per line.")
enteredFileName = open(input("Enter a filename: "), "w")

for i in range(1, 11): # do not exceed 11 but include 10 and start from 1
     enteredFileName.write(str(i) + "\n")
enteredFileName.close()

print("EX4: WATCH VIDEO@17min: open file 'infile' and read and print each line.")
infileHandle = open("infile", "r")

print("When we reach the EOF an empty string is returned in python.")
lineFromFile = infileHandle.readline()
while lineFromFile != "":  #ie we hit end of file
     print(lineFromFile, end='') # supress the newline in each line
     lineFromFile = infileHandle.readline()

infileHandle.close()

#OR You could do this in python,  I don't like the look of this method
#though.  It's a type of for statement and .readline() can be left out
#and the EOF empty string comparison is not necessary.
print("Use python compact form of doing this using a for loop,\n"
      "EOF comparison and .readline() not needed then.")
infileHandle = open("infile", "r")
for lineFromFile in infileHandle:
     print(lineFromFile, end='')
infileHandle.close()


# see to fix this perhaps:
# Solution examples, best explained(some steal from stackoverflow):
#https://www.pythonpool.com/invalid-literal-for-int-with-base-10/
#https://www.yawintutor.com/valueerror-invalid-literal-for-int-with-base-10-in-python/
#https://www.edureka.co/community/30685/this-valueerror-invalid-literal-for-with-base-error-python

# I think the problem is that each line has an EOL and maybe file has EOF.
# EOL =CR LF or \r\n, and EOF is an empty string "" 

# The error message invalid literal for  int() with base 10 would seem
# to indicate that  you are passing a string that's  not an integer to
# the int()  function .  In other  words it's either  empty, or  has a
# character in it other than a digit.

# The reason  you are  getting this  error is that  you are  trying to
# convert a space character to an integer, which is totally impossible
# and restricted.

# use .isdigit() or .numeric() to find non iteger values like EOL and EOF???

# use int(float(value)), gets around it

# use: try: except:

# use .readlines() as it corrects the formatted output

# use: perhaps, stringName.strip('\r\n') to strip the CR LF from EOL
numLines=0
numSum = 0
lineNum=0
print("lineNum is=", numSum)


datafileHandle = open("data.txt", "r")
line = datafileHandle.read(1)
while line != "":  #ie we hit end of file
     if line == "\n":
          print("Newline found, ignore it as it's not the integer we want.")
          line = datafileHandle.read(1)
     else:
          print(line)
          numSum = int(line)
          print(numSum)
          line = datafileHandle.read(1)

#     lineNum = int(line)



# #print("lineStr is=", lineStr)
# #print(int(lineStr))
# while (lineStr != ""):  #ie we hit end of file
#      if (lineStr == ""):
#           print("EOF in while loop")
#      lineStr = fileHandle.readline()
#      lineNum = str(lineStr)
#      numSum += lineNum
print("average of numbers in data.txt is: ")
datafileHandle.close()

