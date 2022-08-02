n = int(input())
list_temp = [input().split() for i in range(n)]
dict_temp = {k: v for k,v in list_temp}

while True:
    try:
        name = input()
        if name in dict_temp:
            print("{}={}".format(name, dict_temp[name]))
        else:
            print("Not found")
    except:
        break