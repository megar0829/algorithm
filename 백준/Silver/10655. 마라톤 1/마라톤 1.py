import sys
input = sys.stdin.readline

N = int(input())

point = []

for _ in range(N):
    x, y = map(int, input().split())
    point.append((x, y))

length = 0
for i in range(N - 1):
    length += abs(point[i + 1][0] - point[i][0]) + abs(point[i + 1][1] - point[i][1])

result = 1e9

for i in range(1, N - 1):
    dist = length - ((abs(point[i - 1][0] - point[i][0]) + abs(point[i - 1][1] - point[i][1]))\
         + (abs(point[i + 1][0] - point[i][0]) + abs(point[i + 1][1] - point[i][1])))\
             + (abs(point[i - 1][0] - point[i + 1][0]) + abs(point[i - 1][1] - point[i + 1][1]))
    result = min(result, dist)

print(result)