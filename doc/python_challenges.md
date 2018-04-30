# CoderDojo Python Challenges

## Introduction
This is a collection of tasks and challenges for you to try. Some are easy, many will be challenging.

Some will list out what you need to do.

Some will ask you to enter certain code. They will look like this:

```python
# this is the code you will need to enter
print("hello world")
```
Some will give you example input and output:

	This is the output
	>>> this is input
	This is more output

Look out for the topics marked challenge. These are extra hard or just puzzling. Figure out what the answer is then find a helper and explain to them the answer.

## 1. Printing

### 1.1 Hello world
Create a python file ex1_1.py and enter the following code. What does it do?
```python
# this is a comment
# you don't need these
# python will ignore them
# but they can be helpful for making notes

print("hello world")
```
> **Hint:** Be prepared, Python, like all computer programs is FUSSY: case matters, punctuation matters, it will not guess, it will just complain and not work. Learn to be careful, learn to read the error messages and know what is wrong

### 1.2 My program
Make a copy of the previous code and save it as ex1_2.py

Modify the code to give the following output:

	This program is written by <your name>

### 1.3 Double up
Make another copy (ex1_3.py) and get it to print the following:

	This program is written by <your name>
	I am learning Python

> **Hint:** You will need two print statements

## 2 Maths
For each of these you will need to create a new file. The instructions will not list it, but you will need to do it.

### 2.1 The Plus (+)
Enter the following code:
```Python
print("lets do some maths")
print(1+1)
```

### 2.2 And other operators
Add to 2.1 to include:
* print with a -
* print with a *
* print with a /

### 2.3 What about fractions?
Add to 2.2 a print command to print a fraction (2/3, 3/4 or similar).

Does it work?

We will be looking at it again at the end of this section

### 2.4 Advanced print use
Write the following code:
```Python
print(1+1, 2+2, 3+3)
print("I can do maths", 3*5)
print("First string","second string")
```

What does it print out? Why?

### Challenge 1: Using "Quotes"
Make a program ch2_1.py and put in the following code

```python
print("3+3",3+3)
print('2*2',2*2)
```

What does this program do? Why? What is the difference between 'single quotes' and "double quotes"?

### Challenge 2: Divide again
Write a program to print the following
* 7/3, 7//3, 7%3

What is the difference between these 3 types of divide?

> **Hint 1:** try 8/3, 8//3, 8%3
>
> **Hint 2:** What is a remainder? Look up the word 'modulo operator' online

## 3 Variables
For this section (and onwards), there is going to be a lot of experimentation. Type in the code, make it work and then figure out what its doing.

If you want to know more on this, type `python variable` into a search engine or look that up in your book/guide.

### 3.1 Using variables
Type in the following program:
```python
a=10
b=20
c=a+b
print(a,b,c)
```

What does it print? What do these represent?

> **Hint:** imagine a, b and c are boxes which contain numbers

### 3.2 Reusing variables
Now try the following program:
```python
a=10
print("a is",a)
a=20
print("a is",a)
a=a+10
print("a is",a)
```

What is going on here?

### 3.3 Variables for strings
You can also put strings into variables. Type this in and test it:
```python
word="cat"
print("word is",word)
```

### Challenge: Variable names
Instead of using single letters we can use longer, more descriptive names for variables, but not all words.

Type in this program, then comment out (`#`) the invalid variable names.

Try to figure out what the rules are for variable names.
```python
test=10
print(test)
test2=20
print(test2)
ANOTHER=30
print(ANOTHER)
print(another)
aFunnyVariable=40
print(aFunnyVariable)
another-variable=50
print(another-variable)
one more=60
print(one more)
one_last_one=70
print(one_last_one)
```

## 4 Input
### 4.1 Basic Input
It’s time we got the computer to listen to us, type in the following program:
```python
a=input("type something")
print(a)
```
Test this then move on to the next question

### 4.2 Python Greeter
Write a program to ask a user their name and then print a greeting to them. It should look like this:

	What is your name?
	>>> fred
	Hello fred

### 4.3 Python Greeter 2.0
Improve upon the previous program to add a request for the persons age, and then display this too.

	What is your name?
	>>> fred
	How old are you?
	>>> 15
	fred is 15

### 4.4 Maths doubler
Write a program which asks the user for a number, multiplies it by two and then prints it out. It will look like this:

	Give me a number:
	>>> 5
	When doubled it is 10

> **Hint:** input only works with strings, to double it you will need to convert the string to a number:
>
> `num = int(input('type something'))`

### 4.5 Maths test
Write a program which asks the user for two numbers, then adds, subtracts, multiplies, and divides them. It will look like this:

	Give me a number:
	>>> 8
	And another one:
	>>> 2
	8 + 2 = 10
	8 - 2 = 6
	8 * 2 = 16
	8 / 2 = 8

Thats a lot of code to write, so solve it bit at a time. Get both numbers in and print them both. Then replace the print with the proper maths, bit by bit.

### Challenge: Decimals
The code for 4.5 will only work with whole numbers. But if you replace the `int` with a `float` in the input routine it will support decimals. Make that change and see if it works correctly.
