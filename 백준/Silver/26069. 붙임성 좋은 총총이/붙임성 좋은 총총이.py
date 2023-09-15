import sys
input = sys.stdin.readline

N = int(input())
arr = {}
c = 'ChongChong'
for _ in range(N):
    A, B = input().strip('\n').split()
    if (arr.setdefault(A, 0) or arr.setdefault(B, 0)) or (A == c or B == c):
        arr[A] = 1
        arr[B] = 1
print(sum(arr.values()))
