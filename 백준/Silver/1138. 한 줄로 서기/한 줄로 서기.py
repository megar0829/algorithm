N = int(input())
arr = list(reversed(list(map(int, input().split()))))

rlt = []

for j in range(N - 1, -1, -1):
    rlt.insert(arr[N - 1 - j], j + 1)

print(*rlt)