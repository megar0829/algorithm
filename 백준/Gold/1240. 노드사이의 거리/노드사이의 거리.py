import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    f, s, d = map(int, sys.stdin.readline().split())
    graph[f].append((d, s))
    graph[s].append((d, f))

for _ in range(M):
    first, second = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(N+1)]

    dq = deque()
    # first에서 출발
    dq.append((0, first))

    while dq:
        now_dist, now_node = dq.popleft()
        # node 방문 처리
        visited[now_node] = True
		
        # 만약 찾고 있는 second 노드라면 거리 출력하고 중지
        if now_node == second:
            print(now_dist)
            break
        else:
            for next_dist, next_node in graph[now_node]:
            	# 이전에 방문하지 않았던 노드만 탐색
                if not visited[next_node]:
                    dq.append((next_dist + now_dist, next_node))