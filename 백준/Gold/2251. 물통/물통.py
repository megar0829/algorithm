from collections import deque


def bfs():    
    que = deque([(0, 0)])
    
    visited = [[False] * (B + 1) for _ in range(A + 1)]
    visited[0][0] = True
    
    result = []
    
    while que:
        a, b = que.popleft()
        c = C - (a + b)
        
        if not a:
            result.append(c)
            
        x, y = a - min(a, (B - b)), b + min(a, (B - b))
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x, y))
        
        x, y = a - min(a, C - c), b
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x, y))

        x, y = a + min(b, A - a), b - min(b, A - a)
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x, y))
                    
        x, y = a, b - min(b, C - c)
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x, y))
            
        x, y = a + min(c, A - a), b
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x, y))
            
        x, y = a, b + min(c, B - b)
        if not visited[x][y]:
            visited[x][y] = True
            que.append((x, y))
        
    return sorted(result)


A, B, C = map(int, input().split())

print(*bfs())