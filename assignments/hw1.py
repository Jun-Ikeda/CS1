"""
Student name: Jun Ikeda
Date: 2022/10/03

HW1
"""
# Exercise A: Course Policies
# A.1:
print("not allowed")
# A.2:
print("not allowed")
# A.3:
print("allowed")
# A.4:
print("not allowed")
# A.5:
print("not allowed")
# A.6:
print("not allowed")
# A.7:
print("not allowed")
# A.8:
print("not allowed")
# A.9:
print("not allowed")

# Exercise B.1: Expressions
# B.1.1:
# 8 - 5 --> 3
# B.1.2:
# 6 * 2.5 --> 15.0
# B.1.3:
# 51 / 2 --> 25.5
# B.1.4: 
# 51 / -2 --> -25.5
# B.1.5: 
# 51 % 2 --> 1
# B.1.6: 
# 51 % -2 --> -1
# B.1.7: 
# -51 % 2 --> 1
# B.1.8:
# 51 / -2.0 --> 25.5
# B.1.9: 
# 1 + 4 * 5 --> 21
# B.1.10:
# (1 + 4) * 5 --> 25

# Exercise B.2: Shortcut Expressions
# B.2.1:
# x = 120 --> 120
# B.2.2:
# x = x + 10 --> 130
# B.2.3:
# x += 20 --> 150
# B.2.4:
# x = x - 30 --> 120
# B.2.5:
# x -= 70 --> 50
# B.2.6:
# x *= 3 --> 150
# B.2.7:
# x /= 5 --> 30.0
# B.2.8:
# x %= 5 --> 0.0

# Exercise B.3: Evaluation walkthrough
# x = 3
# x += x - x --> 3
# Evaluate x - x which is 0. 
# Then the expression is x += 0.
# x = x + 0 which is x = 3. 
# So x is 3. 

# Exercise B.4: Complex numbers
# B.4.1:
# 1j + 2.4j --> 3.4j
# B.4.2:
# 4j * 4j --> (-16+0j)
# B.4.3:
# (1+2j) / (3+4j) --> (0.44+0.08j)
# B.4.4:
# (1+2j) * (1+2j) --> (-3+4j)
# B.4.5:
# 1+2j * 1+2j --> (1+4j)

# Exercise B.5: Functions on complex numbers
# B.5.1:
# cmath.sin(-1.0+2.0j) --> (-3.165778513216168+1.959601041421606j)
# B.5.2:
# cmath.log(-1.0+3.4j) --> (1.2652585805200263+1.856847768512215j)
# B.5.3:
# cmath.exp(-cmath.pi * 1.0j) --> (-1-1.2246467991473532e-16j)

# from math import * means import all the functions from math module. 
# So, if you import multiple libraries and they have some function with exactly the same name, then the function will be overwritten.
# import math means import the math module itself.
# Even if multiple libraries have the same function name, they will both be accessible.

# Exercise B.6: String expressions
# B.6.1:
# "foo" + 'bar' --> 'foobar'
# B.6.2:
# "foo" 'bar' --> 'foobar'
# B.6.3:
# a = 'foo'
# b = "bar"
# a + b --> 'foobar'
# B.6.4:
# a = 'foo'
# b = "bar"
# a b --> SyntaxError: invalid syntax
# B.6.5:
# month = "October"
# days = 31
# days + " days hath " + month --> TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Exercise B.7: Fun with quotes
# 'A\nB\nC' --> 'A\nB\nC'

# Exercise B.8: String generation
# s = '-'*70

# Exercise B.9: A string puzzle
# s = 'Line 1\nLine 2\nLine 3'

# Exercise B.10: String formatting
x = 9
y = 4.25
# B.10.1 
print('Lorem is {}.'.format(x))
# B.10.2 
print('Lorem is {} months old.'.format(x))
# B.10.3 
print('A puppuccino is ${}.'.format(y))
# B.10.4 
print('{0} * {1}'.format(y,x))
# B.10.5 
print('{0} * {1} is {2}.'.format(y,x,y*x))

# Exercise B.11: Terminal input
num = float(input("Enter a number: "))
print(num)

# Exercise B.12: Quadratic expressions
def quadratic(a, b, c, x):
    """
    Computes the value of the quadratic expression ax^2 + bx + c
    
    Arguments:
      `a` (float): coefficient of x^2
      `b` (float): coefficient of x
      `c` (float): constant
      `x` (float): value of x

    Returns:
      (float): the value of the quadratic expression
    """

    return a*x**2 + b*x + c
    # Or, return a*x*x + b*x + c

# Exercise B.13: DNA
def GC_content(dna):
    """
    Computes the single float proportion of G or C in a DNA sequence.
    
    Arguments:
      `dna` (string): DNA sequence
    
    Returns:
      (float): the proportion of G or C in the sequence
    """

    return (dna.count('G') + dna.count('C'))/len(dna)
