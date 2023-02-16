def solution(cipher, code):
    answer = ''
    cnt = 1
    for i in cipher:
        if cnt == code:
            answer += i
            cnt = 0
        cnt += 1
    return answer