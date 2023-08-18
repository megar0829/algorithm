def bfs(start):
    visited = [0] * 101
    queue = []
    queue.append(start)
    visited[start] = 1
    while queue:
        t = queue.pop(0)
        for w in arr[t]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = visited[t] + 1
    return visited


def find_max(arr):
    max_val = 0
    for i in range(101):
        if max_val < arr[i]:
            max_val = arr[i]
    max_lst = []
    for i in range(101):
        if arr[i] == max_val:
            max_lst.append(i)
    return max_lst[-1]


for tc in range(1, 11):
    N, start = map(int, input().split())
    E = list(map(int, input().split()))
    arr = [[] for _ in range(101)]
    for i in range(0, len(E), 2):
        if E[i + 1] not in arr[E[i]]:
            arr[E[i]].append(E[i + 1])
    print(f'#{tc} {find_max(bfs(start))}')