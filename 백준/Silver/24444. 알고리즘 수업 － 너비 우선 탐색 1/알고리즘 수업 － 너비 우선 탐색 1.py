import sys
input = sys.stdin.readline


def bfs(start):
    visited = [0] * (N + 1)
    que = []
    que.append(start)
    visited[start] = 1
    result = [0] * (N + 1)
    cnt = 1
    while que:
        t = que.pop(0)
        result[t] = cnt
        cnt += 1
        for w in arr[t]:
            if visited[w] == 0:
                que.append(w)
                visited[w] = 1
    return result


N, M, R = list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)
for i in range(N):
    arr[i].sort()
for i in bfs(R)[1:]:
    print(i)