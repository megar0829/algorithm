from math   import factorial
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    west, east = map(int, input().split())
    if west == east:
        print(1)
    elif west > east:
        print(int(factorial(west) / (factorial(west - east) * factorial(east))))
    else:
        print(int(factorial(east) / (factorial(east - west) * factorial(west))))