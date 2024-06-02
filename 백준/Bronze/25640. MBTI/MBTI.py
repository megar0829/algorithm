mbti = input()
N = int(input())

cnt = 0

for _ in range(N):
    friend_mbti = input()
    
    if mbti == friend_mbti:
        cnt += 1

print(cnt)