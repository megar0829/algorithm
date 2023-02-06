def solution(numbers, num1, num2):
    answer = []
    while True:
        answer.append(numbers[num1])
        if num1 == num2:
            break
        num1 += 1
    return answer