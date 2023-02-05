def solution(slice, n):
    cnt = 1
    while True:
        if (slice*cnt) >= n:
            answer = cnt
            break
        else:
            cnt += 1
    return answer