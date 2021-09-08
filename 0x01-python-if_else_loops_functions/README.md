# 0x01. Python - if/else, loops, functions

## Resource

- [More Control Flow Tools](https://docs.python.org/3.4/tutorial/controlflow.html)
- [Python IndentationError](https://youtu.be/1QXOd2ZQs-Q)

## Tasks

0. [Positive anything is better than negative nothing](0-positive_or_negative.py) : This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print whether the number stored in the variable `number` is positive or negative.
	- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/0-positive_or_negative_py)
	- The variable `number` will store a different value every time you will run this program.
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code.
	- The output of the program should be:
		- The number, followed by
			- if the number is greater than 0: `is positive`
			- if the number is 0: `is zero`
			- if the number is less than 0; `is negative`
		- followed by a new line.
1. [The last digit](1-last_digit.py) : This program will assign a random signed number to the variable `number` each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable `number`.
	- You can find the source code [here](https://github.com/holbertonschool/0x01.py/blob/master/1-last_digit_py)
	- The variable `number` will store a different value every time you will run this program.
	- You don’t have to understand what `import`, `random. randint` do. Please do not touch this code. This line should not change: `number = random.randint(-10000,10000)`
	- The output of the program should be:
		- The string `Last digit of`, followed by
		- the number, followed by
		- the string `is`, followed by the last digit of `number`, followed by
			- if the last digit is greater than 5: the string `and is greater than 5`
			- if the last digit is 0: the string `and is 0`
			- if the last digit is less than 6 and not 0: the string `and is less than 6 and not 0`
		- followed by a new line.
2. [I sometimes suffer from insomnia. And when I can't fall asleep, I play what I call the alphabet game](2-print_alphabet.py) : Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
3. [When I was having that alphabet soup, I never thought that it would pay off](3-print_alphabt.py) : Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.
	- Print all the letters except `q` and `e`
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
4. [Hexadecimal printing](4-print_hexa.py) : Write a program that prints all numbers from `0` to `98` in decimal and in hexadecimal (as in the following example)
	- Print all the letters except `q` and `e`
	- You can only use one `print` function with string format
	- You can only use one loop in your code
	- You are not allowed to store characters in a variable
	- You are not allowed to import any module
