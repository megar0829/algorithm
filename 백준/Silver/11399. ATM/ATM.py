import sys
input = sys.stdin.readline

N = int(input())
times = sorted(list(map(int, input().split())))
min_time = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    min_time[i] = min_time[i - 1] + times[i - 1]
print(sum(min_time))