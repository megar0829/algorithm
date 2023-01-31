N = int(input())
text = ['*']*(N)
for i in range(N):
    print(*sorted(text), sep='')
    text.pop(0)
    text.append(' ')