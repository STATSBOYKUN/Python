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