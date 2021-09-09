# 0x02. Python - import & modules

## Resource

- [Modules](https://docs.python.org/3.4/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3.4/tutorial/stdlib.html#command-line-arguments)

## Tasks

0. [Import a simple function from a simple file](0-add.py) : Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`
	- You have to assign:
		- the value `1` to a variable called `a`
		- the value `2` to a variable called `b`
		- and use those two variables as arguments when calling the functions `add` and `print`
	- `a` and `b` must be defined in 2 different lines: `a = 1` and another `b = 2`
	- Your program should print: `<a value> + <b value> = <add(a, b) value>` followed with a new line
	- You can only use the word `add_0` once in your code
	- You are not allowed to use `*` for importing or `__import__`
	- Your code should not be executed when imported - by using `__import__`, like the example below.
1. [My first toolbox!](1-calculation.py) : Write a program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result.
	- Do not use the function `print` (with string format to display integers) more than 4 times
	- You have to define:
		- the value `10` to a variable `a`
		- the value `5` to a variable `b`
		- and use those two variables only, as arguments when calling functions (including `print`)
	- `a` and `b` must be defined in 2 different lines: `a = 10` and another `b = 5`
	- Your program should call each of the imported functions. See example below for format
	- the word `calculator_1` should be used only once in your file
	- You are not allowed to use `*` for importing or `__import__`
	- Your code should not be executed when imported
