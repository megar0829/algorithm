import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    text = list(input().split())
    result = ''
    for i in range(len(text)):
        for j in range(len(text[i]) - 1, -1, -1):
            result += text[i][j]
        result += ' '
    print(result)