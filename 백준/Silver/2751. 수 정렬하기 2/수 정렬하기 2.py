import sys
N = int(sys.stdin.readline())
numbers = list(int(sys.stdin.readline()) for i in range(N))
for j in sorted(numbers): print(j)