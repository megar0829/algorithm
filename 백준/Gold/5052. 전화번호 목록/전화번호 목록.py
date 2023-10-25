import sys
input = sys.stdin.readline


t = int(input())
for tc in range(t):
    n = int(input())
    word = sorted([input().strip('\n') for _ in range(n)])
    
    flag = False
    for i in range(n - 1):
        l = len(word[i])
        if word[i] == word[i + 1][:l]:
            flag = True
            break
    
    if flag:
        print('NO')
    else:
        print('YES')