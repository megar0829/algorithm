T = int(input())
for i in range(T):
    text = input()
    lft = []
    rgt = []
    for j in text:
        if len(lft) >= len(rgt):
            if j == '(':
                lft.append(j)
            else:
                rgt.append(j)
    if len(lft) == len(rgt):
        print('YES')
    else:
        print('NO')
    