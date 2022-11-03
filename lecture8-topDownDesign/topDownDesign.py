#!/usr/bin/env python3

###############################################################################
#     GOOD EXAMPLE for dealing with .cvs files and processing file data!!!
#
# This may be useful for processesing illabunda weather data.
###############################################################################

#weather.cvs
#date, highTemp, lowTemp, rainfall

# weather.csv date, high temperature on that date, the low temperature
# on that date,  and the rainfall on that date.


# This type of  file is called a comma-separated value  (CSV) file, or
# sometimes a comma-delimited file. For  data that starts out in Excel
# or another  spreadsheet program,  it’s easy  to use  the spreadsheet
# program to  output the data  values, separated  by commas, as  a CSV
# file.

# HOWTO GET CVS FILE from CUT and PAST
# To get  weather data  like this, you  can go to  any one  of several
# weather  sites, some  of  which  will let  you  download  it into  a
# spreadsheet, but you can ALSO CUT  AND PASTE DATA INTO A SPREADSHEET
# then you can save it in as a CVS file yourself.

###############################################################################
#                https://docs.python.org/3/tutorial/index.html                #
#                       To refresh your mind on python syntax.                #
###############################################################################

fname = input("Enter the name of the data file: ")
fhandle = open(fname, 'r')


# We’ll  be reading  in line  after  line, so  this is  going to  mean
# looping through all the lines of the file.  For each of those lines,
# we need  to read in  the line as a  string— remember that  our input
# comes in  as a  string.  Then,  we need to  pull out  the individual
# pieces of data from the string and finally store them in a list that
# we can access  later.  to access individual strings in  the list use
# the .strip() python method.

# eg string delimited by comma and values assigned into a,b,c variables.
# a, b, c, d = line.split(',')

dataListOFlists = [] # a LIST OF LISTS

# #############################################################################
#     This is the COMPACT PYTHON FORM OF READING LINES FROM FILES to EOF      #
###############################################################################
for line in fhandle:
    date, h, l, r = (line.split(','))

    ###########################################################################
    #                          WE NEED TO USE float()                         #
    ###########################################################################
# The following are totally acceptable in python:

# passing a string representation of an integer into int
# passing a string representation of a float into float
# passing a string representation of an integer into float
# passing a float into int
# passing an integer into float

# But you  get a ValueError if  you pass a string  representation of a
# float  into int,  or  a  string representation  of  anything but  an
# integer (INCLUDING EMPTY STRING, ie EOF  = "", and line contains EOL
# character).  If  you DO want  to pass  a string representation  of a
# float to an int, as @katyhuff points out above, you can convert to a
# float first, then to an integer:

# see:
# https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
# and links in operatinsWithLists.py

# Other ways of doing it, refer to link above.
# The reason you had ValueError is because int cannot convert an empty
# string to the  integer. In this case you'd need  to either check the
# content of the string before conversion, or except an error:

# THIS WILL BE USEFULL for lecture6 ex11 I think, for me using while
# loop with EOF and EOL.

# HERE I THINK using .strip() avoids reading in EOL and EOF, maybe use
# split newline in ex4???
    lowTemp = int(l)
    highTemp = int(h)
    rainfall = float(r)

    m,d,y = date.split('/')
    month = int(m)
    day = int(d)
    year = int(y)

    dataListOFlists.append([day, month, year, lowTemp, highTemp, rainfall])


# MULTIPLE WAYS TO PRINT THIS LIST OF LISTS

# PRINTS HORIZONTALLY
# print(dataListOFlists)

# for i in dataListOFlists[i]:
#     print(dataListOFlists[i])

# PRINTS VERTICALLY
for i in range(len(dataListOFlists)):
    print(dataListOFlists[i])



###############################################################################
# PROCESS the data, EXTRACT data from a particular DATE
############################################################################### 


# HOWTO specify EMPTY LIST in python
needdata = []
aday = []


#Get date of interest, notice all dates have year 2000, so we can
#ignore that for this example using weather.cvs
month = int(input("For the date you care about, enter the month: "))
day = int(input("For the date you care about, enter the day: "))
print(month)
print(day)

print("Using book method:")
for aday in dataListOFlists:
      if (aday[0] == day) and (aday[1] == month):
          print("Day user entered was found.")
          print("NOTE: HOW YOU MUST use .append([]) to add to list.")
          # NOTE: YOUR NED ([]) to access elements in lists of lists
          # YEAR, LOWTEMP, HIGHTEMP, RAINFALL
          needdata.append([aday[2], aday[3], aday[4], aday[5]])

print("print book method:")          
for i in range(len(needdata)):
    print(needdata[i])



# need to shorten name of dataListoflists to fit on one line, trying
# to continue line did not work.


print("Using my alternative method, accessing a list of lists like a 2d array.\n"
      "Book version is more compact but I mine is more intuitve to understand?")
print("NOTE: HOW YOU MUST use .append([]) to add to list.")
for i in range(len(dataListOFlists)):
    # can't seem to work out how to do a continuation in a method argument
    if (day  == dataListOFlists[i][0]) and (month == dataListOFlists[i][1]):
        needdata.append([dataListOFlists[i][2], dataListOFlists[i][3],
                         dataListOFlists[i][4], dataListOFlists[i][5] ])
        print("enter loop i=", i)

# print VERTICALL
print("print data to analyse VERTICALLY:")
for j in range(len(needdata)):
#    pass # so nothing but needed if you have an empyt for statement
    print(needdata[j])

# print HOROZONTALLY
print("print data to analyse HORIZONTALLY:")
print(needdata)

# ANALYSE DATA, ie needdata, the data we are interested
# determine highst and lowest temperature and average of high and low.

# no real need to analyse all data as per book, just iterate through
# list of lists via compact book way to get fundamentals

highest_temp = 0
lowest_temp = 0
average_highest_temp = 0
average_lowest_temp = 0

sum_min_temp = 0
total_num_dates = 0


for day in dataListOFlists:
    # average and sum of minimum temperatures
    sum_min_temp += day[3]
    total_num_dates += 1

avg_min_temp = sum_min_temp/total_num_dates
    
print("The total of minimuim temperatures is: ", sum_min_temp)
print("The total number of temperatures is: ", total_num_dates)
print("The average of the minimuim temperatures is:", avg_min_temp)

    
fhandle.close()
