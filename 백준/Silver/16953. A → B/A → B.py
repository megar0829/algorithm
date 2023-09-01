from collections import deque

def bfs():
    que = deque()
    que.append(B)
    visited = {}
    visited[int(B)] = 1
    while que:
        t = que.popleft()
        if t == A:
            return visited[int(t)]
        if int(t) == 1:
            return -1
        if 1 <= int(t) <= 10 ** 9:
            if int(t) % 2 == 0:
                w = str(int(t) // 2)
                que.append(w)
                if int(w) not in visited:
                    visited[int(w)] = visited[int(t)] + 1
            if t[-1] == '1':
                w = t[:-1]
                que.append(w)
                if int(w) not in visited:
                    visited[int(w)] = visited[int(t)] + 1
    return -1


A, B = input().split()
print(bfs())