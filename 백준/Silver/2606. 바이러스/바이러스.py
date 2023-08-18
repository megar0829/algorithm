import sys
input = sys.stdin.readline


def dfs(n):
    cnt = 0
    stack = []
    stack.append(n)
    visited[n] = True
    while stack:
        for w in range(len(arr[n])):
            if not visited[arr[n][w]]:
                stack.append(n)
                n = arr[n].pop(w)
                visited[n] = True
                cnt += 1
                break
        else:
            if stack:
                n = stack.pop()
    return cnt


V = int(input())
E = int(input())
arr = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
for _ in range(E):
    v, w = map(int, input().split())
    arr[v].append(w)
    arr[w].append(v)
print(dfs(1))