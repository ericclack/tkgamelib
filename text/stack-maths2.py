# Copyright 2019, Eric Clack, eric@bn7.net
# This program is distributed under the terms of the GNU General Public License

"""Evaluate simple mathematical expressions using a stack,
by turning them from the usual infix notation,
e.g. ( 2 * 3 ) + 1, into postfix, e.g. 7 5 9 * +

We use BODMAS for infix so that * happens before +
"""

def to_postfix(infix):
    output = []
    stack = [] # For operators
    
    for m in infix.split(" "):
        if m.isdigit():
            output.append(m)
        elif m == '(':
            push(stack, m)
        elif m in ['/', '*']:
            push(stack, m)
        elif m in ['+', '-']:
            # Divide and Mult take precedent
            while peek(stack) in ['/', '*']:
                output.append(pop(stack))
            push(stack, m)
        elif m == ')':
            while True:
                print(output, stack)
                o = pop(stack)
                if o == '(':
                    break
                output.append(o)

    while stack:
        output.append(pop(stack))

    return " ".join(output)

def postfix_calc(postfix):
    stack = []
    for m in postfix.split(" "):
        if m.isdigit():
            push(stack, int(m))
        elif m in ['+', '*', '-', '/']:
            d2 = pop(stack)
            d1 = pop(stack)
            if m == '+':
                push(stack, d1+d2)
            elif m == '*':
                push(stack, d1*d2)
            elif m == '-':
                push(stack, d1-d2)
            elif m == '/':
                push(stack, d1/d2)

    return pop(stack)

def push(s, e):
    s.append(e)

def pop(s):
    e = s[-1]
    del(s[-1])
    return e

def peek(s):
    if s:
        return s[-1]


print("Enter some maths separated by spaces, e.g. 1 + 2 * 3")

while True:
    maths = input("> ")
    postfix = to_postfix(maths)
    print(postfix)
    print("Result:", postfix_calc(postfix))
    
