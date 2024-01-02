from collections import deque


def bfs(n, computers, computer, visited):
    visited[computer] = 1
    que = deque([computer])
    
    while que:
        now = que.popleft()
        visited[now] = True
        for next in range(n):
            if next != now:
                if computers[now][next] == 1:
                    if visited[next] == False:
                        que.append(next)


def solution(n, computers):
    answer = 0
    visited = [0] * n
    for computer in range(n):
        if not visited[computer]:
            bfs(n, computers, computer, visited)
            answer += 1
    return answer