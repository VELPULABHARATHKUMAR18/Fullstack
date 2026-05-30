# write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of
# characters in the file.

# with open("file_1.txt","r") as f:
#     z=f.read()
#     print(f.tell())
#         or
#     print(len(z))


#  Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10
# characters


# with open("file_1.txt","r") as f:
#     line=f.readlines()
#     for i in line:
#         if len(i)>=10:
#             print(i)


#  Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints
# the complete file content


# with open("file_2.txt","w") as f:
#     f.write("bharath\n")
#     f.write("bharath\n")
#     f.write("kumar\n")
# with open("file_2.txt","a") as f:
#     f.write("velpula\n")
#     f.write("kumar\n")
#     # f.seek(0)
#     # print(f.tell())
#     print(f.read())


#  Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.

# with open("file_1.txt","r")as f:
#     print(f.read(10))
#     print(f.tell())
#     f.seek(0)
#     print(f.read())


#  Write a program using a context manager that opens a file in read mode, uses a
# loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(), uses seek() to move to
# a specific position, and continues reading from there.

