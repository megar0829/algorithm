def backTracking(i):
    if i == M:
        result.add(tuple(numbers))
        return 
    
    for idx in range(N):
        if not used[idx]:
            if i and numbers[i - 1] > arr[idx]:
                continue
            used[idx] = 1
            numbers.append(arr[idx])
            backTracking(i + 1)
            used[idx] = 0
            numbers.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
numbers = []
used = [0] * N
result = set()

backTracking(0)
for rlt in sorted(result):
    print(*rlt)