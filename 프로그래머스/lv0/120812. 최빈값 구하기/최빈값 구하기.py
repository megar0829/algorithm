def solution(array):
    many_dict = {}
    for i in array:
        if i not in many_dict:
            many_dict[i] = 1
        else:
            many_dict[i] += 1
    lst_many = []
    for k, v in many_dict.items():
        if v == max(many_dict.values()):
            lst_many.append(k)
    if len(lst_many) == 1:
        answer = lst_many[0]
    else:
        answer = -1
    return answer