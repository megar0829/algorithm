def abs_num(x, y):
    if x >= y:
        return x - y
    else:
        return y - x


a, b = map(int, input().split())
cnt_a = a % 4
cnt_b = b % 4
if cnt_a == 0:
    cnt_a = 4
if cnt_b == 0:
    cnt_b = 4
rlt_a = (a - cnt_a) // 4
rlt_b = (b - cnt_b) // 4
print(abs_num(cnt_a, cnt_b) + abs_num(rlt_a, rlt_b))  