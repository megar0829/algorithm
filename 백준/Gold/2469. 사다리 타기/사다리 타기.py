import sys
input = sys.stdin.readline


K = int(input())
N = int(input())

alp_lst = []

for num in range(65, 65 + K):
    alp_lst.append(chr(num))

alp = list(input().strip('\n'))

before_lst, after_lst = [], []

flag = False

for _ in range(N) :
    input_text = input().strip('\n')
    
    if input_text[0] == '?':
        flag = True
    
    else:
        if not flag:
            before_lst.append(input_text)
        else:
            after_lst.append(input_text)

after_lst.reverse()


for before in before_lst:
    for i in range(K - 1):
        if before[i] == '-':
            alp_lst[i], alp_lst[i + 1] = alp_lst[i + 1], alp_lst[i]

for after in after_lst:
    for i in range(K - 1):
        if after[i] == '-':
            alp[i], alp[i + 1] = alp[i + 1], alp[i]

result = ''
for i in range(K - 1):
    if alp_lst[i] == alp[i + 1] and alp_lst[i + 1] == alp[i]:
        result += '-'
    else :
        result += '*'

save_lst = alp_lst.copy()

for i in range(K - 1):
    if result[i] == '-':
        save_lst[i], save_lst[i + 1] = save_lst[i + 1], save_lst[i]

if save_lst == alp:
    print(result)
else:
    print('x' * (K - 1))