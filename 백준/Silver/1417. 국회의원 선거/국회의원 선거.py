import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
m = arr.pop(0)
cnt = 0
if N != 1:
    while True:
        arr.sort(reverse=True)
        if m <= arr[0]:
            m += 1
            arr[0] -= 1
            cnt += 1
        else:
            break
print(cnt)