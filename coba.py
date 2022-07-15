def mutate_string(string, position, character):
   string_temp = list(string)
   string_temp[position] = character
   string = "".join(string_temp)
   return string
   
s = input()
i, c = input().split()
s_new = mutate_string(s, int(i), c)
print(s_new)