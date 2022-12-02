#0x02. Python - import & modules
##Resources
Read or watch:

Modules
Command line arguments
Pycodestyle – Style Guide for Python Code
man or help:

python3
##Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

##General
. Why Python programming is awesome
. How to import functions from another file
. How to use imported functions
. How to create a module
. How to use the built-in function dir()
. How to prevent code in your script from being executed when imported
. How to use command line arguments with your Python programs

# Task 0:
. Write a program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3

#task 1:
. Write a program that imports functions from the file calculator_1.py, does some Maths, and prints the result.

# task 2:
Write a program that prints the number of and the list of its arguments.

The output should be:
Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by
: (or . if no arguments were passed) followed by
a new line, followed by (if at least one argument),
one line per argument:
the position of the argument (starting at 1) followed by :, followed by the argument value and a new line
Your code should not be executed when imported
The number of elements of argv can be retrieved by using: len(argv)
You do not have to fully understand lists yet, but imagine that argv can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.

# Task 3:
Write a program that prints the result of the addition of all arguments

The output should be the result of the addition of all arguments, followed by a new line
You can cast arguments into integers by using int() (you can assume that all arguments can be casted into integers)
Your code should not be executed when imported


# Task 4:
Write a program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).

You should print one name per line, in alpha order
You should print only names that do not start with __
Your code should not be executed when imported
Make sure you are running your code in Python3.8.x (hidden_4.pyc has been compiled with this version)

# Task 5:
Write a program that imports the variable a from the file variable_load_5.py and prints its value.

You are not allowed to use * for importing or __import__
Your code should not be executed when imported

# Task 5:
Write a program that imports all functions from the file calculator_1.py and handles basic operations.

Usage: ./100-my_calculator.py a operator b
If the number of arguments is not 3, your program has to:
print Usage: ./100-my_calculator.py <a> <operator> <b> followed with a new line
exit with the value 1
operator can be:
+ for addition
- for subtraction
* for multiplication
/ for division
If the operator is not one of the above:
print Unknown operator. Available operators: +, -, * and / followed with a new line
exit with the value 1
You can cast a and b into integers by using int() (you can assume that all arguments will be castable into integers)
The result should be printed like this: <a> <operator> <b> = <result>, followed by a new line
You are not allowed to use * for importing or __import__
Your code should not be executed when imported
