N = int(input())
arr_temp = []      

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