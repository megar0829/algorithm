N, K = map(int, input().split())

arr = list(map(int, input().split()))

sum_dict = dict()
sum_dict[0] = 1

sum_val = 0
ans = 0

for i in range(N):
    sum_val += arr[i]
    
    sum_dict.setdefault(sum_val - K, 0)
    sum_dict.setdefault(sum_val, 0)
    
    ans += sum_dict[sum_val - K]
    
    sum_dict[sum_val] += 1
        
print(ans)