def solution(n, times):
    answer = 0
    
    start, end = 1, max(times) * n
    
    while True:
        if start > end:
            break
        
        mid = (start + end) // 2
        
        cnt = 0
        for t in times:
            cnt += mid // t

        if cnt >= n:
            answer = mid
            end = mid - 1
        
        else:
            start = mid + 1
    
    return answer