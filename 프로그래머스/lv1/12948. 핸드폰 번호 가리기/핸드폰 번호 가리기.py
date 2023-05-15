def solution(phone_number):
    answer = ''
    for i in range(len(phone_number) -4):
        answer += '*'
    for i in phone_number[-4:]:
        answer += str(i)
    return answer