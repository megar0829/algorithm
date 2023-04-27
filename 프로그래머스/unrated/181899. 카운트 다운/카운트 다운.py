def solution(start, end):
    answer = []
    for i in range(start - end + 1):
        answer.append(start)
        start -= 1
    return answer