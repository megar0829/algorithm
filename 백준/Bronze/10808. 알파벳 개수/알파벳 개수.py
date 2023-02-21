dict_word = {}
for i in 'abcdefghijklmnopqrstuvwxyz':
    dict_word[i] = 0
for j in input():
    dict_word[j] += 1
print(*dict_word.values())