#file write basic way
""" 
fileptr = open("file.txt", "w")

fileptr.write('''Welcome to Python->
file i/o from the system!''')

if fileptr:
    print("File Opened Successfully!")

fileptr.close()
print("File Closed!") """


#file read with "with" statement
""" 
#file read with 'with' statement 
with open("file.txt",'r') as f:
    content = f.read()
    print("file opened and read")


print(content)

"""


#file write in 'a' mode
""" 
with open("file.txt", 'a') as f:

    f.write("Writing with the 'a' mode.")
  
"""   

#file read 
""" 
with open("file.txt", 'r') as f:

    content = f.read(20) #number of bytes to be read 

print(content)

"""

#read file through for loop
#print each line at each loop as 

""" 
fileptr = open("file.txt", 'r')

for i in fileptr:
    print(i)#i contains each line of the file

fileptr.close()
"""


""" 
#readline()
#readlines()

fileptr = open("file.txt", 'r')

#readline()
content = fileptr.readline()
content1 = fileptr.readline()

#readlines() #print as an array
#content2 = fileptr.readlines()

print(content)
print(content1)
#print(content2)
"""

#x-mode:create only
#a-mode:create and append
#w-mode:create and overwrite

""" 
#filepoiner position
#tell()
#seek()

fileptr = open("file.txt", 'r')

print("The filepointer (at the beginning) is at byte: ", fileptr.tell())

content = fileptr.read()
print(content)

print("The filepointer(before seek()) is at byte: ", fileptr.tell())
fileptr.seek(10)
print("The filepointer(after seek()) is at byte: ", fileptr.tell())
"""
#rename

import os

os.rename("newfile.txt", "file.txt")

fileptr = open("file.txt", 'r')

content = fileptr.read()
print("New files content: ",content)

fileptr.close()