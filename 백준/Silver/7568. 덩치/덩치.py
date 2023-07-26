import sys
input = sys.stdin.readline

N = int(input())
size = [tuple(map(int, input().split())) for _ in range(N)]
rank = {}

for i in range(N):
    cnt = 1
    for kg, cm in size:
        if size[i][0] < kg and size[i][1] < cm:
            cnt += 1
    rank[i] = cnt
print(*rank.values())