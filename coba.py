def swap_case(s):
   string_temp = ""
   for i in s:
      if i.islower() == True:
         string_temp += i.upper()
      else:
         string_temp += i.lower()
         
   return string_temp

s = input()
result = swap_case(s)
print(result)