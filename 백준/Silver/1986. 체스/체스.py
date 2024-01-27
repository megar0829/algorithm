import sys
input = sys.stdin.readline

n, m = map(int, input().split())
queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))

chess = [[0] * m for _ in range(n)]

queen_idx = []
for i in range(queen[0]):
    chess[queen[i * 2 + 1] - 1][queen[i * 2 + 2] - 1] = 1
    queen_idx.append((queen[i * 2 + 1] - 1, queen[i * 2 + 2] - 1))

knight_idx = []
for i in range(knight[0]):
    chess[knight[i * 2 + 1] - 1][knight[i * 2 + 2] - 1] = 2
    knight_idx.append((knight[i * 2 + 1] - 1, knight[i * 2 + 2] - 1))

for i in range(pawn[0]):
    chess[pawn[i * 2 + 1] - 1][pawn[i * 2 + 2] - 1] = 3


def move_queen(x, y):
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if chess[nx][ny] <= 1:
                chess[nx][ny] = 1

                while True:
                    nx += dx
                    ny += dy

                    if 0 <= nx < n and 0 <= ny < m and chess[nx][ny] <= 1:
                        chess[nx][ny] = 1

                    else:
                        break

def move_knight(x, y):
    for dx, dy in [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < n and 0 <= ny < m:
            if not chess[nx][ny]:
                chess[nx][ny] = 2


for i, j in queen_idx:
    move_queen(i, j)

for i, j in knight_idx:
    move_knight(i, j)


rlt = 0
for i in range(n):
    for j in range(m):
        if not chess[i][j]:
            rlt += 1

print(rlt)