import sys
import math
input = sys.stdin.readline

r = int(input())
print(f'{round(math.pi * (r ** 2), 6):.6f}')
print(f'{(2 * (r ** 2)):.6f}')