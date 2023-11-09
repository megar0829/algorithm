def dfs(x, y, idx, word):
    global cnt

    if idx == 6:
        return

    words.setdefault(word, 0)
    words[word] += 1

    for dx, dy in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        nx, ny = (x + dx) % N, (y + dy) % M
        dfs(nx, ny, idx + 1, word + graph[nx][ny])


N, M, K = map(int, input().split())

graph = [list(input()) for _ in range(N)]

words = {}

for i in range(N):
    for j in range(M):
        dfs(i, j, 1, graph[i][j])


for _ in range(K):
    s = input()

    words.setdefault(s, 0)

    print(words[s])

