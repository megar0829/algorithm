import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = [[0] * M for _ in range(N)]

k = min(N, M) // 2

arr_idx = []

for i in range(k):
    save_idx = []
    x, y = i, i

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if (dx, dy) == (-1, 0) or (dx, dy) == (1, 0):
            for _ in range(N - 1):
                save_idx.append((x, y))
                x += dx
                y += dy
        else:
            for _ in range(M - 1):
                save_idx.append((x, y))
                x += dx
                y += dy

    arr_idx.append(save_idx)
    N -= 2
    M -= 2

for idx in arr_idx:
    l = len(idx)
    for j in range(l):
        now = idx[j]

        next = idx[(j + R) % l]

        result[next[0]][next[1]] = arr[now[0]][now[1]]

for rlt in result:
    print(*rlt)