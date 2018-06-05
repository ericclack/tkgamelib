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

> **Hint:** input only works with strings. If you double a string it does something strange:

	Give me a number:
	>>> 5
	When doubled it is 55

> To double it properly you will need to convert the string to a number:
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
The code for 4.4 and 4.5 will only work with whole numbers. But if you replace the `int` with a `float` in the input routine it will support decimals. Make that change and see if it works correctly.

## 5 Control: the 'If' statement
The if statement is asking the computer to check if something is true or false and then it does one thing or another.

### 5.1 Writing an if statement
Try entering the following program:
```python
sunny = input("Is it sunny (y/n)?")
if sunny == 'y':
	print("lets go out and play")
else:
	print("lets stay in and read a book")
print("end")
```
This is quite complex and there is a lot of things that might go wrong. Watch out for:
* Quotation marks and brackets
* Colons at the end of certain lines
* The print’s must be set in by the SAME NUMBER of spaces (or use a tab), Python is VERY FUSSY on this
* On the `if` line there is two equals signs, but the `input` has only one
 * the `==` is a comparison

### 5.2 Writing your own if statement
Write a program (ch5_2.py) which asks

	Do you understand programming?

If they say yes, print

	Thats good

Otherwise, print

	Thats ok, you will get better

### 5.3 if with numbers
You can also use the `if` statement with numbers, type this in and test it(ch5_3.py), try many different numbers:

```Python
num = int(input("give me a number"))
if num > 90:
	print("thats a big number")
if num < 10:
	print("thats a small number")
```
Explain what it does. In particular test with 9,10,11 and 89,90,91

	Hint: < means less than, > means greater than

### Challenge: age program
Write a program which asks the user what age they are and print a message accordingly:

Age			| Message
------- | -------
0..5		| Baby!
6..15		| You are young
16..25	| Are you still at school?
26..50	| Are you a parent?
51..65	| Getting quite old
66+			| You are a grandparent

To do this, you will need to use the `if`, `elif` and `else` commands. Look them up online on how to use them.

## 6 Control: For statement
The `for` statement, is often used with the `range` command. Its asking the computer to do something several times, like count a number.

Eg: This will code execute the print command 5 times, with the value n set to 0,1,2,3,4 (5 times total)
```Python
for n in range(5):
	print(n)
```

### 6.1 your first loop
Write a program which prints the numbers 0 to 10 (including the ten)

### 6.2 experimenting with the range command
The `range` command can be used with 1, 2 or 3 numbers between the brackets. The python documentation (you might want to look this up), call these numbers `start`, `stop` and `step`.

```Python
# stop only
for n in range(10):
	print(n)
# start and stop
for n in range(3,7):
	print(n)
# start, stop and step
for n in range(5,10,2):
	print(n)
```
Spend some time experimenting with the three types of for loops. Then write your own versions:

* Print out all the numbers between 10 to 20 (including both 10 and 20)
* Print out the odd numbers from 1 to 10
* Print out the even numbers from 1 to 10
* Print out a countdown from 5 to 1

>	Hint: Think about what you want the start number is, and what the stop is and you might want a negative number in the step

### 6.3 seven times table
Write a program which can print out the 7 times table:

	1 x 7 = 7
	2 x 7 = 14
	...
	10 x 7 = 70

You can use a loop to count 1..10 and then just have a single print command to print all the information for a single line

### Challenge: any times table
Once you have this working, change the program so that it asks what times table you want, so you could try the 3, 8, 13, or even the 101 times table.

Eg.

	Pick a number:
	>>> 9
	1 x 9 = 9
	2 x 9 = 18
	...
	10 x 9 = 90

### 6.4 Summing numbers
For loops are often used in maths, when we want to count, lets use this now
Build a program which adds up the numbers from 1 to 10 and the prints the total.
The answer should be 55

>	Hint: To do this you will need two variables, number which goes 1..10 and
> total which is used to store the total. Inside the loop you will need to add
> the number to the total.
>
> `total = total + number`
>
> Or `total += number`

### Challenge: Summing numbers 2.0
Modify this program so that it asks you how many numbers to add up. Then it will add those numbers. Once you think its working, test it with these numbers.

*	1 to 3 is 6
*	1 to 10 is 55
*	1 to 100 is 5050

## 7 Control: While statement
The `while` statement, works a bit like the `for` statement. In a `for` loop it is for a fixed number of times, a `while` keep going until a condition is met.

### 7.1 is it bed time?
Type in the following program and test it?
```python
bed_time='n'
while bed_time != 'y':
	print("lets play")
	bed_time = input("is it bedtime?")
print("ok lets sleep")
```

What is the most/least number of times you can play?

Notice that you need to set the variable `bed_time` before the `while`, if you don’t the will be an error.

### 7.2 Computer security
Write a program which performs a password check. Here is what it should look like:

	Halt! Who goes there?
	What is the password?
	>>> I don’t know
	Wrong!
	What is the password?
	>>> python
	Pass, friend

> Hint: You will need two variables, the password and the guess. You will also need a while loop and an if check.

### 7.3 Computer security 2.0
Once you have that working, add some extra code at the beginning of the program to get the new password.

	Hi Boss, what it the new password?
	>>> computers
	Ok Boss, the new password is computers
	********************************
	Halt! Who goes there?

And so on
