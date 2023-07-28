n = input()
save_n = n[0]
turn_text = {
    '0': '1',
    '1': '0'
}
turn_cnt = 0
cnt = 0
for i in n:
    if i != save_n:
        if cnt == 1:
            save_n = turn_text[turn_text[i]]
            cnt = 0
        else:
            cnt += 1
            turn_cnt += 1
            save_n = turn_text[turn_text[i]]
print(turn_cnt)