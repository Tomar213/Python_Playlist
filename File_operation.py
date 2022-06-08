#File IO Basics 
'''
"r" - open file for reading only(read mode)    -default
"w" - to write in a file
"x" - create file but fail if the file with the same name already exist
"a" - add the given conten of write(".....") funtion in existing file
"b" - to read the file in  Binary form
"t" - text mode                              - default mode
"r+" - to read and write  
'''
#Read content from a file
f= open("karan.txt","r")   #opens file 
# content = f.read()             # read the opened file
# print(content)
print(f.readline())                 #read lines and print as it is
print(f.tell())            #this will tell the position of pointer 
f.seek(25)                            #this will give the desired position to the pointer 
print(f.tell())
print(f.readline())
# print(f.readlines())                    #make list of lines 
f.close()


#create new file and write in it
f= open("karan.txt ","x")            #alse we can open the file as -  with open("karan.txt") as f    
f.write(" its a new file created by write function ")
f.close()

#add content to exiestin file
f= open("karan.txt ","a")              #append the content in karan.txt
f.write(" stareted the seires of file opening its a new file created by write function ")
f.close()

#read and write both
f= open("rory.txt","r+")
print(f.read())
f.write("\n WELCOME  OKAY ...........")
f.close()

f= open("karan.txt")
print(f.readlines())