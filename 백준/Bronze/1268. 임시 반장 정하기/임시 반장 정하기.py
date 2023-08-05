import sys
input = sys.stdin.readline


def check_class(arr, n):
    global N
    check_row = [0] * N
    for i in range(5):
        for j in range(N):
            if j != n:
                if arr[n][i] == arr[j][i]:
                    check_row[j] += 1
    cnt = 0
    for i in range(N):
        if check_row[i] != 0:
            cnt += 1
    return cnt


N = int(input())
class_monitor = [0] * N
arr = [list(map(int, input().split())) for _ in range(N)]
max_num = 0
for i in range(N):
    class_monitor[i] = check_class(arr, i)
    if max_num < class_monitor[i]:
        max_num = class_monitor[i]

for i in range(N):
    if class_monitor[i] == max_num:
        print(i + 1)
        break
