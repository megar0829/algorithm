import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[1e9] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):   
        for j in range(1, N + 1):   
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

min_val = 1e9
result = []

for i in range(1, N):  
    for j in range(2, N + 1):
        sum_val = 0
        
        for k in range(1, N + 1):  
            sum_val += min(graph[k][i], graph[k][j]) * 2 
            
        if sum_val < min_val:
            min_val = sum_val
            result = [i, j, sum_val]

print(*result)