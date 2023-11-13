from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    flag = 0
    
    arr = deque(input()[1:-1].split(','))

    if n == 0:
        arr = []

    for func in p:
        if func == 'R':
            flag += 1
                                    
        elif func == 'D':
            if arr:
                if flag % 2:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                print('error')
                break
    else:
        if flag % 2:
            arr.reverse()
    
        print('[' + ','.join(arr) + ']')