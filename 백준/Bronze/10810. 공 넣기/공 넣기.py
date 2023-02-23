N, M = map(int, input().split())
balls = [0] * N
for _ in range(M):
    i, j, k = list(map(int, input().split()))
    for i in range(i-1, j):
        balls[i] = k
print(*balls)