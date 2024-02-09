import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def dfs(now, cnt):
    if cnt == 3:
        a, b, c = save_lst

        if denied[a][b] or denied[b][c] or denied[c][a]:
            return

        result.add(tuple(save_lst))
        return

    for next in range(now + 1, N + 1):
        if not denied[now][next]:
            save_lst.append(next)
            dfs(next, cnt + 1)
            save_lst.pop()


N, M = map(int, input().split())

denied = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    denied[x][y] = 1
    denied[y][x] = 1

result = set()

save_lst = []

dfs(0, 0)

print(len(result))