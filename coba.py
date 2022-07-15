# Enter your code here. Read input from STDIN. Print output to STDOUT
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