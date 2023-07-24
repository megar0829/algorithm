import sys
input = sys.stdin.readline

N, K = map(int, input().split())

josephus = []
lst = list(range(1, N + 1))
cnt = (K - 1)

while True:
    josephus.append(lst.pop(cnt))
    cnt += K - 1
    if len(lst) == 0:
        break
    while True:
        if cnt > len(lst) - 1:
            cnt -= len(lst)
        else:
            break
result = '<'
for i in josephus[:N-1]:
    result += str(i) + ', '
result += str(josephus[N-1]) + '>'
print(result) 