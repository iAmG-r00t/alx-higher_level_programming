![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

# Zen (Python) 

>Not sure if C has taught me to think like a programmer or python is just really easy.

<details>
<summary>The Zen of Python, by Tim Peters</summary>
<br>
Beautiful is better than ugly.<br>
Explicit is better than implicit.<br>
Simple is better than complex.<br>
Complex is better than complicated.<br>
Flat is better than nested.<br>
Sparse is better than dense.<br>
Readability counts.<br>
Special cases aren't special enough to break the rules.<br>
Although practicality beats purity.<br>
Errors should never pass silently.<br>
Unless explicitly silenced.<br>
In the face of ambiguity, refuse the temptation to guess.<br>
There should be one-- and preferably only one --obvious way to do it.<br>
Although that way may not be obvious at first unless you're Dutch.<br>
Now is better than never.<br>
Although never is often better than *right* now.<br>
If the implementation is hard to explain, it's a bad idea.<br>
If the implementation is easy to explain, it may be a good idea.<br>
Namespaces are one honking great idea -- let's do more of those!

</details>

>I thought I had escaped [betty](https://github.com/holbertonschool/Betty), but here we have [PEP8](https://www.python.org/dev/peps/pep-0008/)

<details>
<summary> Install Pip3 and Pep8</summary>

- Pycodestyle is now the new standard of Python style code, but at ALX we will use PEP8, version 1.7.\* Don’t worry, pycodestyle is based on pep8.

- The requirement is to use ubuntu 14.04 and old fellah, faced some issue using it be warned you will face some errors.

<pre>$ sudo apt-get install python3-pip<br>$ sudo apt-get install python3-pep8<br>$ sudo pip3 install -Iv pep8==1.7.0</pre>

- Confirm you have the right version.

<pre>$ pep8 --version<br>1.7.0<br>$</pre>

- How to fix the below error:

<pre>FutureWarning: Possible nested set at position 1<br>EXTRANEOUS\_WHITESPACE\_REGEX = re.compile(r'[[({] | []}),;:]')</pre>

- Comment out the statement:
<pre>EXTRANEOUS\_WHITESPACE\_REGEX = re.compile(r'[[({] | []}),;:]')</pre>

- And below that line add this line:
<pre>EXTRANEOUS_WHITESPACE_REGEX = re.compile(r'[\[({] | [\]}),;:]')</pre>

</details>

## About

- This repository consists of all the .Subject projects done with [ALX Africa](https://www.alxafrica.com/) Full stack Software Engineering course in partnership with [Holberton School](https://www.holbertonschool.com/) by [th3\_gr00t](https://th3-gr00t.tk/).


## Resource

- [The Python Tutorial](https://docs.python.org/3/tutorial/index.html)
- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt)
- [PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [The Python Handbook](https://www.freecodecamp.org/news/the-python-handbook/)

---

- [0x00](./0x00-python-hello_world) : Hello, World.
- [0x01](./0x01-python-if_else_loops_functions) : if/else, loops, functions.
