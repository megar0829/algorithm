# import sys
# sys.stdin = open('input.txt', 'r')

N = int(input())
group_text = 0
for i in range(N):
    text = input()
    cnt = 0
    group = []
    for j in text:
        if j not in group:
            group.append(j)
        else:
            if j != save_text:
                group.pop(group.index(j))
            else:
                cnt += 1
        save_text = j
    if len(text) == len(group) + cnt:
        group_text += 1        
print(group_text)