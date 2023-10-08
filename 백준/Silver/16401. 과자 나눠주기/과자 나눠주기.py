def binary_search(start, end):
    global result
    
    # 종료조건
    if start > end:
        return 
    
    # 자를 과자의 크기
    mid = (start + end) // 2
    
    if mid == 0:
        return
    
    # 과자를 mid 크기 만큼 잘라서 개수를 세기
    snack = 0
    for i in range(N):
        if arr[i] >= mid:
            snack += arr[i] // mid
        else:
            break
    
    # 과자의 개수를 충족했다면 더 큰 크기를 찾기
    if snack >= M:
        result = max(result, mid)
        return binary_search(mid + 1, end)
    
    # 과자의 개수가 부족하다면 더 작은 과자를 찾기
    else:
        return binary_search(start, mid - 1)


M, N = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

result = 0
binary_search(1, max(arr))
print(result)