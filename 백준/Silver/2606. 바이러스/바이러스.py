import sys
input = sys.stdin.readline

V = int(input())
E = int(input())
arr = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
for _ in range(E):
    v, w = map(int, input().split())
    arr[v].append(w)
    arr[w].append(v)
stack = []
n = 1
visited[n] = True
while True:
    for w in range(len(arr[n])):
        if len(arr[n]) and visited[arr[n][w]] == False:
            stack.append(n)
            n = arr[n].pop(w)
            visited[n] = True
            break
    else:
        if stack:
            n = stack.pop()
        else:
            break
result = 0
for i in range(2, V + 1):
    if visited[i] == True:
        result += 1
print(result)