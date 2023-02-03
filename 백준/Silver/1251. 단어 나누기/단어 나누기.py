word = input()
n = len(word)
words = []
for i in range(1, n-1):
    for j in range(i+1, n):
        text1 = word[0:i]
        text2 = word[i:j]
        text3 = word[j:n]
        spl_word = text1[::-1] + text2[::-1] +text3[::-1]
        words.append(spl_word)
print(sorted(words)[0])