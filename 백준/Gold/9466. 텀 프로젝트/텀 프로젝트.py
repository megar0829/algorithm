import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def dfs(x):
    global cnt
    visited[x] = 1
    cycle.append(x)
    num = arr[x]

    if not visited[num]:
        dfs(num)
    else:
        if num in cycle:
            cnt += len(cycle[cycle.index(num):])
        return
        

T = int(input())

for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [0] * (n + 1)
    cnt = 0

    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n - cnt)