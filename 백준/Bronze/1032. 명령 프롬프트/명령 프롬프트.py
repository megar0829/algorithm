import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    if i == 0:
        arr = list(input())
    else:
        text = input()
        for j in range(len(arr)):
            if arr[j] != text[j]:
                arr[j] = '?'
print(*arr, sep='')