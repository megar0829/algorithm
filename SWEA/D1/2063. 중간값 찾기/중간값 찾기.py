# import sys
# sys.stdin = open('input.txt', 'r')
N = int(input())
numbers = list(map(int, input().split()))
print(sorted(numbers)[int((N-1)/2)])