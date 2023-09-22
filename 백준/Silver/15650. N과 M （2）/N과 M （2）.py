N, M = map(int, input().split())
arr = list(range(1, N + 1))
path = [0] * M
result = []

def backTracking(idx):
    if idx == M:
        if sorted(path) not in result:
            result.append(sorted(path))
        return
    for num in arr:
        if num not in path:
            path[idx] = num
            backTracking(idx + 1)
            path[idx] = 0

backTracking(0)

for rlt in sorted(result):
    print(*rlt)