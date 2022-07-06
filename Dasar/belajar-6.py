import os
from random import random

#list
data_list = list(range(1,5))
print(data_list)

#tuples
data_tuples = tuple(range(1,5))
print(data_tuples)

#sets
data_sets = set(range(1,10))
print(data_sets)

#dictionary
data_dictionary = {
   1 : "Umar",
   2 : "Ucup",
   3 : data_list,
   4 : data_tuples,
   5 : data_sets
}
print(data_dictionary[4])
print(data_dictionary.get(6,"Nda ada boyy"))

#operasi dictionary
data_dictionary[1] = 5
data_dictionary.update({6:2})
print(data_dictionary)

data_dictionary.__delitem__(1)
del(data_dictionary[2])
print(data_dictionary)

for value in data_dictionary.values():
   print(value)

for key in data_dictionary.keys():
   print(key)

for item in data_dictionary.items():
   print(item)

os.system("cls")
#nested dictionary
data_dictionary2 = {
   1 : "Umar",
   2 : "Ucup",
   3 : data_list,
   4 : data_tuples,
   5 : data_sets
}

data_dictionary3 = {
   1 : data_dictionary,
   2 : data_dictionary2
}
print(data_dictionary3[1][6])