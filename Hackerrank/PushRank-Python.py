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

# List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if (a+b+c) != n])

# Nested Lists
data_temp = []
second_lowest_names = []
scores = set()

for _ in range(int(input())):
    name = input()
    score = float(input())
    data_temp.append([name, score])
    scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in data_temp:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')

# Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    score_temp = student_marks[query_name]
    print("{0:.2f}".format((sum(score_temp)/len(score_temp))))

# itertools.combinations_with_replacement()
from itertools import combinations_with_replacement

str_temp = list(input().split())
list_temp = list(combinations_with_replacement(sorted(str_temp[0]),int(str_temp[1])))

for i in list_temp:
   print("".join(i), end="\n") 


# Compress the String!
from itertools import groupby

int_temp = input()
list_temp = [list(g) for k, g in groupby(int_temp)]

for i in list_temp:
   print("("+str(len(i))+", "+str(i[0])+")", end=" ")

# Iterables and Iterators
from itertools import combinations

n = input()
word_temp = input().split()
r = int(input())

list_temp = list(combinations(''.join(word_temp),r))

count_word = 0
for i in list_temp:
   if 'a' in i:
      count_word += 1

print("{0:.3f}".format(count_word/len(list_temp)))

N = int(input())
arr_temp = []      

# Lists
for _ in range(N):
   command_temp = input().split()
   argument_temp = ["insert", "remove", "append", "pop", "reverse", "sort", "print"]
   if str(command_temp[0]) == argument_temp[0]:
      arr_temp.insert(int(command_temp[1]), int(command_temp[2]))
   elif str(command_temp[0]) == argument_temp[1]:
      arr_temp.remove(int(command_temp[1]))
   elif str(command_temp[0]) == argument_temp[2]:
      arr_temp.append(int(command_temp[1]))
   elif str(command_temp[0]) == argument_temp[3]:
      arr_temp.pop()
   elif str(command_temp[0]) == argument_temp[4]:
      arr_temp.reverse()
   elif str(command_temp[0]) == argument_temp[5]:
      arr_temp.sort()
   elif str(command_temp[0]) == argument_temp[6]:
      print(arr_temp)

# Tuples
N = input()
num = input().split()
for i in range(len(num)):
   num[i] = int(num[i])
   
tuple_temp = tuple(num)
print(hash(tuple_temp))

# sWAP cASE
def swap_case(s):
   string_temp = ""
   for i in s:
      if i.islower() == True:
         string_temp += i.upper()
      else:
         string_temp += i.lower()
         
   return string_temp

s = input()
result = swap_case(s)
print(result)

# String Split and Join
def split_and_join(line):
   word_temp = line.split(" ")
   return "-".join(word_temp)

line = input()
result = split_and_join(line)
print(result)

# What's Your Name?
def print_full_name(first, last):
   print("Hello {} {}! You just delved into python.".format(first,last))
   
first_name = input()
last_name = input()
print_full_name(first_name, last_name)

# Mutations
def mutate_string(string, position, character):
   string_temp = list(string)
   string_temp[position] = character
   string = "".join(string_temp)
   return string
   
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)

# Find a string
def count_substring(string, sub_string):
   count = 0
   for i in range(len(string)):
      if string[i:i+len(sub_string)] == sub_string:
         count += 1

   return count
   
string = input().strip()
sub_string = input().strip()
    
count = count_substring(string, sub_string)
print(count)

# String Validators
s = input()

print(any(i.isalnum()  for i in s))
print(any(i.isalpha() for i in s))
print(any(i.isdigit() for i in s))
print(any(i.islower() for i in s))
print(any(i.isupper() for i in s))

# Text Alignment
#Replace all ______ with rjust, ljust or center. 
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
# Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)

# Designer Door Mat
n = input().split()
a = "-"
b = ".|."
range_temp = [int(i) for i in range(1, int(n[0])) if (i%2) != 0]

for i in range_temp:
    print((i*b).center(int(n[1]),a))

print("WELCOME".center(int(n[1]),a))

range_temp.reverse()
for i in range_temp:
    print((i*b).center(int(n[1]),a))
    
# String Formatting
def print_formatted(number):
    width = len(bin(number)) - 2
    for i in range(1, number + 1):
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

n = int(input())
print_formatted(n)

# Alphabet Rangoli
import string

def print_rangoli(size):
    alpha = string.ascii_lowercase

    L = []
    for i in range(size):
        s = "-".join(alpha[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
    print('\n'.join(L[:0:-1]+L))
    
# Capitalize!
def solve(s):
    s_temp = s.split(" ")
    s_capitalize = ""
    for i in range(len(s_temp)):
        s_capitalize += s_temp[int(i)].capitalize()
        s_capitalize += " "
    return s_capitalize

s = input()
result = solve(s)
print(result)