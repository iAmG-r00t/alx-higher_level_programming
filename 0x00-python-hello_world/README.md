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
