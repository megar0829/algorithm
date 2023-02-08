def solution(emergency):
    answer = sorted(emergency,reverse=True)
    ind = []
    for i in emergency:
        ind.append(answer.index(i)+1)
    return ind