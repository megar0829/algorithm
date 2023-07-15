N = int(input())
result = 0
cnt = 0
for i in range(1, N):
    result += i
    if result > N:
        break
    cnt += 1 
   
if N == 1:
    cnt = 1
elif N == 2:
    cnt = 1
print(cnt)