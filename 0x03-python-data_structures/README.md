# 0x03. Python - Data Structures: Lists, Tuples

#General
. Why Python programming is awesome
. What are lists and how to use them
. What are the differences and similarities between strings and lists
. What are the most common methods of lists and how to use them
. How to use lists as stacks and queues
. What are list comprehensions and how to use them
. What are tuples and how to use them
. When to use tuples versus lists
. What is a sequence
. What is tuple packing
. What is sequence unpacking
. What is the del statement and how to use it	;

# Task 0
. Write a function that prints all integers of a list.

# Task 1
Write a function that retrieves an element from a list like in C.

# Task2
Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except

#TASK 3
Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

#TASK 4:
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except


#TASK 5
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()

