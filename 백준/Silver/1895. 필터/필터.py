import sys
input = sys.stdin.readline


def check(x, y):
    lst = []
    for nx in range(x, x + 3):
        for ny in range(y, y + 3):
            lst.append(arr[nx][ny])

    return sorted(lst)[4]


R, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(R)]

result = [[0] * (C - 2) for _ in range(R - 2)]

T = int(input())

for i in range(R - 2):
    for j in range(C - 2):
        result[i][j] = check(i, j)

ans = 0
for i in range(R - 2):
    for j in range(C - 2):
        if result[i][j] >= T:
            ans += 1

print(ans)