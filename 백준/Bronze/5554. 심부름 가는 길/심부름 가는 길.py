import sys
input = sys.stdin.readline


time = 0
for _ in range(4):
    time += int(input())
x = time // 60
y = time % 60
print(x)
print(y)    