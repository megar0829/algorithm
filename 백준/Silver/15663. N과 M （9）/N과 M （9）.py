def backTracking(i):
    if i == M:
        result.add(tuple(numbers))
        return 
    
    for idx in range(N):
        if not used[idx]:
            used[idx] = 1
            numbers[i] = arr[idx]
            backTracking(i + 1)
            used[idx] = 0
            numbers[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
numbers = [0] * M
used = [0] * N
result = set()

backTracking(0)
for rlt in sorted(result):
    print(*rlt)