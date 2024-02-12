import sys
input = sys.stdin.readline

N = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(N):
    x, y = map(int, input().split())
    arr[y].append(x)

for i in range(N + 1):
    arr[i].sort()

result = 0

for i in range(N + 1):
    lst = arr[i]

    l = len(lst)
    for j in range(l):
        if j == 0:
            result += lst[j + 1] - lst[j]

        elif j == l - 1:
            result += lst[j] - lst[j - 1]

        else:
            result += min(lst[j + 1] - lst[j], lst[j] - lst[j - 1])

print(result)
