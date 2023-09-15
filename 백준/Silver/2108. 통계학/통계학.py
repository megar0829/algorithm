import sys
input = sys.stdin.readline

N = int(input())
arr = []
arr_dict = {}
sum_num = 0
for _ in range(N):
    num = int(input())
    arr.append(num)
    arr_dict.setdefault(num, 0)
    arr_dict[num] += 1
    sum_num += num

# 1. 산술평균
print(round(sum_num / N))

# 2. 중앙값
print(sorted(arr)[N // 2])

# 3. 최빈값
many_num = []
max_val = max(arr_dict.values())
for k, v in arr_dict.items():
    if v == max_val:
        many_num.append(k)
if len(many_num) > 1:
    print(sorted(many_num)[1])
else:
    print(many_num[0])

# 4. 범위
print(max(arr) - min(arr))