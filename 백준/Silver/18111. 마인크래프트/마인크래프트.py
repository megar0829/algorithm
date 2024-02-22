import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

num_dict = dict()

min_cnt, min_val = 1e9, 257

num_dict = dict()

for i in range(N):
    for j in range(M):
        num_dict.setdefault(arr[i][j], 0)
        num_dict[arr[i][j]] += 1

numbers = num_dict.keys()

for height in range(257, -1, -1):
    use_block = 0
    get_block = 0
    
    for num in numbers:
        if num > height:
            get_block += (num - height) * num_dict[num]
        
        elif num < height:
            use_block += (height - num) * num_dict[num]
                
    if use_block > get_block + B:
        continue
    
    if min_cnt > use_block + (get_block * 2):
        min_cnt = use_block + (get_block * 2)
        min_val = height

print(min_cnt, min_val)