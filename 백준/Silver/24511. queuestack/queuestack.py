import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
que = deque()

for i in range(N - 1, -1, -1):
    if A[i] == 0:
        que.append(B[i])

for i in range(M):
    que.append(C[i])
    print(que.popleft(), end=' ')