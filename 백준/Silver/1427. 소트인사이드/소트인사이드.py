import sys
input = sys.stdin.readline
N = input().rstrip()
numbers = list(N)
print(*sorted(numbers, reverse=True), sep='')