N = int(input())
for _ in range(N):
    sentence = input()
    result = ''
    for i in range(len(sentence)):
        if i == 0:
            result += sentence[i].upper()
        else:
            result += sentence[i]
    print(result)