#Say "Hello, World!" With Python
if __name__ == '__main__':
    print "Hello, World!"

#Python If-Else
#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
    if (n%2) == 0:
        if (n > 20) or (n in range(2,6)):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
    else:
        print("Weird") 

#Arithmetic Operators
if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    
    #arithmetic
    print("{}\n{}\n{}").format(a+b, a-b, a*b)

#Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print("{}\n{}").format(a//b, a/b)
    
#Loops
if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i**2)

# Write a function
def is_leap(year):
    leap = False
    
    if year%4 == 0:
        leap = True
    
    return leap

year = int(raw_input())
print is_leap(year)