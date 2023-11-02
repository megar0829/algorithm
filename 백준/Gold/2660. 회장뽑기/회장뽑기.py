import sys
input = sys.stdin.readline
from collections import deque


def bfs(start):
    que = deque([start])
    visited = [-1] * (N + 1)
    visited[start] = 0

    while que:
        now = que.popleft()

        for next in arr[now]:
            if visited[next] == -1:
                que.append(next)
                visited[next] = visited[now] + 1

    return max(visited)


N = int(input())

arr = [[] for _ in range(N + 1)]

score = [0] * (N + 1)

while True:
    p1, p2 = map(int, input().split())

    if p1 == -1 and p2 == -1:
        break

    arr[p1].append(p2)
    arr[p2].append(p1)

min_val = 1e9
for i in range(1, N + 1):
    score[i] = bfs(i)
    min_val = min(min_val, score[i])

result = []
for i in range(1, N + 1):
    if score[i] == min_val:
        result.append(i)

print(min_val, len(result))
print(*result)
'''
1 2 3 4 5
2 1 
  3 2
    4 3
      5 4
  4   2
    5   3

3 2 2 2 3
'''
