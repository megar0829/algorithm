import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    tc, *arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, 20):
        for j in range(i):
            if arr[j] > arr[i]:
                arr.insert(j, arr.pop(i))
                cnt += i - j
    print(f'{tc} {cnt}')
