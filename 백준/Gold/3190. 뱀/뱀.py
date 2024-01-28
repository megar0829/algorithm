from collections import deque
import sys
input = sys.stdin.readline


N = int(input())
K = int(input())
arr = [[0] * N for _ in range(N)]

for _ in range(K):
    x, y = map(int, input().split())
    arr[x - 1][y - 1] = 2

times = [''] * (10001)

L = int(input())
for _ in range(L):
    X, C = input().split()
    times[int(X)] = C

direction = {
    0: (0, 1),
    1: (1, 0),
    2: (0, -1),
    3: (-1, 0),
}


def move():
    snake = deque([(0, 0)])
    t = 0
    i, j = 0, 0
    d = 0

    while True:
        ni, nj = i + direction[d % 4][0], j + direction[d % 4][1]

        t += 1

        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in snake:
            snake.append((ni, nj))
            if arr[ni][nj]:
                arr[ni][nj] = 0
            else:
                snake.popleft()

            if times[t]:
                if times[t] == 'L':
                    d -= 1
                elif times[t] == 'D':
                    d += 1
        else:
            break

        i, j = ni, nj

    return t

print(move())