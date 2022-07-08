#fungsi
from ast import arg


def coba(a,b):
   '''fungsi coba'''
   print('hai')
   return a+b

for i in range(0,5) : 
   print(coba(2,3)+coba(4,5))

#default fungsi
def coba2(input1=1,input2=2,input3=3):
   print(input1 + input2 + input3)

coba2(input2=4)

#fungsi dengan hints
def coba3(a:int,b:str):
   print(a**5)
   print(b)

coba3(5,"hai")

# (*args) pada fungsi
def coba4(*args:int):
   a = args[0]
   b = args[1]
   c = args[2]
   print(a+b+c)

print(coba4(1,2,3))

def coba5(*angka:int):
   a = 1
   for i in angka:
      a = a * i
   
   return a

print(coba5(1,2,3,4,5))

# (**kwargs) pada fungsi
def coba6(**data:int):
   a = 1
   for i in data.values() : 
      a = a * i
   
   return a

print(coba6(a=1,b=2,c=3,d=4,e=5))

# fungsi lambda
coba7 = lambda angka,pangkat:angka**pangkat
print(coba7(2,4))

# fungsi anonymous(currying)
def pangkat(x):
   return lambda angka:angka**x

coba8 = pangkat(4)
print(coba8(2))
