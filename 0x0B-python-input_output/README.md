# 0x0B. Python - Input/Output
<html>
<head>
<body>
<a href="https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files ">Reading and Writing Files</a>

</br>
<a href="https://docs.python.org/3/tutorial/errors.html#predefined-clean-up-actions "> Predefined Clean-up Actions  </a>


</br>
<a href="https://histo.ucsf.edu/BMS270/diveintopython3-r802.pdf "> Dive Into Python 3: Chapter 11. Files </a>


</br>
<a href="https://docs.python.org/3/library/json.html "> JSON encoder and decoder </a>


</br>
<a href="https://www.youtube.com/watch?v=EukxMIsNeqU "> yutube link </a>


</br>
<a href="https://automatetheboringstuff.com/ "> Automate the Boring Stuff with Python </a>

</body>
</html>

# Learning Objectives

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

# Tasks
## Write a function that reads a text file (UTF8) and prints it to stdout:

- Prototype: def read_file(filename=""):
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

# Write a function that writes a string to a text file (UTF8) and returns the number of characters written:

- Prototype: def write_file(filename="", text=""):
- You must use the with statement
- You don’t need to manage file permission exceptions.
- Your function should create the file if doesn’t exist.
- Your function should overwrite the content of the file if it already exists.
- You are not allowed to import any module

# Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

- Prototype: def append_write(filename="", text=""):
- If the file doesn’t exist, it should be created
- You must use the with statement
- You don’t need to manage file permission or file doesn't exist exceptions.
- You are not allowed to import any module

# Write a function that returns the JSON representation of an object (string):

- Prototype: def to_json_string(my_obj):
- You don’t need to manage exceptions if the object can’t be serialized.

# Write a function that returns an object (Python data structure) represented by a JSON string:

- Prototype: def from_json_string(my_str):
- You don’t need to manage exceptions if the JSON string doesn’t represent an object.
