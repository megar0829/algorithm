import sys
N, K = map(int, sys.stdin.readline().split())
result = 1
for i in range(N, 0, -1):
    result *= i
for j in range(K, 0, -1):
    result /= j
for k in range(N-K, 0, -1):
    result /= k
print(int(result))