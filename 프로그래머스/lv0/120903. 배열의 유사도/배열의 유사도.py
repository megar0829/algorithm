def solution(s1, s2):
    answer = []
    for i in s1:
        if i not in s2:
            pass
        else:
            answer.append(i)
    return len(answer)