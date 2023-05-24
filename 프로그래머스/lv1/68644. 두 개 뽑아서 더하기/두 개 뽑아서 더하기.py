def solution(numbers):
    answer = []
    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            n = numbers[i] + numbers[j]
            if n not in answer:
                answer.append(n)
    answer = sorted(answer)
    return answer