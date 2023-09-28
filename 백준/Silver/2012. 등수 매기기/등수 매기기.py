import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)])
result = 0
for i in range(1, N + 1):
    result += abs(arr[i - 1] - i)
print(result)