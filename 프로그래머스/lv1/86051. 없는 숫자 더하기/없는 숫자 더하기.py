def solution(numbers):
    arr = list(range(0, 10))
    for i in numbers:
        if i in arr:
            arr.pop(arr.index(i))
    answer = sum(arr)
    return answer