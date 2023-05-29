def solution(s):
    answer = ''
    numbers = list(s.split())
    n = []
    for i in numbers:
        n.append(int(i))
    n = sorted(n)
    answer += str(n[0])
    answer += ' '
    answer += str(n[-1])
    return answer