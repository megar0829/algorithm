def solution(s):
    n = len(s)
    if n % 2 == 1:
        answer = s[(n - 1) // 2]    
    else:
        answer = s[(n // 2) - 1] + s[n // 2]
    return answer