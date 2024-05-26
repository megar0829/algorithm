N = int(input())
K = input()

odd_cnt = 0
even_cnt = 0

for i in range(N):
    if int(K[i]) % 2:
        odd_cnt += 1
        
    else:
        even_cnt += 1

if odd_cnt > even_cnt:
    print(1)

elif odd_cnt == even_cnt:
    print(-1)

else:
    print(0)