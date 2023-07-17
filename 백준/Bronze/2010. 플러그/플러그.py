import sys
N = int(sys.stdin.readline().strip())
computer = 0
for _ in range(N):
    plug = int(sys.stdin.readline().strip())
    computer += plug - 1
print(computer + 1)