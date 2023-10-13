import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])

max_d = 0
flag = True

while flag:
    k = arr.pop()
    N -= 1
    for i in range(N):
        left, right = i, N - 1

        while left <= right:
            d = arr[i] + arr[left] + arr[right]

            if d < k:
                left += 1
            elif d > k:
                right -= 1
            elif d == k:
                max_d = d
                flag = False
                break

print(max_d)