Opening Files:
f = open('file.txt', mode = "r")

Modes:
"r" = read
"w" = write
"a" = append                             #only adds to the end
"r+" = read + write                      #overwrites at beginning

Reading Files:
f.read()                                 #default - reads the whole file

Change Position of Cursor in File:
file.seek(position)

Read a line:
file.readline()

Read all lines as a List:
file.readlines()

Closing File:
file.closed                              #Returns True/False
file.close()

Using Better Code for the same:         #Automatically closes the file
with open('file.txt') as f:
    data = f.read()

Writing to Files:                       #Original Contents are overwritten, creates a new file if doesnt exist
with open('file.txt', "w") as f:
    f.write("Some shit!\n")
    f.write("Some more shit!\n")
