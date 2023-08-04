import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr_dict = {}
for i in range(N):
    arr_dict[arr[i]] = 1
M = int(input())
check = list(map(int, input().split()))

for i in range(M):
    try:
        print(arr_dict[check[i]])
    except KeyError:
        print(0)