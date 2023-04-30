def solution(num_list):
    answer = 0
    sqr = 1
    sum_num = 0
    for i in num_list:
        sqr *= i
        sum_num += i
    if sqr < sum_num**2:
        answer = 1
    else:
        answer = 0   
    return answer