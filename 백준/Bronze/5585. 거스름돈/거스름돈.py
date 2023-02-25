N = int(input())
N = 1000 - N
yen = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in yen:
    cnt += N // i
    N = N % i
print(cnt)