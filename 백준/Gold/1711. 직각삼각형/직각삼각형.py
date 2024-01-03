import sys
input = sys.stdin.readline

N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

cnt = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            a = (coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2
            b = (coordinates[j][0] - coordinates[k][0]) ** 2 + (coordinates[j][1] - coordinates[k][1]) ** 2
            c = (coordinates[k][0] - coordinates[i][0]) ** 2 + (coordinates[k][1] - coordinates[i][1]) ** 2

            if 2 * max(a, b, c) == a + b + c:
                cnt += 1
                
print(cnt)