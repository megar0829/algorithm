from collections import deque

n, w, L = list(map(int, input().split()))
arr = deque(list(map(int, input().split())))

queue = deque([0] * w)
weight = 0
result = 0
while arr:
    result += 1
    trug = arr.popleft()
    weight -= queue.popleft()
    if weight + trug <= L:
        queue.append(trug)
        weight += trug
    else:
        queue.append(0)
        arr.appendleft(trug)
result += w
print(result)