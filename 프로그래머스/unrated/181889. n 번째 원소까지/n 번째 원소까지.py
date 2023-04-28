def solution(num_list, n):
    answer = []
    cnt = 0
    for i in range(n):
        answer.append(num_list[cnt])
        cnt += 1
    return answer