import sys
input = sys.stdin.readline

# 숫자, 게산식 더해가며 저장
def dfs(idx, num_lst, cal_lst):
    if idx == N:
        save_num = num_lst[0]
        for i in range(len(cal_lst)):
            save_num += cal_lst[i] + num_lst[i + 1]
        
        lst = []
        num = ''
        for n in range(len(save_num)):
            if save_num[n].isdigit():
                num += save_num[n]
                if n != len(save_num) - 1 and save_num[n + 1] == ' ':
                    continue
                else:
                    lst.append(int(num))
                    num = ''
            else:
                if save_num[n] == ' ':
                    continue
                else:
                    lst.append(save_num[n])
        
        sum = lst[0]
        
        for t in range(1, len(lst)):
            if lst[t] == '+':
                sum += lst[t + 1]
            elif lst[t] == '-':
                sum -= lst[t + 1]

        if sum == 0:
            result.append(save_num[:])
        return
    
    
    for cal in range(3):
        if cal == 0:
            dfs(idx + 1, num_lst + str(arr[idx]), cal_lst + '+')
        
        elif cal == 1:
            dfs(idx + 1, num_lst + str(arr[idx]), cal_lst + '-')                
        
        elif cal == 2:
            dfs(idx + 1, num_lst + str(arr[idx]), cal_lst + ' ')


T = int(input())
for tc in range(T):
    N = int(input())
    
    arr = list(range(1, N + 1))
    
    cnt = 0
    
    result = []
    
    dfs(1, str(arr[0]), '')
    
    result.sort()
    
    for rlt in result:
        print(rlt)
    
    if tc != T - 1:
        print() 