import sys
input = sys.stdin.readline


def dfs(lst):
    stack = [lst[0]]
    visited = [0] * (N + 1)
    t = lst[0]
    visited[t] = 1
    cnt = 1
    while stack:
        for w in arr[t]:
            if not visited[w] and w in lst:
                stack.append(w)
                visited[w] = 1
                cnt += 1
                continue
        else:
            if stack:
                t = stack.pop()
    if cnt == len(lst):
        return True
    return False


def dist(lst):
    save_lst = 0
    for i in lst:
        save_lst += node[i]
    return save_lst


N = int(input())
node = [0] + list(map(int, input().split()))
arr = [[] for _ in range(N + 1)]
min_val = 100000
for i in range(1, N + 1):
    n, *w = list(map(int, input().split()))
    for j in range(n):
        arr[i].append(w[j])

for i in range(1, 1 << (N - 1)):
    sub1 = []
    sub2 = []
    for j in range(N):
        if i & (1 << j):
            sub1.append(j + 1)
        else:
            sub2.append(j + 1)
    if dfs(sub1) and dfs(sub2):
        min_val = min(min_val, abs(dist(sub1) - dist(sub2)))

if min_val == 100000:
    min_val = -1
print(min_val)

