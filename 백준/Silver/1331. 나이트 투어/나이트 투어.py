from collections import deque


def night_search(x, y):
    global cnt
    i, j = que.popleft()
    
    for di, dj in [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < 6 and 0 <= nj < 6 and not arr[ni][nj]:
            if ni == x and nj == y:
                arr[ni][nj] = 1
                cnt += 1
                return

alp = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5
    }

arr = [[0] * 6 for _ in range(6)]
que = deque()
cnt = 0
for n in range(36):
    idx = input()
    x, y = int(idx[1]) - 1, alp[idx[0]]
    que.append([x, y])
    if n == 0:
        start = [x, y]
    else:
        night_search(x, y)
    if n == 35:
        que.append(start)
        night_search(start[0], start[1])
    
if cnt == 36:
    print('Valid')
else:
    print('Invalid')