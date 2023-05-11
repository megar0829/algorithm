def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    else:
        while True:
            if num % 2 == 0:
                num /= 2
                answer += 1
            elif num % 2 == 1:
                num = (num * 3) + 1
                answer += 1
            if num == 1:
                break
            elif answer == 500:
                answer = -1
                break
    return answer