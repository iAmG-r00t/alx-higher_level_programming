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
2. [How to make a script dynamic!](2-args.py) : Write a program that prints the number of and the list of its arguments.
	- The output should be:
		- Number of argument(s) followed by `argument` (if number is one) or `arguments` (otherwise), followed by
		- `:` (or `.` if no arguments were passed) followed by
		- a new line, followed by (if at least one argument),
		- one line per argument:
			- the position of the argument (starting at `1`) followed by `:`, followed by the argument value and a new line
	- Your code should not be executed when imported
	- The number of elements of `argv` can be retrieved by using: `len(argv)`
	- You do not have to fully understand lists yet, but imagine that `argv` can be used just like a C array: you can use an index to walk through it. There are other ways (which will be preferred for future project tasks), if you know them you can use them.
3. [Infinite addition](./3-infinite_add.py) : Write a program that prints the result of the addition of all arguments.
	- The output should be the result of the addition of all arguments, followed by a new line
	- You can cast arguments into integers by using `int()` (you can assume that all arguments can be casted into integers)
	- Your code should not be executed when imported
	- Last but not least, your program should also handle big numbers.
	
	```sh
	guillaume@ubuntu:~/0x02$ ./3-infinite_add.py 1111111111111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999990000000000000000000 11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334567788888899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
	11111111111111111111111111111111111111111111111111222222222222222222222222222333333333333333333334568900000011111111111111111111111111111111111111111111111111112222222222222222222222222222222222223435467866765443534434222222254444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555666666666666666666666666666666777777777777777777777777777777888888888888888888888888888888899999999999999999999999989999999999999999999
	guillaume@ubuntu:~/0x02$
	```
4. [Who are you?](4-hidden_discovery.py) : Write a program that prints all the names defined by the compiled module [hidden\_4.pyc](https://github.com/holbertonschool/0x02.py/raw/master/hidden_4.pyc) (please download it locally).
	- You should print one name per line, in alpha order
	- You should print only names that do not start with `__`
	- Your code should not be executed when imported
	- Make sure you are running your code in Python3.8.x (`hidden_4.pyc`  has been compiled with this version)

5. [Everything can be imported](5-variable_load.py) : Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
	- You are not allowed to use `*` for importing or `__import__`
	- Your code should not be executed when imported
