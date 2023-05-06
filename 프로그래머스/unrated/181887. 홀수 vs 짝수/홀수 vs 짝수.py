def solution(num_list):
    answer = 0
    odd = []
    even = []
    cnt = 0
    for i in num_list:
        if cnt % 2 == 0:
            even.append(i)
            cnt += 1
        else:
            odd.append(i)
            cnt += 1
    if sum(even) > sum(odd):
        answer = sum(even)
    else:
        answer = sum(odd)
    return answer