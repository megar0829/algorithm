T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']
for t in range(1, T+1):
    word = input()
    consonant = ''
    for i in word:
        if i in vowel:
            pass
        else:
            consonant += i
    print(f'#{t} {consonant}')