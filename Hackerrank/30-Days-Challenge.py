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

# Day 4: Class vs. Instance
class Person:
    def __init__(self,initialAge):
        self.age = initialAge
    def amIOld(self):
        if self.age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0
            print("You are young.")
            self.age = 3
        elif self.age < 13:
            print("You are young.")
        elif self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")
    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")

# Day 5: Loops
n = int(input().strip())
for i in range(1, 11):
    print("{} x {} = {}".format(n,i, n*i))
    
# Day 6: Let's Review
n = input()

for _ in range(int(n)):
    word_temp = str(input())
    word1, word2 = "", ""
    for i in range(len(word_temp)):
        if i%2 == 0:
            word1 += (word_temp[i])
        else:
            word2 += (word_temp[i])
    print(word1+" "+word2)

# Day 7: Arrays
n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
arr.reverse()
for i in arr:
    print(i, end=" ")

# Day 8: Dictionaries and Maps
n = int(input())
list_temp = [input().split() for i in range(n)]
dict_temp = {k: v for k,v in list_temp}

while True:
    try:
        name = input()
        if name in dict_temp:
            print("{}={}".format(name, dict_temp[name]))
        else:
            print("Not found")
    except:
        break

# Day 9: Recursion 3
def factorial(n):
    if n == 1 or 0:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()

# Day 10: Binary Numbers
bin_temp = bin(int(input()))
text_temp = bin_temp[2:]
list_temp = text_temp.split("0")

print(len(max(list_temp)))

# Day 11: 2D Arrays
list_temp = []
for i in range(6):
    list_temp.append(input().split())

sum_temp = 0
list_sum = []
for i in range(4):
    for j in range(4):
        sum_temp += (int(list_temp[i][j]) + int(list_temp[i][j+1]) + int(list_temp[i][j+2]))
        sum_temp += (int(list_temp[i+1][j+1]))
        sum_temp += (int(list_temp[i+2][j]) + int(list_temp[i+2][j+1]) + int(list_temp[i+2][j+2]))
        
        list_sum.append(sum_temp)
        sum_temp = 0

print(max(list_sum))

# Day 12: Inheritance
class Person:
   	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
    def calculate(self):
        avg = sum(self.scores)/len(self.scores)
        if avg >= 90:
            return "O"
        elif avg >= 80:
            return "E"
        elif avg >= 70:
            return "A"
        elif avg >= 55:
            return "P"
        elif avg >= 40:
            return "D"
        else:
            return "T"

line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())