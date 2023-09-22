def backTracking(i, idx):
    global min_val

    if i == N // 2:
        sum_start = 0
        sum_link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    sum_start += arr[i][j]
                elif not visited[i] and not visited[j]:
                    sum_link += arr[i][j]
        min_val = min(min_val, abs(sum_start - sum_link))
        return

    for num in range(idx, N):
        if not visited[num]:
            visited[num] = 1
            backTracking(i + 1, num + 1)
            visited[num] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_val = 1e9
backTracking(0, 0)

print(min_val)