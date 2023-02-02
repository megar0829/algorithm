def solution(n):
    even = []
    for i in range(1, n+1):
        if i % 2 == 0:
            even.append(i)
    answer = sum(even)
    return answer