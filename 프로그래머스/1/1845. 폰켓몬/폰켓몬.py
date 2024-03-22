def solution(nums):
    N = len(nums) // 2
    
    nums = set(nums)
    
    n = len(nums)
    
    if N <= n:
        answer = N
        
    else:
        answer = n
    
    return answer