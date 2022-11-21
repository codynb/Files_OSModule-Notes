#example1
#Tying in Mac terminal


#NOTE: all .txt files used are in the SAME FOLDER as example1!
fin = open("myFile.txt")

fin1 = fin.readline()
print(fin1)
#this printed the first line of myFile.txt

fin2 = fin.readline()
print(fin2)

fin3 = fin.readline()
print(fin3)


fin = open("myFile.txt")

for line in fin:
    print(line)
#This prints all lines


#New for silly_notes.txt
fin = open("silly_notes.txt")

fin1 = fin.readline()
print(fin1)
print(len(fin1))
word = fin1.strip()
print(word)
len(word)
print(len(word))


#New for note1, calling this text file
fin = open("note1.txt")

for line in fin:
    print(line)
#This prints the information from note1.txt

#Writing a file
fin1 = open("note1.txt","w")
#this line removed all the information from note1!


#Creating new files
fout = open('note3.txt','w')

fout1 = open("example2.py",'w')
#These two functions created 2 new files in myFolder!

#Adding data into the new files
fout = open("myStory.txt", 'w')
first_line = "Once upon a time...\n"

fout.write(first_line)

#Adding lines of code into the .py
fout = open('example2.py','w')
line1 = "for i in range(4)"
fout.write(line1)


fout = open("new_story.txt",'w')
line1 = 'This is line1'
fout.write(line1)

#Wringing in example2
fout = open('example2.py','w')
line1 = "for i in range(4)"
fout.write(line1)

line2 = "   print(i)"
fout.write(line2)
fout.close()

#Format operator: %

%d #second operand should be formatted as an integer
%f #second operand should be formatted as a float
%first.secondf #the second operand should be formatted a float
    # first fives us the number of places for the entire number
    # second gives us the number of decimal places

#File names and paths
# files are organized into directories, also called folders,
# every running program has a "current directory"
import os
cwd = os.getcwd()
print(cwd)
# cwd stands for "current working directory"
# this prints the address of the current directory:
    # in terminal: /Users/codybrown/Desktop/myFolder
    # in IDLE: /Users/codybrown/Documents

#The name of the file is the relative path for the document, the whole thing
#is the absolute path
import os
os.path.abspath("note2.txt")
#this prints:
    #in IDLE: '/Users/codybrown/Documents/note2.txt'

#About the os module
#What exists?
os.mkdir()
    # this creates a directory named path with numeric module
    # mode
os.listdr()
    # returns a list of names of the entries in the directory given
    # by a path (arbitrary order)
os.rename()
    # renames a file or directory src to dst, if dst exists
    # will fail
    # AKA we a renaming the path and changing where it is
    # located

#Changing the directory
import os
os.chdir(r"/Users/codybrown/Desktop/myFolder")
cwd = os.getcwd()
print(cwd)
#this prints '/Users/codybrown/Documents'
os.listdir()
#this prints ['example1.py', '.DS_Store', 'note1.txt', 'note2.txt',
#'note3.txt', 'silly_notes.txt', 'myFile.txt', 'myStory.txt', 'example2.py']
os.mkdir("Documents1")
os.listdir()
# this prints['example1.py', 'Documents1', '.DS_Store', 'note1.txt',
#'note2.txt', 'note3.txt', 'silly_notes.txt', 'myFile.txt', 'myStory.txt', 'example2.py']
os.rename("myStory.txt","Documents1/myStory.txt")
#this moves myStory.txt into the Documents1 folder within
#myFolder
