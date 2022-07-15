# Day 0: Hello, World.
inputString = raw_input() # get a line of input from stdin and save it to our variable

# Your first line of output goes here
print 'Hello, World.'

# Write the second line of output
print(inputString)

# Day 1: Data Types
i = 4
d = 4.0
s = 'HackerRank '

# Declare second integer, double, and String variables.
i = 4
d = 4.0
s = 'HackerRank '

# Read and save an integer, double, and String to your variables.
i2 = int(input())
d2 = float(input())
s2 = str(input())

# Print the sum of both integer variables on a new line.
print(i+i2)

# Print the sum of the double variables on a new line.
print(d+d2)

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(str(s)+str(s2))

# Day 2: Operators
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solve' function below.
#
# The function accepts following parameters:
#  1. DOUBLE meal_cost
#  2. INTEGER tip_percent
#  3. INTEGER tax_percent
#

def solve(meal_cost, tip_percent, tax_percent):
    print(round(meal_cost+(meal_cost*tip_percent+meal_cost*tax_percent)/100))

if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)

# Day 3: Intro to Conditional Statements
n = int(input().strip())

if (n%2) == 0:
    if (n > 20) or (n in range(2,6)):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
else:
    print("Weird") 