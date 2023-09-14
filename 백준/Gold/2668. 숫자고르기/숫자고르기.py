import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]
for i in range(N):
    arr[int(input())].append(i + 1)

result = set([])
for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    stack = [i]
    visited[i] = 1
    while stack:
        t = stack.pop()
        for j in arr[t]:
            if not visited[j]:
                stack.append(j)
                visited[j] = 1
            elif visited[j] and i == j:
                result.add(j)

result = sorted(list(result))
print(len(result))
for i in result:
    print(i)