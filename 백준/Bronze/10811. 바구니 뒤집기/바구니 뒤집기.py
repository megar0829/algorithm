N, M = map(int, input().split())
balls = list(range(1, N+1))
copy_balls = list(range(1, N+1))
for _ in range(M): 
    i, j = list(map(int, input().split()))
    for k in range(j-i+1):
        balls[j-1-k] = copy_balls[i-1+k]
    for l in range(N):
        copy_balls[l] = balls[l]      
print(*balls)