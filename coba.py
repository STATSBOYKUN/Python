n = input()

for _ in range(int(n)):
    word_temp = str(input())
    word1, word2 = "", ""
    for i in range(len(word_temp)):
        if i%2 == 0:
            word1 += (word_temp[i])
        else:
            word2 += (word_temp[i])
    print(word1+" "+word2)