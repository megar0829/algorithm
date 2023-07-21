import sys
input = sys.stdin.readline
N = int(input())
A_lst = list(map(int, input().split()))
M = int(input())
X_lst = list(map(int, input().split()))
A_set = set(A_lst)


for i in range(M):
    if X_lst[i] in A_set:
        print(1)
    else:
        print(0)