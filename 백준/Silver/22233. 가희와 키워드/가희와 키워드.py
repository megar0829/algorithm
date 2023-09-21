import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = {}
for _ in range(N):
    text = input().strip('\n')
    arr[text] = 1

for _ in range(M):
    text = list(input().strip('\n').split(','))
    for word in text:
        if word in arr:
            del arr[word]
    print(len(arr.keys()))