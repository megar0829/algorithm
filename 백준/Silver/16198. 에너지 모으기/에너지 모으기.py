def backTracking(lst, sum_val):
    global max_val
    if len(lst) == 2:
        max_val = max(max_val, sum_val)
        return
    for j in range(1, len(lst) - 1):
        save_val = lst.pop(j)
        backTracking(lst, sum_val + lst[j - 1] * lst[j])
        lst.insert(j, save_val)



N = int(input())
arr = list(map(int, input().split()))
max_val = 0
backTracking(arr, 0)
print(max_val)