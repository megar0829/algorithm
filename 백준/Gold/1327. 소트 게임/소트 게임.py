from collections import deque


def bfs():
    global result
    que = deque([])
    for i in range(N - K + 1):
        que.append((i, arr_str, 0))
    visited.setdefault(arr_str, 1)
    
    while que:
        idx, val, cnt = que.popleft()
        
        if val == answer:
            result = min(result, cnt)
            break
        
        save_str = val[0:idx] + val[idx:idx + K][::-1] + val[idx + K:]

        visited.setdefault(save_str[:], 0)
        if visited[save_str[:]]:
            continue
        else:
            visited[save_str[:]] = 1
            for i in range(N - K + 1):
                que.append((i, save_str[:], cnt + 1))


N, K = map(int, input().split())
arr = list(map(int, input().split()))

arr_str = ''
for num in arr:
    arr_str += str(num)
    
answer = ''
for num in sorted(arr):
    answer += str(num)

visited = dict()

result = 1e9

bfs()

if result == 1e9:
    result = -1

print(result)