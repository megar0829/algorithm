import sys
input = sys.stdin.readline
from collections import deque


import sys
input = sys.stdin.readline
from copy import deepcopy

direction = {
    1: (0, -1),
    2: (-1, -1),
    3: (-1, 0),
    4: (-1, 1),
    5: (0, 1),
    6: (1, 1),
    7: (1, 0),
    8: (1, -1)
}

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

cloud = [[0] * N for _ in range(N)]

cloud[N - 2][0] = 1
cloud[N - 2][1] = 1
cloud[N - 1][0] = 1
cloud[N - 1][1] = 1

num = 1

for _ in range(M):
    d, s = map(int, input().split())
    di, dj = direction[d]

    num += 1
    
    # 구름 이동
    for i in range(N):
        for j in range(N):
            if cloud[i][j] == num - 1:
                ni, nj = (i + di * s) % N, (j + dj * s) % N
                cloud[i][j] = 0
                cloud[ni][nj] += num

            elif cloud[i][j] > num:
                ni, nj = (i + di * s) % N, (j + dj * s) % N
                cloud[ni][nj] += num
                cloud[i][j] = num

    # 구름 있는 칸에 비내리기 & 대각선에 물이 있는지 확인 후 증가
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                graph[i][j] += 1

    copy_graph = deepcopy(graph)
    
    for i in range(N):
        for j in range(N):
            if cloud[i][j]:
                cloud[i][j] = -1

                for di, dj in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        if copy_graph[ni][nj]:
                            graph[i][j] += 1

    # 새로운 구름 생성
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and cloud[i][j] != -1:
                graph[i][j] -= 2
                cloud[i][j] = num

            if cloud[i][j] == -1:
                cloud[i][j] = 0
                
result = 0
for i in range(N):
    result += sum(graph[i])

print(result)