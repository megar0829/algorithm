def inorder(n):
    global result
    if n:
        inorder(ch1[n])
        result += arr[n]
        inorder(ch2[n])


for tc in range(1, 11):
    N = int(input())
    arr = [''] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
    for _ in range(N):
        edge = list(input().split())
        if len(edge) == 4:
            n, val = int(edge[0]), edge[1]
            c1, c2 = int(edge[2]), int(edge[3])
            arr[n] = val
            ch1[n], ch2[n] = c1, c2
        elif len(edge) == 3:
            n, val = int(edge[0]), edge[1]
            c = int(edge[2])
            arr[n] = val
            ch1[n] = c
        else:
            n, val = int(edge[0]), edge[1]
            arr[n] = val
    result = ''
    inorder(1)
    print(f'#{tc} {result}')