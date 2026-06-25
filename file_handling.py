#----------- File handling
#1. File handling in python means reading from and writing to files/folder stored on
# disk using python.

#2. Your python code can open a file , pull out data of it , put data into it and 
# also close it properly.

#---------- What is file
# files are store of data and information on the specifi path of device.

# Types of file
# 1.Text file (.txt,.csv,.json)
# 2.Binary file (images,vedios,audio)

# Types of file path.
# 1.Absolute path : The complete path from the root of the filesystem.
# 2.Relative path : The path relative to where your current folder (current working dir)

# file mode
# 1. a : append , a+ : append and read
# 2. w : write , w+ : write and read
# 3. r : read  ,  r+ : read and write
# 4. x : strictly create file

# python file handling methods.
# 1.open(file_name,mode) : opens file 
# 2.close() : close file.
# 3.flush() : memory cleanup.

# 4.read() : file read.
# 5.readlines(): file read line by line.
# 6.write() : writes data in file only take string.
# 7.writelines() : write data in file of any data types.

# 8.tail(): cursor move
# 9.seek(): specific position set of cursor

# in-built modules
# os library
# shutil library
# subprocess libary
# random library
# string library

# -----------------------------------------------------
# 1.create a file in strict mode
# try:
#     file=open("demo.txt","x")
#     print("File Created")
# except Exception as e:
#     print("Error:",e)

# 2.write mode file creation
# file=open("new_demo.txt","w")
# file.write("This is file conten using file handling")
# print("file created in write mode..")

# import os
# print(os.getcwd())
# path=r"c:\Users\dev\OneDrive\Desktop"
# os.chdir(path)
# print(os.getcwd())

# file=open("data.py","w")
# file.write(f"print('File handling')")
# file.close()
# print(os.listdir())

# context manager.
# with open("demo.txt","a") as file:
#     file.write("this is new content of file")
#     file.write("this is updated content")
#     print("file written")

# server_list=['prod_server',"test_server","dev_server"]
# for i in server_list:
#     with open(f"{i}.txt","w") as file:
#         print(i," file created...")


# with open("dev_server.txt","w") as file:
#     file.write("This is content of dev server")
    

# with open("dev_server.txt","a") as file:
#     file.write("\n")
#     file.write("this is my content")

# extact all number from paragraph
para="""
Lorem Ipsum is simply dummy text of 
the printing and typesetting industry. 
Lorem Ipsum has been the industry's 
standard 234 dummy text ever since 1966, 
when designers at Letraset and James 
Mosley,999 the librarian at St Bride Printing Library
in London, took a 1914 Cicero translation and 
scrambled it to make dummy text for 
Letraset's Body Type sheets.
"""

count_digits=0
total_char=0
for i in para:
    if i in "0123456789":
        count_digits+=1
    else:
        total_char+=1
with open('stats.txt',"w") as file:
    file.write(f"Total Digits in file : {count_digits}")
    file.write("\n")
    file.write(f"Total chars in file : {total_char}")

