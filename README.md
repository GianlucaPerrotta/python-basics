# Hello world and comments in Python

## Python basic data types

In this exercise, we will focus on the use of the ```print()``` function, including printing basic data types, and the use of ```type()``` function, including getting information about class type of argument(object) passed as a parameter of this function.   
We will also focus on the use of ```isinstance()``` function, including checking if first argument of this function is an object of the given class (second argument of function).  
And finally we will focus on different types of comments available in Python including:

- Block comments 
- Inline comments
- Documentation strings

## 

## Usage

The ```print()``` function prints the specified message to the screen, or other standard output device.  
Syntax from [documentation](https://docs.python.org/3/library/functions.html#print): 
```bash
print(object or objects, sep=separator, end=end, file=file, flush=flush) 
```

First argument is required, others are optional. For example separator specifies how to separate the objects, if there is more than one, e.g.:
```bash
print("Hello", "world", sep=" - ")
```
Default separator is ' '

The ```type()``` function returns the [class type](https://www.w3schools.com/python/ref_func_type.asp) of the specified object. We can use it to get information about class type of given object. For example to get to know what type is 'Hello' we can write: 
```bash
type('Hello')
```

The ```isinstance()``` function returns True (this is a Boolean data type, which will be explored in this exercise)  if type of the first argument (object) is the same as the name of the given class (second argument).  
 For example to get to know if 123 is an integer type we can write: 
```bash
isinstance(123, int)
```
Hint: You can use one function (e.g. ```type()```) inside another function, e.g. ```print()```.
## 

## Tasks

### 

### Task 1 - printing single object

Your task is to print values of primitive data types, one type in one line. Use following types: integer, float, complex, string, boolean

- Your result could look like this:

```bash
234
43.12
(3+2j)
Hello
True
```

### 

### Task 2 - printing type of given value

Your task is to print two objects with separator for the same primitive types as in task 1.   
The first object is a value of given type, the second object is a type of value.  
The separator is a string " is type of ".

- Your result could look like this:

```bash
123 is type of <class 'int'>
43.23 is type of <class 'float'>
(4-1j) is type of <class 'complex'>
How are you? is type of<class 'str'>
True is type of <class 'bool'>
```

### 

### Task 3 - checking type of value

Your task is to check if given value is the instance of given class type using ```isinstance()``` function.  
The first argument of this function should be value, for example `city` and the second argument should be class type, for example `int`.   
Print at least one result for every primitive data type ('int', 'float', 'bool', 'complex', and 'str'). 


- Your result should look like this:

```bash
True
False
True
True
False
```
- Hint: if you print directly to terminal, you don't need to use `print()` function.  
But when you code is being run from file (with extension `.py`) then you should use `print()` function in the form: `print(another function to check instance of given value)`.

### 

### Task 4 - checking type of value (version 2)

Your task is a slightly modification of task 3. Instead  printing `True` or `False` modify your code to get readable information about the type of your value. 

- Your result should look like this:

```bash
Is 123  an instance of int?:  True
Is 43.23  an instance of bool?: False
Is (4-1j)  an instance of complex?: True
Is True  an instance of bool?: True
Is 'How are you?'  an instance of float?: False
```

### 

### Task 5 - using comments in code

Use code from one of the earlier exercises and add [comments](https://www.python.org/dev/peps/pep-0008/#comments) to it.  
Read most popular [answer](https://stackoverflow.com/questions/7696924/is-there-a-way-to-create-multiline-comments-in-python) about multiline comments in Python.
Use  block comments, inline comments, and multiline comments to your code. 
> Comments that contradict the code are worse than no comments. Always make a priority of keeping the comments up-to-date when the code changes!

- Your result could look like this:

```python
# This is my first comment
# Block comments are indented to the same level as that code

print("Hello")
print("Line with inline code!")  # remember about spacing!

print(type(123.45))  # getting type of number

"""
You can use triple-quoted strings. When they're not a docstring (the first thing in a class/function/module), they are ignored.
Read aforementioned answer from Stack Overflow!
"""

```

### 

