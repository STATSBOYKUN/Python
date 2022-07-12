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
    n = int(input().strip())
    if (n%2) == 0:
        if (n > 20) or (n in range(2,6)):
            print("Not Weird")
        elif n in range(6,21):
            print("Weird")
    else:
        print("Weird") 

#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    #arithmetic
    print("{}\n{}\n{}").format(a+b, a-b, a*b)

#Python: Division
from __future__ import division

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print("{}\n{}").format(a//b, a/b)
    
#Loops
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)

# Write a function
def is_leap(year):
    leap = False
    
    if (year%4) == 0:
        if (year%100 == 0):
            if (year%400 == 0):
                leap = True
            else:
                leap = False
        else:
            leap = True
        
        
    return leap

year = int(input())
print is_leap(year)

#Print Function
if __name__ == '__main__':
    n = int(input())
    print("".join(str(i) for i in range(1,n+1)))

# Classes: Dealing with Complex Numbers
import math
class Complex(complex):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        return Complex(complex.__add__(self, no))

    def __sub__(self, no):
        return Complex(complex.__sub__(self, no))

    def __mul__(self, no):
        return Complex(complex.__mul__(self, no))

    def __truediv__(self, no):
        return Complex(complex.__truediv__(self, no))

    def mod(self):
        return Complex(complex.__abs__(self))
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')