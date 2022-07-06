# buat list
from copy import deepcopy


data = [range(0,10)]
print(data)

data = list(range(1,9))
print(data)

data = [i * 2 for i in range(1,9) if i%2]
print(data)

#manipulasi data
data[2] = 5
print(data)

data.append(7)
print(data)

data.insert(2,5)
print(data)

data.remove(data[2])
print(data)

data.pop()
print(data)

print(f"Panjang data : {len(data)}")
print(f"Data 2 : {data.count(2)}")
print(f"Index Data 2 : {data.index(2)}")

# urut list
data.sort()
data.reverse()
print(data)

data.sort()
print(data)

print(f"Alamat data : {hex(id(data))}")

#copy list
data2 = data.copy()
print(data2)

#nested list
data3 = [data, data2]
print(data3[0][0])

#copy nested list
data4 = deepcopy(data3)
print(data2)