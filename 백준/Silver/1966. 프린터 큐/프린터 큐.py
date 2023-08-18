import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr_idx = [[val, idx] for idx, val in enumerate(arr)]
    arr_sort = sorted(arr)
    cnt = 1
    front = -1
    max_idx = arr_sort.pop()
    while True:
        front = (front + 1) % len(arr_idx)
        if arr_idx[front][0] == max_idx:
            if arr_idx[front][1] == M:
                print(cnt)
                break
            arr_idx.pop(front)
            max_idx = arr_sort.pop()
            cnt += 1
            front -= 1