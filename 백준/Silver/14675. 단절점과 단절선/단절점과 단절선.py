import sys
input = sys.stdin.readline

N = int(input())
arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    
    arr[a].append(b)
    arr[b].append(a)

q = int(input())

for _ in range(q):
    t, k = map(int, input().split())
    
    if t == 1:
        if (len(arr[k]) < 2):
            print("no")
            
        else:
            print("yes")

    elif t == 2:
        print("yes")