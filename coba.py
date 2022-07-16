def solve(s):
    s_temp = s.split(" ")
    s_capitalize = ""
    for i in range(len(s_temp)):
        s_capitalize += s_temp[int(i)].capitalize()
        s_capitalize += " "
    return s_capitalize

s = input()
result = solve(s)
print(result)