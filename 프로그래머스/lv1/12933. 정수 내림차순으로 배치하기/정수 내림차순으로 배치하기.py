def solution(n):
    res = []
    for i in str(n):
        res.append(i)
    res = sorted(res, reverse=True)
    answer = ''
    for i in res:
        answer += i
    answer = int(answer)    
    return answer