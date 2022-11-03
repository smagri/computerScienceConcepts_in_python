#!/usr/bin/env python3

# Files are closely tied with strings, because the typical file format
# that you  will write to and  read from will essentially  be one long
# string. The locations  of those files are also given  by strings.

# OPENING and CLOSING files:

# Closing the file makes sure that everything in the file is left in a
# nice condition  so that nothing  is corrupted. Also, it  prevents us
# from accidentally opening too many files at the same time.

# program filename  = open(actual filesystem filename, premissions)
# permissions = r => read from file, error if filename does not exist
# permissions = w=>write to file, from start of file, file created
# permissions = a=>append to file, add to the end of the file, file created


# myfileR/W is program file VARIABLE, file handle/file descriptor/file I guess
print("Open and close a file for reading called myFilename4reading,\n"
      "when reading the file must already exist on the filesystem.")
myfileR = open("myFileName4reading", "r") 
myfileR = myfileR.close()

print("Open myfileW on our filesystem and write something to it.\n"
      "This creates the file if it doesn't exist, as .append does.")
myfileW = open("myFileName4writing", "w")
myfileW.write("hello world writing to files in python.")
myfileW = myfileW.close()


# But there’s another way we can write  this code in Python. It makes it
# easier to know when you have the  file open and when you don’t, and it
# helps ensure  that your file  always gets closed.  “with.”  This opens
# the  file.  Then,  the  stuff  you   want  to  do  with  the  code  is
# indented. For  all that  indented code,  we can  use the  opened file,
# named “myfileR/W”  in this case,  WHEN WE LEAVE THE  INDENTED PORTION,
# THE FILE WILL BE CLOSED for us AUTOMATICALLY.

with open("myFileName4reading") as myfileR:
    print("Opened myFilename4reading with the with statement, this closes file\n"
          "automatically after its indented code is executed.")

print("The .write command ONLY WRITES STRINGS TO a FILE,\n"
      "and only one at a time. You must also put in your own newline.\n"
      "REMEMBER print() PUTS its own NEWLINE at the END OF A STRING.")


# READING from an exisiting file
print("Reading a line from a file with .readline needs line to end in newline.")
myfileW = open("myFileName4writing", "r")
lineFromFile = myfileW.readline() # reads one line at a time
print("line from myFileName4writing is: ", lineFromFile)
myfileR.close()


# ACCESSING FILES IN DIRECTORIES or on the FILESISTEM

print("You can give a path to the filename variable in file open() commands.\n"
      "Otherwise the path is assumend as the current directory\n"
      "Paths can be relative to the current directory also.")
