import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
sum_arr = [0 for _ in range(N + 1)]


for i in range(1, N +1):
    sum_arr[i] = sum_arr[i - 1] + numbers[i - 1]
    
    
for _ in range(M):
    i, j = map(int, input().split())
    result = sum_arr[j] - sum_arr[i - 1]
    print(result)
        