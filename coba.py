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