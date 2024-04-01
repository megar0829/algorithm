import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(node, sum_dist, prev_dist):
    visited[node] = True
    
    if node == R2 :
        print(sum_dist - prev_dist)
        exit(0)

    for next,dist in arr[node]:
        if not visited[next]:
            dfs(next, sum_dist + dist, max(dist, prev_dist))
        
        
N, R1, R2 = map(int, input().split())

arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    r1, r2, dist = map(int, input().split())
    
    arr[r1].append((r2, dist))
    arr[r2].append((r1, dist))
    


visited = [False] * (N + 1)

if R1 == R2:
    print(0)
    
else: 
    dfs(R1, 0, 0)