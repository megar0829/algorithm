import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


# 1. union find 사용
# def find_set(x):
#     if parents[x] == x:
#         return x
    
#     parents[x] = find_set(parents[x])
    
#     return parents[x]


# def union(x, y):
#     x, y = find_set(x), find_set(y)
    
#     if x == y:
#         return
    
#     elif x > y:
#         parents[x] = y
    
#     elif x < y:
#         parents[y] = x
        

# N, M = map(int, input().split())

# known_cnt, *known = list(map(int, input().split()))

# parents = list(range(N + 1))

# party_lst = [list(map(int, input().split())) for _ in range(M)]

# for lst in party_lst:
#     party_cnt, *party = lst
    
#     for i in range(party_cnt - 1):
#         union(party[i], party[i + 1])


# for k in known:
#     parents[parents[k]] = -1
    
# for i in range(1, N + 1):
#     find_set(i)


# ans = 0
        
# for party in party_lst:
#     flag = True
    
#     for p in party[1:]:
#         if parents[p] == -1:
#             flag = False
#             break
        
#     if flag:
#         ans += 1

# print(ans)

from collections import deque
# 2. 그래프 활용

def bfs(num):
    que = deque([num])
    visited = [False] * (N + 1)
    visited[num] = True
    arr[num] = False
    
    while que:
        now = que.popleft()
        
        for next in range(1, N + 1):
            if graph[now][next] and not visited[next]:
                arr[next] = False
                que.append(next)
                visited[next] = True


N, M = map(int, input().split())

known_cnt, *known = list(map(int, input().split()))

party_lst = [list(map(int, input().split())) for _ in range(M)]

graph = [[0] * (N + 1) for _ in range(N + 1)]

arr = [True] * (N + 1)

for cnt, *party in party_lst:
    for i in range(cnt - 1):
        for j in range(i + 1, cnt):
            graph[party[i]][party[j]] = 1
            graph[party[j]][party[i]] = 1

for k in known:
    bfs(k)
    
ans = 0
    
for cnt, *party in party_lst:
    flag = True
    
    for p in party:
        if not arr[p]:
            flag = False
            break
        
    if flag:
        ans += 1

print(ans)