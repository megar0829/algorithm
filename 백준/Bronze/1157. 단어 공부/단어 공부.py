# import sys
# sys.stdin = open('input.txt', 'r')

text = input()
cnt_text = {}
for i in text:
    up_text = i.upper()
    if up_text not in cnt_text:
        cnt_text[up_text] = 1
    else:
        cnt_text[up_text] += 1
max_cnt = 0
max_num = max(cnt_text.values())
for j in cnt_text.values():
    if j == max_num:
        max_cnt += 1
if max_cnt > 1:
    print('?')
else:
    for k, v in cnt_text.items():
        if v == max_num:
            print(k)