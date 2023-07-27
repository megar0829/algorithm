import sys
input = sys.stdin.readline

N, M = map(int, input().split())
text = [input() for _ in range(N)]
find = [input() for _ in range(M)]
cnt = 0 
for i in find:
    if i in text:
        cnt += 1
print(cnt)