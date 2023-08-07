T = int(input())
for tc in range(1, T + 1):
    t, n = input().split()
    n = int(n)
    arr = list(input().split())
    arr_dict = {
        'ZRO': 0,
        'ONE': 0,
        'TWO': 0,
        'THR': 0,
        'FOR': 0,
        'FIV': 0,
        'SIX': 0,
        'SVN': 0,
        'EGT': 0,
        'NIN': 0
    }
    for i in range(n):
        arr_dict[arr[i]] += 1
    result = ''
    for i in arr_dict.keys():
        for j in range(arr_dict[i]):
            result += i + ' '
    print(t)
    print(result)