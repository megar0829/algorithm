import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)


def binary_search(start, end, target):
    global min_time
    if start > end:
        return

    mid = (start + end) // 2

    save_cnt = 0
    for i in range(N):
        save_cnt += mid // arr[i]

    if save_cnt < target:
        return binary_search(mid + 1, end, target)
    elif save_cnt >= target:
        min_time = min(min_time, mid)
        return binary_search(start, mid - 1, target)


N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])

start, end = 0, min(arr) * M
min_time = 10 ** 18
binary_search(start, end, M)

print(min_time)