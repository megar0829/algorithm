N = int(input())
save_N, next_N, cnt = N, -1, 0
while next_N != N:
    next_N = (save_N%10)*10 + (save_N//10 + save_N%10)%10
    save_N = next_N
    cnt += 1
print(cnt)
