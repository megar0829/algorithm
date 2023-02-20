import sys
import math
T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, input().split())
    print(math.lcm(A, B))