# 0x00. Python - Hello, World

## Resource

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html) (*only the first three chapters below*)
	- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html)
	- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html)
	- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html) (*Read up until “3.1.2. Strings” included*)
- [How to use string formatters in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3)

## Tasks

0. [Run Python file](0-run) : Write a Shell script that runs a Python script.
	- The Python file name will be saved in the environment variable `$PYFILE`

	```sh
	guillaume@ubuntu:~/py/0x00$ cat main.py 
	#!/usr/bin/python3
	print("Holberton School")

	guillaume@ubuntu:~/py/0x00$ export PYFILE=main.py
	```
1. [Run inline](1-run_inline) : Write a Shell script that runs Python code.
	- The Python code will be saved in the environment variable `$PYCODE`

	```sh
	guillaume@ubuntu:~/py/0x00$ export PYCODE='print("Holberton School: {}".format(88+10))'
	```
2. [Hello, print](2-print.py) : Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.
	- Use the function `print`
3. [Print integer](3-print_number.py) : Complete the source code in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/3-print_number.py)
	- The output of the script should be:
		- the number, followed by `Battery street`,
		- followed by a new line.
	- You are not allowed to cast the variable `number` into a string.
	- Your code must be 3 lines long
	- You have to use the new print numbers [tips](https://pyformat.info/#number) (with `.format(...)`)
	> C is strongly typed… not in Python! The variable `number`  can be assigned to a string, a float, a bool etc… Forcing the type during a string format (`"...".format(...)`) is a way to control the type of a variable
4. [Print float](4-print_float.py) : Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/4-print_float.py)
	- The output of the program should be:
		- `Float:`, followed by the float with only two digits.
		- Followed by a new line.
	- You are not allowed to cast the variable `number` into a string.
	- You have to use the new print numbers [tips](https://pyformat.info/#number) (with `.format(...)`)
5. [Print string](5-print_string.py) : Complete the source code in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/5-print_string.py)
	- The output of the program should be:
		- 3 times the value of `str`
		- followed by a new line
		- followed by the 9 first characters of `str`
		- followed by a new line
	- You are not allowed to use any loops or conditional statement
	- Your program should be maximum 5 lines long
6. [Play with strings](6-concat.py) : Complete this source code to print `Welcome to Holberton School!`
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/6-concat.py)
	- You are not allowed to use any loops or conditional statements.
	- You have to use the variables	`str1` and `str2` in your new line of code.
	- Your program should be exactly 5 lines long
7. [Copy - Cut - Paste](7-edges.py) : Complete this source code.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/7-edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 8 lines long
	- `word_first_3` should contain the first 3 letters of the variable `word`
	- `word_last_2` should contain the last 2 letters of the variable `word`
	- `middle_word` should contain the value of the variable `word` without the first and last letters
8. [Create a new sentence](8-concat_edges.py) : Complete this source code to print `object-oriented programming with Python`, followed by a new line.
	- You can find the source code [here](https://github.com/holbertonschool/0x00.py/blob/master/8-concat_edges.py)
	- You are not allowed to use any loops or conditional statements
	- Your program should be exactly 5 lines long
	- You are not allowed to create new variables
	- You are not allowed to use string literals
9. [Easter Egg](9-easter_egg.py) : Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.
	- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)
10 [Linked list cycle](10-check_cycle.c) Technical interview preparation:
	- You are not allowed to google anything
	- Whiteboard first
	- This task and all future technical interview prep tasks will include checks for the efficiency of your solution, i.e. is your solution’s runtime fast enough, does your solution require extra memory usage / mallocs, etc.
	- Write a function in C that checks if a singly linked list has a cycle in it.
		- Prototype: `int check_cycle(listint_t *list);`
		- Return: `0` if there is no cycle, `1` if there is a cycle
	- Requirements:
		- Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
	- Compile the code this way: `gcc -Wall -Werror -Wextra -pedantic 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle`
	- Solving a problem is already a big win! but finding the best and optimal way to solve it, it’s way better! Think about the most optimal / fastest way to do it.
