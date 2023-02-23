N, M = map(int, input().split())
balls = list(range(1, N+1))
save = 0
for _ in range(M): 
    i, j = list(map(int, input().split()))
    save = balls[i-1]
    balls[i-1] = balls[j-1]
    balls[j-1] = save
print(*balls)