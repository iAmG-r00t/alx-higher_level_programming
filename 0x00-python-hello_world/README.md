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
