t = int(input())
num_alp = {}
alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for a in range(26):
    num_alp[alp[a]] = a + 1
for _ in range(t):
    word1, word2 = input().split()
    dif_word = []
    for i in range(len(word1)):
        if num_alp[word1[i]] > num_alp[word2[i]]:
            dif_word.append((num_alp[word2[i]] + 26) - num_alp[word1[i]])
        else:
            dif_word.append(num_alp[word2[i]] - num_alp[word1[i]])
    print('Distances:', *dif_word)