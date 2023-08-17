for _ in range(10):
    tc = int(input())
    arr = list(map(int, input().split()))
    check = True
    front = -1
    while check:
        for i in range(5):
            front = (front + 1) % 8
            arr[front] -= (i + 1)
            if arr[front] <= 0:
                arr[front] = 0
                check = False
                break
    result = [0] * 8
    for i in range(8):
        front = (front + 1) % 8
        result[i] = arr[front]
    print(f'#{tc}', *result)