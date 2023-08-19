import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
arr = [input().strip('\n') for _ in range(N)]
arr_len = []
result = 0
name = {}
save_name = deque()
for i in range(2, 21):
    name[i] = 0
    
for i in range(N):
    arr_len.append(len(arr[i]))

for i in range(1, K + 1):
    save_name.append(arr_len[i])
    name[arr_len[i]] += 1
    
for i in range(N - K - 1):
    result += name[arr_len[i]]
    name[save_name.popleft()] -= 1
    save_name.append(arr_len[i + K + 1])
    name[arr_len[i + K + 1]] += 1

for i in range(N - K - 1, N - 1):
    result += name[arr_len[i]]
    name[save_name.popleft()] -= 1
    
print(result)