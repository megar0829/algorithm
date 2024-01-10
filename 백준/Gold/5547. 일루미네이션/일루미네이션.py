from collections import deque
import sys
input = sys.stdin.readline


def check(i, j):
    que = deque([(i, j)])
    visited = [[0] * (W + 1) for _ in range(H + 1)]
    visited[i][j] = 1
    
    while que:
        x, y = que.popleft()
        
        if x % 2:
            for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < H + 1 and 0 < ny < W + 1:
                    if not visited[nx][ny]:
                        if not arr[nx][ny]:
                            que.append((nx, ny))
                            visited[nx][ny] = 1
                else:
                    return True

        else:
            for dx, dy in [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < H + 1 and 0 < ny < W + 1:
                    if not visited[nx][ny]:
                        if not arr[nx][ny]:
                            que.append((nx, ny))
                            visited[nx][ny] = 1   
                else:    
                    return True

    
    return False


def marking(i, j, val):
    que = deque([(i, j)])
    arr[i][j] = val
    
    while que:
        x, y = que.popleft()
        
        if x % 2:
            for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < H + 1 and 0 < ny < W + 1:
                    if not arr[nx][ny]:
                        que.append((nx, ny))
                        arr[nx][ny] = val
        else:
            for dx, dy in [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 < nx < H + 1 and 0 < ny < W + 1:
                    if not arr[nx][ny]:
                        que.append((nx, ny))
                        arr[nx][ny] = val
    
    return False


W, H = map(int, input().split())

arr = [[0] * (W + 1)] + [[0] + list(map(int, input().split())) for _ in range(H)]

# 건물 사이에 있는 부분 찾아서 2로 변경
# 그 외에 바깥 부분은 -1로 변경
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if not arr[i][j]:
            if check(i, j):
                marking(i, j, -1)
            else:
                marking(i, j, 2)
               
# 건물이 있는 경우
# 건물이 보여지는 부분은 6 - (주변에 있는 건물의 수)
result = 0
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if arr[i][j] == 1:
            cnt = 0
            if i % 2:
                for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 < ni < H + 1 and 0 < nj < W + 1:
                        if arr[ni][nj] > 0:
                            cnt += 1
            else:
                for di, dj in [(-1, -1), (-1, 0), (0, 1), (1, 0), (1, -1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 < ni < H + 1 and 0 < nj < W + 1:
                        if arr[ni][nj] > 0:
                            cnt += 1
                            
            result += (6 - cnt)
            
print(result)