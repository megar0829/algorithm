import sys
input = sys.stdin.readline

N = int(input())
stack = [0] * N
top = -1
point = [0] * N
time = [0] * N
result = 0
for _ in range(N):
    homework = list(map(int, input().split()))
    if len(homework) != 1:
        A, T = homework[1], homework[2]
        top += 1
        point[top] = A
        time[top] = T - 1
    else:
        time[top] -= 1
        
    if time[top] == 0:
        result += point[top]
        top -= 1
print(result)