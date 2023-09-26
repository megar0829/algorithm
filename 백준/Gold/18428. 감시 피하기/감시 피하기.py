import sys
input = sys.stdin.readline


def backTracking(idx):
    global result
    if idx == 3:
        if check():
            result = 'YES'
        return

    if result == 'YES':
        return

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                arr[i][j] = 'O'
                backTracking(idx + 1)
                arr[i][j] = 'X'


def check():
    for i, j in teacher:
        for di, dj in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            ni, nj = i + di , j + dj
            while 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 'O':
                    break
                if arr[ni][nj] == 'S':
                    return False
                ni += di
                nj += dj
    return True


N = int(input())
arr = [list(input().split()) for _ in range(N)]
teacher = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 'T':
            teacher.append((i, j))

result = 'NO'

backTracking(0)

print(result)