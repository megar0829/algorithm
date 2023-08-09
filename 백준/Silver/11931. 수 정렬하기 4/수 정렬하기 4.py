import sys
input = sys.stdin.readline

N = int(input())
arr = sorted([int(input()) for _ in range(N)], reverse=True)
for i in arr:
    print(i)