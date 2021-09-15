# 0x03. Python - Data Structures: Lists, Tuples 

## Resource

- [3.1.3. Lists](https://docs.python.org/3.4/tutorial/introduction.html#lists)
- [5. Data Structures](https://docs.python.org/3.4/tutorial/datastructures.html) (*until `5.3. Tuples and Sequences included`*)
- [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)

## Tasks

0. [Print a list of integers](0-print_list_integer.py) : Write a function that prints all integers of a list.
	- Prototype: `def print_list_integer(my_list=[]):`
	- Format: one integer per line.
	- You are not allowed to import any module
	- You can assume that the list only contains integers
	- You are not allowed to cast integers into strings
	- You have to use `str.format()` to print integers
1. [Secure access to an element in a list](1-element_at.py) : Write a function that retrieves an element from a list like in C.
	- Prototype: `def element_at(my_list, idx):`
	- If `idx` is negative, the function should return `None`
	- If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
	- You are not allowed to import any module
	- You are not allowed to use `try/except`
