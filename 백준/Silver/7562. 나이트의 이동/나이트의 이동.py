import sys
input = sys.stdin.readline


def bfs(start):
    que = []
    que.append((start[0], start[1]))
    visited[start[0]][start[1]] = 1
    while que:
        i, j = que.pop(0)
        if arr[i][j] == 2:
                    return visited[i][j] - 1
        for k in range(8):
            ni, nj = i + di[k], j + dj[k]
            
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] != 1 and visited[ni][nj] == 0:
                    que.append((ni, nj))
                    visited[ni][nj] = visited[i][j] + 1
                
    


di = [-2, -1, 1, 2, 2, 1, -1, -2]
dj = [1, 2, 2, 1, -1, -2, -2, -1]

T = int(input())
for _ in range(T):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    start1, start2 = map(int, input().split())
    arr[start1][start2] = 1
    end1, end2 = map(int, input().split())
    arr[end1][end2] = 2
    visited = [[0] * N for _ in range(N)]
    print(bfs((start1, start2)))