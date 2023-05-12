def solution(arr):
    if len(arr) == 1:
        answer = [-1]
    else:
        arr.pop(arr.index(min(arr)))
        answer = arr
    return answer