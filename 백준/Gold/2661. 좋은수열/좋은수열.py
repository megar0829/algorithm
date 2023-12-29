def backTracking(idx):
    for i in range(1, (idx // 2) + 1):
        if arr[-i:] == arr[-2 * i:-i]: 
            return -1

    if idx == N:
        for i in range(N): 
            print(arr[i], end = '')
        return 0

    for i in range(1, 4):
        arr.append(i)
        
        if backTracking(idx + 1) == 0:
            return 0
        
        arr.pop()

N = int(input())
arr = []
backTracking(0)