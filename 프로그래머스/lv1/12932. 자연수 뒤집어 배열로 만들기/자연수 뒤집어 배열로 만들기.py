def solution(n):
    n = str(n)[::-1]
    answer = []
    for i in n:
        answer.append(int(i))
    return answer