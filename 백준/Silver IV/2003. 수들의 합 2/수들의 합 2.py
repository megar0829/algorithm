N, M = map(int, input().split())

arr = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while True:
    if right > N or left > right:
        break
    
    sum_arr = arr[left:right]
    
    result = sum(sum_arr)
    
    if result == M:
        cnt += 1
        right += 1
        
    elif result < M:
        right += 1
        
    else:
        left += 1
        
print(cnt)