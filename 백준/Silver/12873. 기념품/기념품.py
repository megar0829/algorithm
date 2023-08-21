N = int(input())
arr = list(range(1, N + 1))
front = 0
t = 2
arr.pop(front)
while len(arr) > 1:
    n = t ** 3
    front = (front + n - 1) % len(arr)
    arr.pop(front)
    t += 1
if N == 1:
    print(1)
else:
    print(*arr)