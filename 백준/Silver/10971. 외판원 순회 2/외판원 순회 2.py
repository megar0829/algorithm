import sys
input = sys.stdin.readline


def backTracking(start, i, sum_val):
    global min_val
    if i == N - 1 and arr[start][0] != 0:
        min_val = min(min_val, sum_val + arr[start][0])
        return
    
    for j in range(N):
        if not visited[j] and arr[start][j]:
            visited[j] = 1
            backTracking(j, i + 1, sum_val + arr[start][j])
            visited[j] = 0


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [0] * N
min_val = 1e9

visited[0] = 1
backTracking(0, 0, 0)
print(min_val)