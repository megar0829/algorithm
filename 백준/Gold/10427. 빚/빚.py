import sys
input = sys.stdin.readline


T = int(input())
for tc in range(T):
    n, *arr = map(int, input().split())
    arr.sort()
    S = [1e9] * n
    S[0] = 0
    
    result = 0
    
    if n > 1:
        for i in range(n - 1):
            max_lst = arr[i]
            sum_lst = arr[i]
            for j in range(1, n - i):
                max_lst = max(max_lst, (arr[i + j]))
                sum_lst += arr[i + j]
                S[j] = min(S[j], (max_lst * (j + 1)) - sum_lst)
        
        result = sum(S)
        
    print(result)