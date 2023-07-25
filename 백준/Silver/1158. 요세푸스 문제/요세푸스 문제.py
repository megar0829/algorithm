import sys
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(range(1, N + 1))
josephuse = [0 for _ in range(N)]
cnt = K - 1
for i in range(N):
    josephuse[i] = lst.pop(cnt)
    cnt += K - 1
    while True:
        if len(lst) == 0:
            break
        if cnt >= len(lst):
            cnt -= len(lst)
        else:
            break
result = '<'
for i in josephuse[:-1]:
    result += str(i) + ', '
result += str(josephuse[-1]) + '>'
print(result)