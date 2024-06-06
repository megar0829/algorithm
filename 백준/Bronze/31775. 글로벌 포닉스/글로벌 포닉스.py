k_cnt, l_cnt, p_cnt = 0, 0, 0

for _ in range(3):
    word = input()
    
    if word[0] == "k":
        k_cnt += 1
    elif word[0] == "l":
        l_cnt += 1
    elif word[0] == "p":
        p_cnt += 1
        
if k_cnt == 1 and l_cnt == 1 and p_cnt == 1:
    print("GLOBAL")
else:
    print("PONIX")