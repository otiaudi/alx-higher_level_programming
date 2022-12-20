# 0x05. Python - Exceptions
# Learning Objectives
# General
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

# Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc

# Task 0:
- Write a function that prints x elements of a list.

- Prototype: def safe_print_list(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- x represents the number of elements to print
- x can be bigger than the length of my_list
- Returns the real number of elements printed
- You have to use try: / except:
- You are not allowed to import any module
- You are not allowed to use len()

# Task 1:
- Write a function that prints an integer with "{:d}".format().

- Prototype: def safe_print_integer(value):

# Task 2:
- Write a function that prints the first x elements of a list and only integers.

- Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)

# Task 3:
- Write a function that divides 2 integers and prints the result.

- Prototype: def safe_print_division(a, b)

# Task 4:
- Write a function that divides element by element 2 lists.

- Prototype: def list_division(my_list_1, my_list_2, list_length):

# Task 5:
- Write a function that raises a type exception.

- Prototype: def raise_exception():
- You are not allowed to import any module

# Task 6:

- Write a function that raises a name exception with a message.

- Prototype: def raise_exception_msg(message=""):
- You are not allowed to import any module

