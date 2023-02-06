def solution(array, height):
    cnt = 0
    for i in array:
        if i > height:
            cnt += 1
    answer = cnt
    return answer