N = int(input())
n = 1
for i in range(1, N+1):
    if N == 1:
        print(N)
        break
    elif n < N <= n + 6*i:
        print(i+1)
        break    
    n = n + 6*i