N = input()
num = input().split()
for i in range(len(num)):
   num[i] = int(num[i])
   
tuple_temp = tuple(num)
print(hash(tuple_temp))