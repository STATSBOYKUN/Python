def split_and_join(line):
   word_temp = line.split(" ")
   return "-".join(word_temp)

line = input()
result = split_and_join(line)
print(result)