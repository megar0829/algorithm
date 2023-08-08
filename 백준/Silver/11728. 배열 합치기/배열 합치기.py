import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr_n = list(map(int, input().split()))
arr_m = list(map(int, input().split()))
print(*sorted(arr_n + arr_m))